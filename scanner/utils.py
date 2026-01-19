import requests
from django.conf import settings  # لاستدعاء المفتاح من الـ settings
from .models import IPAddress

def scan_ip_details(ip_id):
    ip_obj = IPAddress.objects.get(id=ip_id)
    url = 'https://api.abuseipdb.com/api/v2/check'
    params = {'ipAddress': ip_obj.address, 'maxAgeInDays': '90'}

    # استدعاء المفتاح من الإعدادات التي تقرأ من ملف .env
    headers = {
        'Accept': 'application/json',
        'Key': settings.ABUSE_API_KEY
    }

    try:
        response = requests.get(url, headers=headers, params=params)

        # التعامل مع الاستجابة
        if response.status_code == 429:
            print(f"❌ Error: Daily quota reached.")
        elif response.status_code == 401:
            print(f"❌ Error: API Key is invalid.")
        elif response.status_code == 200:
            data = response.json()['data']
            score = data.get('abuseConfidenceScore', 0)
            ip_obj.reputation_score = int(score)

            # منطق تحديد الخطورة
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

        # جلب الموقع الجغرافي
        geo_url = f"http://ip-api.com/json/{ip_obj.address}"
        geo_res = requests.get(geo_url).json()
        if geo_res.get('status') == 'success':
            ip_obj.country = geo_res.get('country', 'Unknown')

        ip_obj.save()

    except Exception as e:
        print(f"❌ Connection Error: {e}")