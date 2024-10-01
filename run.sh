xhost +SI:localuser:root

sudo /bin/bash -c 'source $(pwd)/.venv/bin/activate && python3 $(pwd)/main.py'