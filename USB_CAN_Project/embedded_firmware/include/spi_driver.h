#ifndef SPI_DRIVER_H
#define SPI_DRIVER_H

#include <stdint.h>

void spi_init(void);
void spi_transfer(uint8_t *data, uint8_t length);

#endif // SPI_DRIVER_H
