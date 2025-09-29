# System Requirements

Ensure your system meets these requirements for optimal DEEPS performance.

## :material-monitor: Minimum System Requirements

### Hardware Requirements

=== "Recommended (Best Performance)"
    - **CPU**: Quad-core processor (Intel i5/AMD Ryzen 5 or better)
    - **RAM**: 8 GB or more
    - **Storage**: 5 GB available space (SSD recommended)
    - **Display**: 1920×1080 resolution or higher

=== "Minimum (Basic Operation)"
    - **CPU**: Dual-core processor
    - **RAM**: 4 GB
    - **Storage**: 2 GB available space
    - **Display**: 1366×768 resolution

### Operating System Support

=== "Windows"
    - Windows 10 (64-bit) or later
    - Windows 11 supported
    - .NET Framework 4.8 or later

=== "macOS"
    - macOS 10.15 (Catalina) or later
    - Intel and Apple Silicon processors supported
    - macOS Monterey/Ventura recommended

=== "Linux"
    - Ubuntu 18.04 LTS or later
    - CentOS 7+ / RHEL 7+
    - Fedora 30 or later
    - Other distributions with Python 3.8+

---

## :material-network: Network Requirements

### Internet Connectivity
- **Initial Setup**: Required for license verification
- **Daily Operation**: Offline capable once activated
- **Updates**: Periodic connection for version updates

### Firewall Configuration
Allow outbound HTTPS connections to:
```
https://raw.githubusercontent.com/SamMachariaPhD/exam-system-auth/main/licenses.json
```

---

## :material-application: Software Dependencies

### Python Environment
- **Python 3.8** or later (included in installation packages)
- **SQLite 3.31+** for database operations
- **Qt 6.2+** for user interface (bundled)

### Document Generation
- **LibreOffice** (optional) - For advanced document formatting
- **PDF viewers** - For report verification

---

## :material-harddisk: Storage Considerations

### Data Storage Estimates

| Institution Size | Student Records | Storage Needed |
|------------------|----------------|----------------|
| Small Department | < 1,000 students | 500 MB |
| Medium Faculty | 1,000 - 5,000 students | 2 GB |
| Large University | 5,000+ students | 10 GB+ |

### Backup Requirements
- **Automatic backups**: 2x data size for rotation
- **Archive storage**: Network drive or external media
- **Recovery space**: 1GB for temporary operations

---

## :material-security: Security Requirements

### User Permissions
- **Windows**: Standard user account (Administrator for installation)
- **macOS**: Standard user (sudo for installation)
- **Linux**: Standard user with sudo access for packages

### Antivirus Compatibility
DEEPS is compatible with all major antivirus software. If installation issues occur:
1. Add DEEPS installation folder to antivirus exceptions
2. Temporarily disable real-time scanning during installation
3. Contact support if persistent issues occur

---

## :material-speedometer: Performance Optimization

### Recommended Optimizations

**For Large Datasets (5,000+ records):**
- Use SSD storage for database files
- Allocate 8GB+ RAM
- Close unnecessary applications during processing

**Network Storage Setup:**
- Use wired Ethernet connection
- Ensure consistent network access to shared drives
- Configure automatic reconnection for mapped drives

**Multi-User Environments:**
- Install on local drives, not network shares
- Use shared network storage only for databases
- Limit concurrent users to prevent conflicts

---

## :material-check-circle: Pre-Installation Checklist

Before installing DEEPS, verify:

- [ ] Operating system meets minimum requirements
- [ ] Sufficient disk space available
- [ ] Administrative privileges for installation
- [ ] Internet connection for license activation
- [ ] Antivirus software configured appropriately
- [ ] Backup strategy planned for data protection

---

## :material-alert: Common Issues

### Performance Problems
**Slow startup or processing:**
- Check available RAM and close other applications
- Verify database files are on fast storage (SSD preferred)
- Ensure antivirus isn't scanning database files repeatedly

**Display Issues:**
- Update graphics drivers
- Check display scaling settings (Windows)
- Verify resolution meets minimum requirements

### Installation Problems
**Permission denied errors:**
- Run installer as Administrator (Windows) or with sudo (Linux)
- Check user account has write access to installation directory

**Missing dependencies:**
- Install latest system updates
- Verify Python 3.8+ is available
- Contact support for distribution-specific requirements

---

*Ready to install? Continue to the [Installation Guide](installation.md).*