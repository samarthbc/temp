# Simple application firewall demo
requests = [
    {"user": "alice", "url": "http://dsce.edu.in"},
    {"user": "bob", "url": "http://blocked.com"},
]

# Define allowed URLs
allowed_urls = ["http://example.dsce.edu.in", "http://safe-site.com"]

for req in requests:
    if req["url"] in allowed_urls:
        print(f"Request allowed: {req}")
    else:
        print(f"Request blocked by app firewall: {req}")
