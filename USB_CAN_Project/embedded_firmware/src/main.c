#include "spi_driver.h"
#include "usb_can_bridge.h"

int main() {
    uint8_t spi_data[] = {0x01, 0x02, 0x03};

    // Initialize SPI
    spi_init();
    spi_transfer(spi_data, 3);
    
    // Initialize and run USB-CAN bridge
    usb_can_bridge_init();
    usb_can_bridge_run();

    return 0;
}
