
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
Example
Running the Script:

bash
Copy code
python packet_sniffer.py

## Output: Starting packet sniffing on interface eth0...

Captured Packet Example:

-TCP Packet >> Src: 192.168.1.10, Dst: 192.168.1.1, Src Port: 56789, Dst Port: 80
-UDP Packet >> Src: 192.168.1.12, Dst: 192.168.1.1, Src Port: 1234, Dst Port: 53

## Disclaimer
This tool is intended for educational purposes and ethical use only. Ensure that you have the necessary permissions to monitor network traffic in your environment.

