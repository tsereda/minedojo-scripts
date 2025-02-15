# MineDojo Setup Guide

This guide provides step-by-step instructions for setting up MineDojo with GUI visibility in a Docker container.

## Prerequisites

- Docker installed
- NVIDIA GPU with updated drivers
- VcXsrv (Windows X Server) installed
- Git

## Setup Steps

### 1. Start VcXsrv
- Launch XLaunch
- Select "Multiple windows"
- Set Display number to 0
- Select "Start no client"
- Check "Disable access control"
- Save configuration and start

### 2. Pull and Run Docker Container
```bash
# Pull the MineDojo image
docker pull minedojo/minedojo:latest

# Run container with GPU support
docker run --gpus all -it -d \
  -p 8080:8080 \
  -e DISPLAY=host.docker.internal:0 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  minedojo/minedojo:latest tail -f /dev/null

# Get container ID and connect
docker ps
docker exec -it <container_id> /bin/bash
```

### 3. Inside Container Setup
```bash
# Clone setup scripts
git clone https://github.com/tsereda/minedojo-scripts.git
cd minedojo-scripts

# Make script executable and run setup
chmod +x fix-minedojo.sh
sudo ./fix-minedojo.sh

# Verify Xvfb
ps aux | grep Xvfb
export DISPLAY=:0
xdpyinfo | grep dimensions  # Should show display info

# Optional: Test display forwarding
apt-get update
apt-get install x11-apps
xeyes &  # Should show up on your host machine
```

### 4. Run Validation
```bash
python validate_script.py
```

## Troubleshooting

### Display Issues
- Verify Xvfb is running: `ps aux | grep Xvfb`
- Check display connection: `xdpyinfo | grep dimensions`
- For visibility on host: `export DISPLAY=host.docker.internal:0`
- For headless operation: `export DISPLAY=:0`

### Common Problems
1. **No display**: Make sure VcXsrv is running with access control disabled
2. **GPU not found**: Verify nvidia-smi works inside container
3. **Java issues**: Check Java installation with `java -version`
4. **Python dependencies**: Use `pip list` to verify MineDojo installation

## Additional Notes

  - `:0` (1920x1200x24) 

- For GUI visibility, ensure Windows Firewall allows VcXsrv connections
- Container must be launched with GPU support for MineDojo to function properly

