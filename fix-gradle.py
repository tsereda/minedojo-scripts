#!/bin/bash

# Script to fix MixinGradle dependency issues in MineDojo Docker installation

# Set up error handling
set -e

# Create necessary directories
MIXIN_DIR="/opt/conda/lib/python3.9/site-packages/minedojo/sim/Malmo/Minecraft/MixinGradle-dcfaf61/MixinGradle/dcfaf61"
mkdir -p "$MIXIN_DIR"

# Download the MixinGradle jar file
echo "Downloading MixinGradle..."
wget https://github.com/verityw/MixinGradle-dcfaf61/raw/main/MixinGradle/dcfaf61/MixinGradle-dcfaf61.jar -P "$MIXIN_DIR"

# Path to the build.gradle file
GRADLE_FILE="/opt/conda/lib/python3.9/site-packages/minedojo/sim/Malmo/Minecraft/build.gradle"

# Backup the original build.gradle
cp "$GRADLE_FILE" "${GRADLE_FILE}.backup"

cp "build.gradle" "$GRADLE_FILE"

echo "MixinGradle dependency has been fixed!"
echo "Original build.gradle has been backed up to ${GRADLE_FILE}.backup"
echo "You can now try running the validation script again."
