# USB-CAN Bridge

## Overview

The USB-CAN Bridge project facilitates communication between USB and CAN interfaces, tailored for applications in the automotive industry and embedded systems. This project simulates the operation of a USB-CAN converter, enabling seamless data transfer between USB ports and CAN networks.

## Project Domain

- **Automotive Industry**
- **Embedded Software Design**
- **Light Motor Vehicles (LMV)**

## Tools and Technologies

- **Renesas CS+ IDE**
- **R5F10BGC Microcontroller**
- **Embedded C**
- **UART**
- **CAN**
- **CAN Analyzer**
- **Emulators**
- **SPI**
- **Linux**
- **MATLAB Simulink**
- **Hardware Design**
- **Board Bring Up**
- **Schematic Analysis**

## Description

This project involves designing and implementing a USB-CAN converter for real-time monitoring and analysis in Light Motor Vehicles (LMVs). The system allows for communication between USB and CAN interfaces, integrating performance-enhancing algorithms for LMVs.

## Features

- **USB to CAN Communication**: Converts data from USB to CAN and vice versa.
- **Real-time Monitoring**: Allows real-time monitoring of CAN messages through USB.
- **Simulation and Emulation**: Simulates CAN and USB interfaces using virtual devices for development and testing purposes.

## Setup Instructions

### Prerequisites

- Python 3
- `socat` for creating virtual serial ports
- `python-can` and `pyserial` libraries

### Installation

1. **Install Required Packages**

   For Linux distributions:
   ```bash
   sudo apt-get install socat python3-pip python3-venv
   ```
2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
Install Python Libraries
```
```bash
pip install pyserial python-can
Setup Virtual CAN Interface
```
```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```
3. Create Virtual Serial Ports

```bash
socat -d -d pty,raw,echo=0 pty,raw,echo=0 &
```
4. Running the Bridge
Run the USB-CAN Bridge Script

```bash
python usb_can_bridge.py
```
5. Send Test Data

Open a terminal and write data to the USB virtual port:

```bash
echo "Test Data" > /dev/pts/1
```
Monitor CAN messages:

```bash
candump vcan0
```
6. Read from the other USB virtual port:

```bash

cat /dev/pts/3
usb_can_bridge.py Script
```
The script usb_can_bridge.py bridges the data between USB and CAN interfaces. Below is the example code:

```python
import os
import can
import time

# USB and CAN device paths
usb_device = '/dev/pts/1'
can_interface = 'vcan0'

# Open USB pseudo-terminal
usb_port = open(usb_device, 'r+b', buffering=0)

# Set up CAN interface
bus = can.interface.Bus(channel=can_interface, bustype='socketcan')

while True:
    try:
        # Read data from USB
        data = usb_port.read(64)
        if data:
            # Create CAN message
            message = can.Message(arbitration_id=0x123, data=data, is_extended_id=False)
            # Send CAN message
            bus.send(message)

        # Receive CAN message
        message = bus.recv()
        if message:
            # Write CAN message data to USB
            usb_port.write(message.data)

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(0.1)
```

## 7. Documentation
For further details on how the system works, refer to the Documentation.

## 8. Contributing
Contributions are welcome! Please follow the guidelines provided in the CONTRIBUTING.md.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
