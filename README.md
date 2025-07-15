# ☁️ CloudShield: Real-Time Cloud-Based Threat Detection System


CloudShield is a real-time threat detection and visualization system for AWS-like cloud environments. It analyzes log data, detects attack patterns, sends Telegram alerts, and visualizes threats on a dashboard and interactive world map.

---

## 🚀 Features

- ✅ **AWS-style Log Parsing**
- 📊 Real-Time Dashboard with Charts (Chart.js)
- 🌍 Attack Map (Leaflet.js)
- 📅 Date-based Filtering
- ⚠ Blacklist IP Detection & Alerts
- 🔔 Telegram Bot Alerts
- 🔐 Login System (Session-based)
- 📤 Export Logs to CSV

---

## 🧠 Technologies Used

| Layer       | Tools/Libraries               |
|-------------|-------------------------------|
| Backend     | Python, Flask                 |
| Frontend    | HTML, CSS, Chart.js, Leaflet  |
| Bot Alerts  | Telegram Bot API              |
| Log Parsing | Custom JSON AWS-style parser  |

---

## 📁 Project Structure

CloudShield/
├── app.py ← Main Flask app
├── templates/
│ ├── dashboard.html ← Dashboard UI
│ ├── login.html ← Login Page
│ └── map.html ← World Map View
├── static/
│ ├── css/style.css ← Styling
│ └── js/charts.js ← Chart.js logic
├── logs/sample_logs.json ← AWS-style logs
├── blacklist.txt ← IP blacklist file
├── utils/
│ ├── threat_detector.py ← Log parsing & threat detection
│ └── ip_lookup.py ← IP geolocation logic
├── alerts/
│ └── telegram_alerts.py ← Telegram bot integration
└── README.md ← This file

yaml
Copy
Edit

---

## 📸 Screenshots

> (Take these after launching the app)

- 🖼 `dashboard.html` with charts
- 🗺 `map.html` with attack markers
- 🔐 `login.html` page
- 🧾 Telegram alert example
- 📤 Export CSV download
- 🛑 Blacklist alert popup

---

## 📡 Telegram Alerts Setup

- Bot Token via [@BotFather](https://t.me/BotFather)
- Send message alerts using: `send_telegram_alert(msg)`

---

## 👨‍💻 Author

- **Name**: Vansh Dhiman   
- **GitHub**: [github.com/Vanshdhiman22](https://github.com/Vanshdhiman22)

---

## 📦 License

MIT — Feel free to use and modify!
