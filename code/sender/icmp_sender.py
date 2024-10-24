from scapy.all import *

def send_icmp_packet():
    target_ip = "receiver"

    # Create an ICMP packet with TTL value set to 1
    icmp_packet = IP(dst=target_ip, ttl=1)/ICMP()

    send(icmp_packet)

if __name__ == "__main__":
    send_icmp_packet()