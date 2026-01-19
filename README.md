# 🛡️ IP-Sentinel: Network Security & SOC Tool

**IP-Sentinel** is a professional network monitoring and IP management system built with **Django**. It is designed to help Security Operations Center (SOC) analysts track network assets and perform automated port scanning.

---

## ✨ Key Features
* **Automated Port Scanning:** Integrated with **Nmap** to detect open ports and services.
* **IP Asset Management:** Easily add, edit, and track IP addresses in a centralized database.
* **Security Dashboard:** A clean, responsive interface to visualize network status.
* **Data Portability:** Support for importing/exporting data via Excel and CSV formats.
* **Modern UI:** Built with Bootstrap 5 for a smooth user experience.

## 🛠️ Installation & Setup

To run this project locally, follow these steps in your terminal:

### 1. Clone the Repository
```bash
git clone [https://github.com/Ali-dev-codes/IP_Sentinel.git](https://github.com/Ali-dev-codes/IP_Sentinel.git)
cd IP_Sentinel
2. Install Dependencies****pip install -r requirements.txt****
3. Database Migration****python manage.py migrate****
4. Start the Server****python manage.py runserver****


Requirements:
Python 3.x
Django 5.x
Nmap Engine: (Must be installed on your OS for the scanner to function).

Disclaimer:
This tool is developed for educational and authorized security testing purposes only. Always ensure you have permission before scanning any network.
Developed by [Ali]
