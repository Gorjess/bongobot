# Created by 954860224@qq.com
# BongoCat Usage Guide

> ⚖️ Legal Notice & Disclaimer (Important)
>
> This tool is for non-competitive scenarios (office/presentation/testing) as a keep-alive/automation helper. It must not be used for any gaming automation (AFK/point farming/auto-opening cases). Such use may violate platform/game ToS and cause bans or legal risks. Users bear full responsibility for misuse.

## Quick Start

### 1. Installation

```bash
# Option 1: From PyPI (after release)
pip install bongobot

# Option 2: From source (dev/local testing)
python -m pip install -e .
```

### 2. Basic Execution

```bash
# Run with default configuration (requires package installed into current venv)
bongobot

# Or run as module (works without console script installed)
python -m bongobot
```

### 3. Custom Configuration

```bash
# Copy example configuration
cp examples/config.example.yaml config.yaml

# Edit configuration file
notepad config.yaml  # Windows
# nano config.yaml   # Linux/Mac

# Prepare your own template image (optional)
# 1) Put your cropped PNG into assets/, e.g. my_btn.png
# 2) Edit config.yaml:
# clicker:
#   enabled: true
#   template_path: "assets/my_btn.png"
#   confidence: 0.8

# Run (works even without console script installed)
python -m bongobot
```

## Configuration Details

### Basic Configuration Structure

```yaml
bot:
  idle_threshold_seconds: 5.0
  keys: ["a", "s", "d", "w", "q", "e", "space", "j", "k", "l"]

clicker:
  enabled: true
  template_path: "assets/test_btn.png"
  confidence: 0.8
  wait_after_click_seconds: 8.0
  search_interval_seconds: 1.0

logging:
  level: "INFO"
  write_to_file: false
  dir: "log"
```

### Configuration Options Explained

#### bot section

- **idle_threshold_seconds**: Idle detection threshold (seconds)
  - How long user must be inactive before simulation starts
  - Recommended: 5-10 seconds
  - Too small = frequent triggering, too large = delayed response

- **keys**: List of simulation keys
  - Program randomly selects from these keys for simulation
  - Recommend using common letters that won't trigger system shortcuts
  - Supports special keys: space, enter, tab, etc.

#### clicker section

- **enabled**: Whether to enable image clicking feature
  - true: Enable template matching clicks
  - false: Use keyboard simulation only

- **template_path**: Template image path
  - Relative or absolute path
  - Supported formats: PNG, JPG, JPEG
  - Recommend PNG format for matching accuracy
  - Default resources stored in `assets/` directory

- **confidence**: Template matching confidence
  - Range: 0.0-1.0
  - 0.8 means 80% similarity
  - Too low = false clicks, too high = no matches

- **wait_after_click_seconds**: Cooldown time after click
  - Wait time after successful click
  - Prevents frequent clicking
  - Recommended: 5-15 seconds

- **search_interval_seconds**: Search interval
  - Time between template searches
  - Prevents high CPU usage
  - Recommended: 0.5-2 seconds

#### logging section

- **level**: Log level
  - DEBUG: Detailed debug information
  - INFO: General information (recommended)
  - WARNING: Warning messages
  - ERROR: Error messages only

- **write_to_file**: Whether to write log files
  - true: Write to file (for debugging)
  - false: Console output only (recommended)

- **dir**: Log file directory
  - Only effective when write_to_file=true

## Use Cases

### 1. Remote Work Anti-Lock

```yaml
bot:
  idle_threshold_seconds: 30.0  # Activate after 30s idle
  keys: ["shift"]               # Use only Shift key, no text input

clicker:
  enabled: false                # Disable clicking

logging:
  level: "WARNING"              # Minimal logging
```

### 2. Game AFK Clicking

```yaml
bot:
  idle_threshold_seconds: 5.0   # Quick response
  keys: []                      # No keyboard simulation

clicker:
  enabled: true
  template_path: "game_button.png"
  confidence: 0.85              # Higher accuracy
  wait_after_click_seconds: 10.0
  search_interval_seconds: 0.5  # Fast searching

logging:
  level: "INFO"
  write_to_file: true           # Record click logs
```

### 3. Presentation Screen Keep-Alive

```yaml
bot:
  idle_threshold_seconds: 60.0  # 1 minute idle detection
  keys: ["f15"]                 # Use function key, won't affect presentation

clicker:
  enabled: false

logging:
  level: "ERROR"                # Minimal log output
```

## Advanced Features

### Template Image Creation

1. **Screenshot Tool**: Use screenshot tool to save target button
2. **Image Editing**: Crop to minimum recognition area
3. **Format Conversion**: Save as PNG format
4. **Test Verification**: Adjust confidence value for testing

### Multi-Configuration Management

```bash
# Create configuration files for different scenarios
config-office.yaml      # Office scenario
config-game.yaml        # Game scenario
config-presentation.yaml # Presentation scenario

# Use environment variable to specify configuration
set BONGOBOT_CONFIG=config-game.yaml
bongobot
```

### Debug Mode

```bash
# Enable detailed logging
# Set in config.yaml
logging:
  level: "DEBUG"
  write_to_file: true

# Run program to view detailed logs
bongobot
```

## Common Issues

### Q: Program not responding?
A: Check idle time setting, ensure it exceeds idle_threshold_seconds

### Q: Clicking feature not working?
A: 
1. Check template image path is correct
2. Adjust confidence value
3. Ensure target is in visible screen area

### Q: Blocked by antivirus software?
A: Add program directory to antivirus whitelist

### Q: Insufficient permissions?
A: Run program as administrator

### Q: How to stop the program?
A: Press Ctrl+C or close command line window

## Security Considerations

1. **Compliance**: Follow company and legal regulations
2. **Game Rules**: Be aware of game anti-cheat policies
3. **Privacy Protection**: Don't run during sensitive operations
4. **Resource Monitoring**: Monitor CPU and memory usage

## Technical Support

- **Project URL**: https://github.com/Gorjess/bongobot
- **Issue Reports**: https://github.com/Gorjess/bongobot/issues
- **Email**: 954860224@qq.com

## Legal Notice & Disclaimer

This tool is intended for non-competitive scenarios (office/presentation/testing) as a keep-alive/automation helper. Using it for gaming automation (AFK/point farming) is prohibited and may violate platform or game ToS, leading to bans or legal risks. Users bear all responsibility for misuse.
