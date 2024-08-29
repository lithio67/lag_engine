#!/bin/bash

# Install Homebrew if not already installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL 
https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Python 3.12.5
echo "Installing Python 3.12.5..."
brew install python@3.12

# Link the installed version
brew link --force --overwrite python@3.12

# Verify the installation
python3.12 --version
