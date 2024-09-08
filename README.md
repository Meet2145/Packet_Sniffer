# Packet Sniffer

## Overview

This project includes a Python script that captures network packets in real-time using the **Scapy** library. It extracts and logs important information like the source and destination IP addresses, as well as the packet type (e.g., TCP, UDP, ICMP).

## Features

- **Packet Sniffing**: Capture live network packets on a specified network interface.
- **Protocol Analysis**: Identify the protocol used (TCP, UDP, ICMP) and display relevant information.
- **Logging**: Logs captured packet details both in the console and to a file.

## Prerequisites

- **Python 3.x**
- **Scapy Library**: Install with:
  ```bash
  pip install scapy

- Npcap (for Windows users): Install Npcap from Npcap's official website and enable WinPcap compatibility mode.

Example
Running the Packet Sniffer:

bash
python packet_sniffer.py
# When prompted, enter the network interface name (e.g., Wi-Fi, eth0).
# The output will display captured packet details like source IP, destination IP, and protocol.

# Example Output:
[*] Starting packet sniffing on interface eth0...
TCP Packet >> Src: 192.168.1.10, Dst: 192.168.1.1, Src Port: 56789, Dst Port: 80
UDP Packet >> Src: 192.168.1.12, Dst: 192.168.1.1, Src Port: 1234, Dst Port: 53

Notes
Admin Privileges: On Windows, run the script as Administrator. On Linux/macOS, use sudo if needed.
Log File: The captured packets are logged in a file called packets.log in the same directory as the script.

Disclaimer
This tool is intended for educational purposes and ethical use only. Ensure you have permission to monitor network traffic in your environment.
