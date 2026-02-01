import socket

# -------------------------------

# -------------------------------
def scan(target, ports):
    print(f"\n Scanning target: {target}")
    
    for port in range (1, ports):
        scan_port(target, port)
def scan_port(ipaddress, port):
    try:
        socketvar = socket.socket()
        socketvar.connect(ipaddress, port)
        print ('port opened'+ str(port))
        socketvar.close()
    except:
        pass
# ----------------------------
# -------------------------------
targets = input("Enter target(s), split multiple with comma: ")
ports = int(input('how many ports to scan? ')

# -------------------------------
              
# -------------------------------
if ',' in targets:
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(''), ports)
else:
    scan(targets, ports)
