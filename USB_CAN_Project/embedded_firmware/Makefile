# Compiler and linker
CC = gcc
CFLAGS = -Wall -Iinclude -g
LDFLAGS = 

# Directories
SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin

# Source files
SRC = $(wildcard $(SRC_DIR)/*.c)
OBJ = $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(SRC))

# Output binary
TARGET = usb_can_bridge.elf

# Targets and rules
all: $(TARGET)

$(TARGET): $(OBJ)
	@mkdir -p $(BIN_DIR)
	$(CC) $(LDFLAGS) -o $(BIN_DIR)/$(TARGET) $(OBJ)
	cp $(BIN_DIR)/$(TARGET) .

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR) $(TARGET)

run: $(TARGET)
	qemu-system-arm -M versatilepb -nographic -s -S -kernel $(TARGET)

debug: $(TARGET)
	gdb-multiarch $(TARGET)

.PHONY: all clean run debug
