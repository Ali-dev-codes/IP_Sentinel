import requests
from .models import IPAddress


def scan_ip_details(ip_id):
    ip_obj = IPAddress.objects.get(id=ip_id)
    url = 'https://api.abuseipdb.com/api/v2/check'
    params = {'ipAddress': ip_obj.address, 'maxAgeInDays': '90'}

    # IMPORTANT: Ensure your Key is strictly alphanumeric characters only.
    headers = {
        'Accept': 'application/json',
        'Key': '916ca0ede32e11c0b58b6f8a5165a7189ca57b881ae5a4a99550b44a5171b6c4fdb2336a5da87c8c'
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        # Response handling with English terminal logs
        if response.status_code == 429:
            print(f"❌ Error: Daily quota reached (100 checks). Try again tomorrow or use another key.")
        elif response.status_code == 401:
            print(f"❌ Error: API Key is invalid or not activated.")
        elif response.status_code == 200:
            data = response.json()['data']
            score = data.get('abuseConfidenceScore', 0)
            ip_obj.reputation_score = int(score)

            # Severity Logic
            if ip_obj.reputation_score >= 75:
                ip_obj.severity = 'high'
            elif ip_obj.reputation_score >= 25:
                ip_obj.severity = 'medium'
            else:
                ip_obj.severity = 'low'

            ip_obj.status = 'Online'
            print(f"✅ Scan successful: {ip_obj.address} | Score: {score}")
        else:
            print(f"⚠️ Unknown Error. HTTP Status: {response.status_code}")

        # Geolocation Fetching (Separate Free API)
        geo_url = f"http://ip-api.com/json/{ip_obj.address}"
        geo_res = requests.get(geo_url).json()
        if geo_res.get('status') == 'success':
            ip_obj.country = geo_res.get('country', 'Unknown')

        # Final Save to Database
        ip_obj.save()

    except Exception as e:
        print(f"❌ Connection Error: {e}")