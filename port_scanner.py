import socket

target = input("Enter the IP address or domain to scan: ")
start_port = 1
end_port = 1024

print(f"Scanning {target} for ports {start_port} to {end_port}...")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()
