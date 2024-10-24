from scapy.all import *

def handle_packet(packet):
    # Check if the packet is an ICMP request 
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:
        packet.show()  # Print the ICMP request

def capture_icmp():
    sniff(filter="icmp", prn=handle_packet)  # Waits for incoming ICMP packets

if __name__ == "__main__":
    capture_icmp() # This will block and wait for incoming packets

