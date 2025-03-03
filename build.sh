#!/bin/bash
# Install Python (if not already available)
if ! command -v python3 &>/dev/null; then
    echo "Python not found, installing..."
    apt-get update && apt-get install -y python3 python3-pip
fi

# Install dependencies
pip3 install -r requirements.txt
