#!/bin/bash

# Function to check if a command exists
command_exists () {
  type "$1" &> /dev/null ;
}

# Determine Linux Distribution
distro=""
if [ -f /etc/os-release ]; then
    . /etc/os-release
    distro=$ID
elif [ "$(uname -o)" == "Android" ]; then
    distro="termux"
fi

# 1) Check and install Python3 and pip
if ! command_exists python3; then
    echo "Installing Python3..."
    case $distro in
        "termux") pkg install python ;;
        "arch") sudo pacman -S python ;;
        "fedora") sudo dnf install python3 ;;
        "opensuse") sudo zypper install python3 ;;
        "debian"|"ubuntu"|"kali"|"parrot") sudo apt update && sudo apt install -y python3 ;;
        *) echo "Sorry, this distro is not supported" ;;
    esac
fi

# Install python3-venv if needed
if [ "$distro" == "debian" ] || [ "$distro" == "ubuntu" ] || [ "$distro" == "kali" ] || [ "$distro" == "parrot" ]; then
    sudo apt update && sudo apt install -y python3-venv
fi

# 2) Check and install Git
if ! command_exists git; then
    echo "Installing Git..."
    case $distro in
        "termux") pkg install git ;;
        "arch") sudo pacman -S git ;;
        "fedora") sudo dnf install git ;;
        "opensuse") sudo zypper install git ;;
        "debian"|"ubuntu"|"kali"|"parrot") sudo apt update && sudo apt install -y git ;;
        *) echo "Sorry, this distro is not supported" ;;
    esac
fi

# 3) Termux specific installation
if [ "$distro" == "termux" ]; then
    pkg install libjpeg-turbo
fi

# 4) Clone the repository
git clone https://github.com/EchterAlsFake/Osintgram2

# 5) cd into it and create a virtual environment
cd Osintgram2 || { echo "Failed to change directory to Osintgram2"; exit 1; }
python3 -m venv osintgram_venv

# Activate virtual environment
source osintgram_venv/bin/activate

# Install pip dependencies in the virtual environment
pip install -r requirements.txt

# 6) Run pyinstaller
pyinstaller -F Osintgram.py

# 7) chmod +x to the Osintgram file
cd dist || { echo "Failed to change directory to dist"; exit 1; }
chmod +x Osintgram

echo "Done"
