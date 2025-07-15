from flask import Flask, render_template, request, redirect, url_for, session, send_file
from datetime import datetime
import csv
import os
from utils.threat_detector import parse_logs
from utils.ip_lookup import get_ip_location
from alerts.telegram_alerts import send_telegram_alert
from functools import wraps

app = Flask(__name__)
app.secret_key = 'cloudshield_secret_key'

# ✅ Hardcoded login (for now)
VALID_USER = {
    "email": "vanshdhiman22@gmail.com",
    "password": "Vansh@90188"
}

# 🔐 Decorator to protect routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ⛔ Load blacklist IPs
def load_blacklist(filepath='blacklist.txt'):
    try:
        with open(filepath, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []

# 🔓 Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == VALID_USER["email"] and password == VALID_USER["password"]:
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# 🔐 Logout Route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# 🧠 Dashboard Route
@app.route('/')
@login_required
def dashboard():
    start_str = request.args.get("start")
    end_str = request.args.get("end")

    start_date = datetime.fromisoformat(start_str) if start_str else None
    end_date = datetime.fromisoformat(end_str) if end_str else None

    result = parse_logs('logs/sample_logs.json', start_date, end_date)
    threat_data = result["threat_counts"]
    log_entries = result["logs"]

    blacklist = load_blacklist()
    blacklisted_hits = []

    for entry in log_entries:
        if entry.get("sourceIPAddress") in blacklist:
            blacklisted_hits.append(entry.get("sourceIPAddress"))

    for attack_type, count in threat_data.items():
        if count >= 3:
            send_telegram_alert(f"🚨 CloudShield Alert 🚨\nAttack Type: {attack_type}\nDetections: {count}")

    for ip in blacklisted_hits:
        send_telegram_alert(f"⚠ Blacklisted IP Detected: {ip}")

    return render_template(
        'dashboard.html',
        data=threat_data,
        logs=log_entries,
        blacklisted=blacklisted_hits,
        start=start_str,
        end=end_str
    )

# 🌍 Attack Map Route
@app.route('/map')
@login_required
def map_view():
    raw_ips = ["203.0.113.10", "192.168.1.22", "45.33.32.156"]
    attack_types = ["Login Failure", "S3 Access", "IAM Abuse"]

    data = []
    for ip, attack_type in zip(raw_ips, attack_types):
        location = get_ip_location(ip)
        if location:
            location["attack_type"] = attack_type
            data.append(location)

    return render_template('map.html', data=data)

# 📤 Export CSV Route
@app.route('/export_csv')
@login_required
def export_csv():
    result = parse_logs('logs/sample_logs.json')
    log_entries = result["logs"]

    csv_path = 'exported_logs.csv'
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['eventTime', 'sourceIPAddress', 'eventName', 'awsRegion', 'errorMessage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in log_entries:
            writer.writerow({
                'eventTime': row.get('eventTime', ''),
                'sourceIPAddress': row.get('sourceIPAddress', ''),
                'eventName': row.get('eventName', ''),
                'awsRegion': row.get('awsRegion', ''),
                'errorMessage': row.get('errorMessage', '')
            })

    return send_file(csv_path, as_attachment=True)

# 🚀 Run Server
if __name__ == '__main__':
    app.run(debug=True)

