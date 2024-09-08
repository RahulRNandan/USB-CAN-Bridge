import time

class SPIEmulator:
    def __init__(self):
        self.data = []

    def spi_init(self):
        print("SPI Initialized.")

    def spi_transfer(self, data):
        self.data = data
        for byte in data:
            print(f"Transferring over SPI: {hex(byte)}")
        return data

class USB_CAN_BridgeEmulator:
    def __init__(self):
        self.spi = SPIEmulator()

    def usb_can_bridge_init(self):
        print("USB-CAN Bridge Initialized.")
        self.spi.spi_init()

    def usb_can_bridge_run(self):
        while True:
            # Simulate USB to CAN data forwarding
            print("Waiting for data to forward from USB to CAN...")
            time.sleep(1)
            can_data = [0x11, 0x22, 0x33]  # Example CAN data
            print(f"Forwarding data: {can_data}")
            self.spi.spi_transfer(can_data)

if __name__ == "__main__":
    bridge = USB_CAN_BridgeEmulator()
    bridge.usb_can_bridge_init()
    bridge.usb_can_bridge_run()
