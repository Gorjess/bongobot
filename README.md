# Created by 954860224@qq.com
# BongoCat Intelligent Idle Simulator 🐱

> ⚖️ Legal Notice & Disclaimer (Important)
>
> This tool is ONLY for office/presentation/testing keep-alive and automation. Do NOT use it for any game (including Steam/BongoCat) to AFK, farm points, auto-open cases, or bypass interactions. Such use may violate platform/game ToS and lead to bans or legal risks. Users assume all responsibility for misuse; authors/contributors are not liable.

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Windows](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows/)

**Language / 语言**: [🇺🇸 English](README.md) | [🇨🇳 中文](README.zh-CN.md)

</div>

An intelligent automation tool designed to prevent system idle state. Automatically simulates keyboard input and mouse clicks when user inactivity is detected, keeping the system active.

## ✨ Features

- 🎯 **Smart Detection**: Automatically detects user idle state
- ⌨️ **Keyboard Simulation**: Simulates random keyboard input to avoid system shortcuts
- 🖱️ **Image Recognition Clicking**: Smart clicking based on template matching
- 🔧 **Highly Configurable**: Support for customizing all parameters
- 📝 **Detailed Logging**: Complete operation logging system
- 🚀 **Lightweight**: Extremely low resource usage, runs silently in background

## 🚀 Quick Start

### System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows 10/11
- **Package Manager**: pip (Python package manager)

### Installation Methods

#### Method 1: One-Click Quick Setup (Recommended for Beginners)

```bash
# 1. Clone the project
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# 2. Run quick setup script
python quick_setup.py
```

#### Method 2: Manual Environment Setup

```bash
# 1. Clone the project
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# 2. Run environment setup script
python scripts/setup_environment.py

# 3. Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 4. Verify installation
bongobot --help
```

#### Method 3: Direct pip Installation (Available after release)

```bash
pip install bongobot
```

#### Method 4: Developer Mode

```bash
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# Choose complete development environment (includes testing tools)
python scripts/setup_environment.py
# Select "2. Complete development environment" when prompted
```

### Basic Usage

> Note: Running `bongobot` requires the package to be installed (which creates the console entry). If you are testing from source without installation, use `python -m bongobot` instead.

1. **Direct command line execution**:
   ```bash
   # Install into current venv first (editable recommended)
   # python -m pip install -e .
   bongobot
   ```

2. **Run as Python module**:
   ```bash
   python -m bongobot
   ```

3. **Prepare and add your own template image (optional)**:
   ```bash
   # Put your cropped button/region image into assets/
   # Prefer PNG, crop to the minimal recognizable area
   # Then edit config.yaml:
   clicker:
     enabled: true
     template_path: "assets/your_template.png"
     confidence: 0.8
   ```

4. **Run from source (for developers)**:
   ```bash
   # Create and activate venv
   python -m venv venv
   venv\Scripts\activate

   # Install dependencies
   python -m pip install -r requirements.txt

   # Editable install (creates bongobot command)
   python -m pip install -e .

   # Run
   bongobot            # or
   python -m bongobot
   ```

3. **Using custom configuration**:
   ```bash
   # Copy example configuration file
   cp examples/config.example.yaml config.yaml
   # Edit configuration file and run
   bongobot
   ```

## ⚙️ Configuration Guide

The program automatically searches for `config.yaml` configuration file. If not found, default configuration is used.

### Configuration File Example

```yaml
bot:
  # How long user must be idle before simulation starts (seconds)
  idle_threshold_seconds: 5.0
  # Set of keys used for simulation
  keys: ["a", "s", "d", "w", "q", "e", "space", "j", "k", "l"]

clicker:
  # Whether to enable template image clicker
  enabled: true
  # Target template image path
  template_path: "assets/test_btn.png"
  # Template matching confidence (0~1)
  confidence: 0.8
  # Cooldown time after successful click (seconds)
  wait_after_click_seconds: 8.0
  # Interval between consecutive searches (seconds)
  search_interval_seconds: 1.0

logging:
  # Log level: DEBUG/INFO/WARNING/ERROR
  level: "INFO"
  # Whether to write log files
  write_to_file: false
  # Log directory
  dir: "log"
```

### Main Configuration Options

