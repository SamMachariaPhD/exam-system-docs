# Getting Started with DEEPS

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10+ / macOS 10.14+ / Ubuntu 18.04+
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB available space
- **Python**: Python 3.8 or later (if running from source)

### Recommended Requirements
- **RAM**: 8GB or more for optimal performance
- **Storage**: SSD with 5GB+ available space
- **Network**: Internet connection for license verification

## Installation Options

### Option 1: Executable Download (Recommended)

1. Visit the [Releases Page](https://github.com/SamMachariaPhD/exam-system-releases/releases)
2. Download the latest version for your operating system:
   - Windows: `DEEPS-v2.x.x-windows.exe`
   - macOS: `DEEPS-v2.x.x-macos.dmg`
   - Linux: `DEEPS-v2.x.x-linux.tar.gz`
3. Run the installer and follow the setup wizard

### Option 2: Python Package

If you prefer to run from Python:

```bash
pip install deeps-exam-system
```

## Initial Setup

### First Launch

1. **Launch DEEPS** from your applications menu or desktop shortcut
2. **Authentication Setup**:
   - Enter your institutional license key
   - Configure user credentials
3. **Database Initialization**:
   - The system will create the local database automatically
   - Choose a secure location for your data files

### License Verification

DEEPS requires a valid institutional license:

1. Contact your institution's IT department for your license key
2. Enter the license key during first setup
3. The system will verify online connectivity for activation

## Next Steps

Once installed and configured:

1. **[First Run Guide](user-guide/first-run.md)** - Complete the initial configuration
2. **[Student Management](user-guide/student-management.md)** - Start adding students
3. **[Assessment Setup](user-guide/assessments.md)** - Create your first assessments

## Troubleshooting Installation

### Common Issues

**Installation fails on Windows**
- Ensure you have administrator privileges
- Temporarily disable antivirus during installation
- Check Windows version compatibility

**macOS security warnings**
- Right-click the application and select "Open"
- Go to System Preferences > Security & Privacy to allow the app

**Linux permission issues**
- Ensure the downloaded file has execute permissions:
  ```bash
  chmod +x DEEPS-v2.x.x-linux
  ```

For more detailed troubleshooting, see our [Technical Support Guide](technical/troubleshooting.md).

## Support

If you encounter issues during installation or setup:

1. Check our [Troubleshooting Guide](technical/troubleshooting.md)
2. Verify system requirements
3. Contact your institutional IT support

---

Ready to get started? Proceed to the [First Run Guide](user-guide/first-run.md)!