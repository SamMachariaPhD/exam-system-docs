# Installation Guide

Get DEEPS up and running on your system in minutes with our comprehensive installation guide.

## :material-download: Download DEEPS

### Current Version: v2.1

DEEPS is available for all major operating systems. Choose your platform below:

=== "Windows"

    **System Requirements:**
    - Windows 10 or later (64-bit)
    - 4 GB RAM (8 GB recommended)
    - 2 GB available disk space
    - Administrator privileges for installation

    **Download Options:**

    - **Installer (.msi)** - Recommended for most users
      [:material-download: Download Windows Installer](https://github.com/SamMachariaPhD/exam-system-releases/releases/latest){ .md-button .md-button--primary }

    - **Portable (.zip)** - No installation required
      [:material-download: Download Portable Version](https://github.com/SamMachariaPhD/exam-system-releases/releases/latest){ .md-button }

=== "macOS"

    **System Requirements:**
    - macOS 10.15 (Catalina) or later
    - Intel or Apple Silicon processor
    - 4 GB RAM (8 GB recommended)
    - 2 GB available disk space

    **Download:**

    [:material-download: Download for macOS (.dmg)](https://github.com/SamMachariaPhD/exam-system-releases/releases/latest){ .md-button .md-button--primary }

=== "Linux"

    **System Requirements:**
    - Ubuntu 18.04+ / CentOS 7+ / Fedora 30+
    - 4 GB RAM (8 GB recommended)
    - 2 GB available disk space
    - Python 3.8+ (usually pre-installed)

    **Download Options:**

    - **AppImage** - Universal Linux package
      [:material-download: Download AppImage](https://github.com/SamMachariaPhD/exam-system-releases/releases/latest){ .md-button .md-button--primary }

    - **Debian Package (.deb)**
      [:material-download: Download .deb Package](https://github.com/SamMachariaPhD/exam-system-releases/releases/latest){ .md-button }

---

## :material-cog: Installation Steps

### Windows Installation

1. **Download** the Windows installer (.msi file)
2. **Right-click** the installer and select **"Run as administrator"**
3. **Follow the setup wizard:**
   - Accept the license agreement
   - Choose installation location (default recommended)
   - Select components to install
4. **Complete installation** and restart if prompted
5. **Launch DEEPS** from the Start menu or desktop shortcut

!!! tip "Installation Tips"
    - Temporarily disable antivirus during installation if prompted
    - Choose "Install for all users" for multi-user environments
    - Keep the default installation path for automatic updates

### macOS Installation

1. **Download** the macOS disk image (.dmg file)
2. **Open** the downloaded .dmg file
3. **Drag DEEPS** to the Applications folder
4. **Launch DEEPS** from Applications
5. **Allow** the app when macOS security prompts appear

!!! warning "Security Notice"
    On first launch, you may see "DEEPS cannot be opened because it is from an unidentified developer":

    - Right-click DEEPS in Applications
    - Select "Open" from the context menu
    - Click "Open" in the security dialog

### Linux Installation

#### Option 1: AppImage (Recommended)
1. **Download** the AppImage file
2. **Make it executable:** `chmod +x DEEPS-v2.1-x86_64.AppImage`
3. **Run:** `./DEEPS-v2.1-x86_64.AppImage`

#### Option 2: Debian Package
1. **Download** the .deb package
2. **Install:** `sudo dpkg -i deeps_2.1_amd64.deb`
3. **Resolve dependencies:** `sudo apt-get install -f`
4. **Launch:** `deeps` or find in applications menu

---

## :material-check-circle: Post-Installation Setup

### First Launch

When you start DEEPS for the first time:

1. **License Verification** - DEEPS will attempt to verify your educational license
2. **Institution Setup** - Configure your institution's details
3. **Database Initialization** - Create the local database structure
4. **User Account** - Set up the first administrator account

### Verify Installation

Test your DEEPS installation:

- [ ] Application launches without errors
- [ ] License verification completes successfully
- [ ] You can access the main interface
- [ ] Sample data can be imported (optional test)

---

## :material-network: Network Configuration

### License Verification Requirements

DEEPS requires internet access for initial license verification:

- **Outbound HTTPS** (port 443) to GitHub
- **No inbound ports** required
- **Proxy support** available for corporate networks

### Firewall Settings

If using institutional firewalls, allow access to:

```
https://raw.githubusercontent.com/SamMachariaPhD/exam-system-auth/main/licenses.json
```

---

## :material-database: Data Directory Setup

### Default Locations

DEEPS stores data in these default locations:

=== "Windows"
    ```
    C:\Users\[Username]\Documents\DEEPS\
    ├── databases/          # Student data (local only)
    ├── exports/           # Generated reports
    ├── imports/           # Excel file workspace
    └── backups/           # Automatic backups
    ```

=== "macOS"
    ```
    ~/Documents/DEEPS/
    ├── databases/          # Student data (local only)
    ├── exports/           # Generated reports
    ├── imports/           # Excel file workspace
    └── backups/           # Automatic backups
    ```

=== "Linux"
    ```
    ~/Documents/DEEPS/
    ├── databases/          # Student data (local only)
    ├── exports/           # Generated reports
    ├── imports/           # Excel file workspace
    └── backups/           # Automatic backups
    ```

### Custom Data Location

For institutional deployments, you can specify custom data directories:

1. **Settings** → **Preferences** → **Data Storage**
2. **Choose** network drive or shared storage location
3. **Ensure** all users have read/write access
4. **Configure** automatic backups to secure location

---

## :material-account-multiple: Multi-User Setup

### Shared Installation

For multiple users accessing the same data:

1. **Install DEEPS** on each user's computer
2. **Configure** shared network storage for databases
3. **Set up** user accounts with appropriate permissions
4. **Test** concurrent access (read-only for most users)

### Access Control

Configure user permissions:

- **Administrator** - Full access to all features
- **Academic Staff** - Process exams, generate reports
- **Registrar** - Access student records, create transcripts
- **Read-Only** - View reports, export data

---

## :material-tools: Troubleshooting Installation

### Common Issues

**Installation Fails on Windows:**
- Run installer as Administrator
- Temporarily disable antivirus software
- Check available disk space (minimum 2 GB)

**macOS Security Blocks App:**
- Right-click app, select "Open"
- Check System Preferences → Security & Privacy
- Allow app from "unidentified developer"

**Linux Dependencies Missing:**
- Update package manager: `sudo apt update`
- Install Python 3.8+: `sudo apt install python3`
- Install required libraries: `sudo apt install python3-tk`

**License Verification Fails:**
- Check internet connectivity
- Verify institutional firewall settings
- Contact support for offline license activation

### Getting Help

If you encounter installation issues:

1. **Check** the [Troubleshooting Guide](../support/troubleshooting.md)
2. **Review** [Frequently Asked Questions](../support/faq.md)
3. **Contact** technical support: deeps-support@dkut.ac.ke

---

## :material-arrow-right: Next Steps

Once DEEPS is installed successfully:

1. **[System Requirements](requirements.md)** - Verify your system is optimized
2. **[First Setup](setup.md)** - Configure DEEPS for your institution
3. **[User Guide](../user-guide/overview.md)** - Learn to use DEEPS effectively

---

*Installation complete? Proceed to [System Requirements](requirements.md) to optimize your setup.*