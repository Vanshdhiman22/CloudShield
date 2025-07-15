import requests

def get_ip_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            return {
                'ip': ip,
                'lat': data['lat'],
                'lon': data['lon'],
                'country': data['country'],
                'city': data['city']
            }
    except:
        pass
    return None
