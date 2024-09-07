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
