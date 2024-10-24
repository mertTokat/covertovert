# ICMP Packet Sender and Receiver

This project consists of two Python scripts, `icmp_sender.py` and `icmp_receiver.py`, which uses the Scapy library to send and receive ICMP packets.

# Authors

Berk Ulutaş 2522084

Mert Tokat 2644383

Group 15

Link to the project repository: https://github.com/mertTokat/covertovert 

## Scripts

### 1. icmp_sender.py

#### Code
```python
from scapy.all import *

def send_icmp_packet():
    target_ip = "receiver"

    # Create an ICMP packet with TTL value set to 1
    icmp_packet = IP(dst=target_ip, ttl=1)/ICMP()

    send(icmp_packet)

if __name__ == "__main__":
    send_icmp_packet()
```

#### Explanation
- The script sends a single ICMP Request packet to receiver.
- The packet has a TTL value of 1.
- The ICMP packet is sent using the send() function from scapy library.

### 2. icmp_receiver.py
```python
from scapy.all import *

def handle_packet(packet):
    # Check if the packet is an ICMP request 
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:
        packet.show()  # Print the ICMP request

def capture_icmp():
    sniff(filter="icmp", prn=handle_packet)  # Waits for incoming ICMP packets

if __name__ == "__main__":
    capture_icmp() # This will block and wait for incoming packets

```
#### Code

#### Explanation
- The script listens for network packets.
- It captures only ICMP packets.
- For each packet, it checks if it's a request (ICMP Type 8).
- If it's a request, the packet details are printed using the show() method.