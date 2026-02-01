# Port-scanner
#  Python Port Scanner

A simple port scanner built in Python using the **socket** library.  
It allows scanning one or multiple targets and checks which ports are open.

This project is made for learning networking and cybersecurity basics.

---

##  Features

- Scan a single IP or multiple targets
- Custom port range selection
- Detects open ports
- Timeout handling
- Beginner-friendly code

---

##  Requirements

- Python 3.x  
(No extra libraries required)

---

## How to Run

Run the script:
You will be asked to enter:

- Target IP(s) (separate multiple with comma)
- Start port
- End port

---

##  How It Works

The program:

1. Takes targets from the user  
2. Splits multiple targets using commas  
3. Loops through the selected port range  
4. Uses `socket.connect_ex()` to check if ports are open  

If a port responds, it is marked as **OPEN**.

---

## Disclaimer

This tool is for **educational purposes only**.  
Only scan systems you own or have permission to test.

---
