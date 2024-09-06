from scapy.all import sniff, IP, Raw
from scapy.layers.http import HTTPRequest

def process_packet(packet):

    if packet.haslayer(HTTPRequest):

        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        src_ip = packet[IP].src
        

        print("HTTP Request >>", url)
        print("Source IP >>", src_ip)
        
    
        with open("sniffed_packets.log", "a") as log_file:
            log_file.write(f"[+] HTTP Request from {src_ip}: {url}\n")

def start_sniffer(interface):
    print(f"[*] Starting packet sniffer on interface {interface}...")
    sniff(iface=interface, prn=process_packet, store=False)

if __name__ == "__main__":
    interface = input("Enter the interface to sniff on (e.g., Wi-Fi, eth0): ")
    start_sniffer(interface)