| Configuration Item | Description | Recommended Value |
|-------------------|-------------|-------------------|
| `idle_threshold_seconds` | Idle detection threshold | 5-10 seconds |
| `keys` | List of simulation keys | Common letters avoiding system shortcuts |
| `template_path` | Click target image path | Relative or absolute path |
| `confidence` | Image matching confidence | 0.75-0.9 |
| `wait_after_click_seconds` | Cooldown after click | 5-15 seconds |

## 🎮 Use Cases

- **Remote Work**: Prevent computer from locking due to inactivity
- **Game AFK**: Automatically click specific buttons in games
- **Presentations**: Keep screen always on
- **System Testing**: Simulate user operations for stress testing

## 📁 Project Structure

```
bongobot/
├── bongobot/              # Main program package
│   ├── __init__.py        # Package initialization and version info
│   ├── __main__.py        # Module entry point (python -m bongobot)
│   ├── main.py            # Main program entry
│   ├── config_loader.py   # Configuration file loader
│   ├── logger_setup.py    # Logging system setup
│   ├── runner.py          # Main run loop logic
│   ├── automation.py      # Automation operations implementation
│   └── idle.py            # Idle state detection
├── assets/                # Program resource files
│   ├── README.md          # Resource file description
│   ├── test_btn.png       # Default template image
│   └── __test_btn.png     # Backup template image
├── examples/              # Examples and template files
│   └── config.example.yaml # Configuration file example
├── tests/                 # Unit tests
│   ├── __init__.py
│   └── test_config_loader.py
├── docs/                  # Project documentation
│   └── usage.md           # Detailed usage guide
├── scripts/               # Environment setup scripts
│   ├── setup_environment.py # Environment configuration script
│   └── check_environment.py # Environment check script
├── requirements.txt       # Basic dependencies list
├── requirements-dev.txt   # Development environment dependencies
├── setup.py              # Package installation script
├── pyproject.toml        # Modern Python project configuration
├── quick_setup.py        # One-click environment setup
├── gamebot.py            # Compatibility startup script
└── README.md             # Project documentation
```

## 🔧 Development Guide

### Environment Preparation

```bash
# Clone project
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
pip install -e .[dev]  # Install development dependencies
```

### Run Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black bongobot/
flake8 bongobot/
```

## 📋 System Requirements

- **Operating System**: Windows 10/11
- **Python Version**: 3.8 or higher
- **Dependencies**:
  - pyautogui >= 0.9.54
  - pydirectinput >= 1.0.4
  - pywin32 >= 311
  - opencv-python >= 4.8.0
  - numpy >= 1.24.0
  - Pillow >= 11.0.0
  - PyYAML >= 6.0.0

## ⚠️ Important Notes

1. **Administrator Privileges**: May require administrator privileges in some cases
2. **Antivirus Software**: May be flagged as malware, please add to whitelist
3. **Game Anti-cheat**: Do not use in games with anti-cheat systems
4. **Compliance**: Please comply with relevant laws and terms of use

## ⚖️ Legal and Ethical Use (Important)

Intended purpose of this project:
- Prevent system lock/sleep in non-competitive scenarios such as office, presentation, or automated testing;
- Serve as a keep-alive helper in demo/testing scripts.

Explicitly prohibited:
- Using this tool for any game (online or offline) to farm points/AFK/automate interactions;
- Violating Steam, game developers’ (e.g., BongoCat authors) or platform Terms of Service;
- Harming fair play or game economy/leaderboards.

Legal risk notice:
- Automation in games may violate platform/game agreements and cause bans, account penalties, or legal risks;
- The authors and contributors are not responsible for any misuse; users assume all risks of non-compliant use.

Recommended compliant description and usage boundary:
- "This tool is for office/presentation keep-alive and automated testing only, not for any gaming scenario."
- "Do not use it in applications with anti-cheat systems or real-time rewards/points."

## 🤝 Contributing

We welcome Issues and Pull Requests!

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version update details.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Author**: GorjessJin
- **Email**: 954860224@qq.com
- **Project URL**: https://github.com/Gorjess/bongobot

## 🙏 Acknowledgments

- Thanks to all contributors for their support
- Thanks to the open source community for excellent libraries
- Special thanks to the BongoCat project for inspiration

---

⭐ If this project helps you, please give it a star!
