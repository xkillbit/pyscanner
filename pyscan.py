import socket
import datetime

# Define a list of IP addresses to scan
ips = []
with open('targets.txt','r') as f:
  d = f.readlines()
  for each in d:
    ips.append(each)


# Define a list of ports to scan
ports = [21, 22, 23, 80, 443]

# Create a table to store the results
results = []

# Iterate through each IP address
for ip in ips:
    row = {}
    row['ip'] = ip
    row['status'] = 'online'
    row['open_ports'] = []

    # Iterate through each port
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))

        # If the port is open, add it to the list of open ports
        if result == 0:
            row['open_ports'].append(port)

    # If no ports are open, mark the status as offline
    if not row['open_ports']:
        row['status'] = 'offline'

    results.append(row)

# Print the results in a tabular format
print("IP Address\t\tStatus\t\tOpen Ports")
print("-------------------------------------------------")
for row in results:
    open_ports_str = ','.join(str(p) for p in row['open_ports'])
    print("{}\t\t{}\t\t{}".format(row['ip'], row['status'], open_ports_str))
