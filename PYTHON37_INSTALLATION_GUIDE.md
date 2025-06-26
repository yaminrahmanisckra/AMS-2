# Python 3.7.17 Installation Guide

## Quick Installation

### For Minimal Installation (Recommended for Shared Hosting):
```bash
pip3 install -r requirements_python37_minimal.txt
```

### For Complete Installation:
```bash
pip3 install -r requirements_python37.txt
```

## cPanel Setup
1. cPanel → Software → Setup Python App
2. Python Version: 3.7.17
3. Startup File: passenger_wsgi.py
4. Entry Point: application

## Troubleshooting
- Use --user flag if permission denied
- Install packages one by one if needed
- Check Python version: python3 --version

## All packages tested with Python 3.7.17
