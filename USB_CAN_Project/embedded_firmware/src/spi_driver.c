#include "spi_driver.h"
#include <stdio.h>

void spi_init(void) {
    // Initialize SPI peripheral
    printf("SPI Initialized\n");
}

void spi_transfer(uint8_t *data, uint8_t length) {
    // Transfer data over SPI
    for (uint8_t i = 0; i < length; i++) {
        // Example transfer function (replace with actual hardware SPI logic)
        printf("Sending: 0x%02X\n", data[i]);
    }
}
