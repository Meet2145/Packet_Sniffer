# Packet Sniffer

## Overview

This project includes a Python script that captures network packets in real-time using the **Scapy** library. It logs important details about each packet, such as source and destination IP addresses, protocol type (TCP, UDP, ICMP), and more. This tool is useful for network analysis and learning how packet sniffing works.

## Features

- **Packet Sniffing**: Capture live network traffic on a specified network interface.
- **Protocol Analysis**: Identify packet types such as TCP, UDP, and ICMP, and display relevant information.
- **Logging**: Save captured packet details to a log file for future analysis.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed.
- **Scapy Library**: Install the Scapy library by running:
  ```bash
  pip install scapy
Npcap (for Windows users): Install Npcap from Npcap's official website and enable WinPcap compatibility mode.
Installation
Clone the Repository (Optional):

bash
Copy code
git clone https://github.com/your-username/packet-sniffer.git
cd packet-sniffer
Install Dependencies: Install Scapy using the following command:

bash
Copy code
pip install scapy
Usage
Run the Script:

Open a terminal or command prompt (as Administrator on Windows).
Run the script:
bash
Copy code
python packet_sniffer.py
Choose Network Interface:

When prompted, enter the network interface name (e.g., Wi-Fi, eth0):
bash
Copy code
Enter the interface to sniff on (e.g., Wi-Fi, eth0): eth0
Monitor Output:

The script will display the details of each packet (IP, protocol, ports) in real-time.
Packet details will also be saved in a log file named packets.log in the same directory as the script.
Example Output
bash
Copy code
[*] Starting packet sniffing on interface eth0...
TCP Packet >> Src: 192.168.1.10, Dst: 192.168.1.1, Src Port: 56789, Dst Port: 80
UDP Packet >> Src: 192.168.1.12, Dst: 192.168.1.1, Src Port: 1234, Dst Port: 53
Notes
Admin Privileges: On Windows, you must run the script as Administrator. On Linux/macOS, use sudo if necessary.
Permissions: Ensure you have the required permissions to sniff network traffic on the selected interface.
Log File: All captured packets are saved in packets.log in the script directory.
Example Commands
Starting the packet sniffer:

bash
Copy code
python packet_sniffer.py
# When prompted, enter the network interface name (e.g., Wi-Fi, eth0).
Example Output:

bash
Copy code
[*] Starting packet sniffing on interface eth0...
TCP Packet >> Src: 192.168.1.10, Dst: 192.168.1.1, Src Port: 56789, Dst Port: 80
UDP Packet >> Src: 192.168.1.12, Dst: 192.168.1.1, Src Port: 1234, Dst Port: 53
Disclaimer
This tool is intended for educational purposes and ethical use only. Ensure that you have the necessary permissions to monitor network traffic in your environment.

