from modules import port_scanner, brute_forcer

def show_menu():
    print("\n🛠️  Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Force Login (HTTP Basic Auth)")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        target = input("Enter target IP or domain: ")
        port_scanner.scan_ports(target)
    elif choice == "2":
        url = input("Enter target login URL: ")
        brute_forcer.brute_force_login(url)
    elif choice == "3":
        print("Exiting toolkit. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
