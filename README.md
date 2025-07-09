# 🛠️ Modular Penetration Testing Toolkit

A simple Python-based command-line toolkit for penetration testing. This modular script includes a **Port Scanner** and a **Brute Force Login Tool** using HTTP Basic Authentication.

---

## 👨‍💻 Author

- **Name**: Anurag Batham
- **GitHub**: [github.com/hninlaekhaing](https://github.com/anuragbatham2007)  
- **Project**: Developed as part of CodTech Cybersecurity Internship

---

## 🧩 Features

- 🔍 **Port Scanner** — Scans commonly used ports on a target IP/domain.
- 🔐 **Brute Force Login** — Attempts to brute-force HTTP Basic Auth with common credentials.
- 🧱 Modular design — Easy to expand with more modules (e.g., XSS, SQLi, Directory Fuzzing).

---

## 🗂️ Project Structure

penetration-toolkit/
├── main.py # Main CLI menu interface
├── modules/
│ ├── init.py
│ ├── port_scanner.py # Contains port scanning logic
│ └── brute_forcer.py # Contains brute-force login logic
├── wordlists/
│ ├── usernames.txt # (Optional) List of usernames
│ └── passwords.txt # (Optional) List of passwords
├── README.md # Documentation

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/penetration-toolkit.git
   cd penetration-toolkit
Install any required dependencies:
The built-in modules like socket, requests, etc., are usually pre-installed with Python.

If you're using external packages:

bash
Copy
Edit
pip install -r requirements.txt
Ensure the folder structure is correct:

The main script (main.py) should be outside the modules/ folder.

Inside modules/, you should have port_scanner.py and brute_forcer.py.

## ▶️ Usage
Run the toolkit from terminal:

bash
Copy
Edit
python main.py
Menu Options
Option 1: Enter an IP or domain to scan common ports (e.g., 22, 80, 443).

Option 2: Enter a URL with HTTP Basic Auth (e.g., http://example.com/login) to start brute force.

Option 3: Exit the toolkit.

## ⚠️ Legal Disclaimer
This toolkit is intended for educational purposes only. Do NOT use it on networks or systems without explicit permission. Unauthorized scanning or brute-forcing is illegal and unethical.
