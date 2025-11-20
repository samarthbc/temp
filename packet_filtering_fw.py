# Simple packet filtering firewall demo
packets = [
    {"src_ip": "192.168.1.2", "dst_port": 80},
    {"src_ip": "10.0.0.5", "dst_port": 22},
]

# Define allowed IPs and ports
allowed_ips = ["192.168.1.2"]
allowed_ports = [80, 443]

for pkt in packets:
    if pkt["src_ip"] in allowed_ips and pkt["dst_port"] in allowed_ports:
        print(f"Packet allowed: {pkt}")
    else:
        print(f"Packet blocked: {pkt}")
