#!/bin/bash

# Print a message indicating the start of the setup
echo "Setting up the project environment..."

# Ensure Python and pip are installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Please install Python3."
    exit 1
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 not found. Please install pip3."
    exit 1
fi

# Install Python packages from requirements.txt if it exists
if [ -f requirements.txt ]; then
    echo "Installing Python packages..."
    pip3 install -r requirements.txt
else
    echo "requirements.txt not found. Skipping Python package installation."
fi

# Check for any required system packages or tools
echo "Checking for required system packages..."
# Example: Check for `make` and `gcc`
for pkg in make gcc; do
    if ! dpkg -s $pkg &> /dev/null; then
        echo "$pkg not found. Installing..."
        sudo apt-get update
        sudo apt-get install -y $pkg
    else
        echo "$pkg is already installed."
    fi
done

# Print a success message
echo "Environment setup complete."

# Optionally, you might want to set up environment variables
# For example:
# export PROJECT_PATH=~/rrn/USB_CAN/USB_CAN_Project

# If you have any additional setup tasks, add them here
# For example, setting up paths or directories
# mkdir -p ~/usb_can_project_data

# Print a message indicating the end of the setup
echo "All setup tasks completed."
