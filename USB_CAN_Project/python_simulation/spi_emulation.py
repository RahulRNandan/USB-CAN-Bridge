import spidev
import time

def spi_communication():
    spi = spidev.SpiDev()
    spi.open(0, 0)  # Bus 0, Chip Select 0
    spi.max_speed_hz = 50000
    
    try:
        while True:
            spi.xfer([0x01, 0x02, 0x03])
            print("Sent SPI data")
            time.sleep(1)
    except KeyboardInterrupt:
        spi.close()

if __name__ == "__main__":
    spi_communication()
