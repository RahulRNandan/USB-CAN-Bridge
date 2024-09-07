import serial
import can

# Set up USB serial port
usb_port = serial.Serial('/dev/pts/1', 9600)

# Set up virtual CAN interface
can_interface = 'vcan0'
bus = can.interface.Bus(can_interface, bustype='socketcan')

try:
    while True:
        # Read from USB port
        usb_data = usb_port.readline().strip()
        
        if usb_data:
            # Create a CAN message
            can_msg = can.Message(arbitration_id=0x123,
                                  data=usb_data,
                                  is_extended_id=False)
            bus.send(can_msg)
            
            print(f"Sent to CAN: {usb_data}")
        
        # Receive CAN messages
        can_msg = bus.recv()
        if can_msg:
            # Send CAN data to USB port
            usb_port.write(can_msg.data)
            print(f"Received from CAN: {can_msg.data}")
except KeyboardInterrupt:
    pass
finally:
    usb_port.close()
