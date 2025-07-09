import socket

def scan_ports(host, ports=range(1, 1025)):
    print(f"\n🔍 Scanning ports on {host}...\n")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((host, port))
            print(f"[OPEN] Port {port}")
            s.close()
        except:
            pass
