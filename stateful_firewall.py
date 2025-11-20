# Simple stateful firewall demo
packets = [
    {"src_ip": "192.168.1.2", "dst_port": 80},
    {"src_ip": "192.168.1.2", "dst_port": 80},
]

# Session table to track active connections
session_table = set()

for pkt in packets:
    connection = (pkt["src_ip"], pkt["dst_port"])
    if connection in session_table:
        print(f"Packet allowed (return traffic): {pkt}")
    else:
        print(f"Packet allowed (new connection): {pkt}")
        session_table.add(connection)
