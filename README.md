# 🛡️ IP-Sentinel: Advanced IP Intelligence & Monitoring Tool

**IP-Sentinel** is a comprehensive network security tool built with **Django**. It provides a 3-stage analysis for any IP address, combining threat intelligence, network availability, and geographical tracking in one sleek dashboard.

---

## 🚀 The 3-Stage Analysis Process
1.  **Security Reputation:** Integrates with **AbuseIPDB API** to check if an IP is reported for malicious activity (spam, hacking, etc.).
2.  **Live Connectivity (Ping):** Performs a real-time ICMP Ping to verify if the host is **Online** or **Offline**.
3.  **Geolocation Tracking:** Retrieves precise geographical data, including City, Country, and ISP information.

## ✨ Core Features
* **Bulk Import/Export:** Upload a list of IPs via files for mass scanning and export results for reporting.
* **Threat Intelligence:** Instantly see the confidence score of an IP's maliciousness.
* **Automated Monitoring:** Keep track of your network assets with a professional UI.
* **Responsive Dashboard:** A modern, user-friendly interface to visualize all your IP data.

## 🛠️ Installation & Setup

1.Clone the Repository:
   ```bash
   git clone [https://github.com/Ali-dev-codes/IP_Sentinel.git](https://github.com/Ali-dev-codes/IP_Sentinel.git)
   cd IP_Sentinel
2. Install Dependencies****pip install -r requirements.txt****
3. Database Migration****python manage.py migrate****
4. Start the Server****python manage.py runserver****

⚙️ Tech Stack
Backend: Python 3.x / Django 5.x
APIs: AbuseIPDB API & Geolocation Services
Networking: ICMP Ping (OS Level)
Frontend: Bootstrap 5 / Custom CSS

Developed by [Ali]
