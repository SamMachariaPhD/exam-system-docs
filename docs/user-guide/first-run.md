# First Run Configuration

## Initial Database Setup

When you first launch DEEPS, you'll need to complete the initial configuration:

### 1. Welcome Screen
- Review the welcome message and system information
- Click "Initialize Database" to set up the local database

### 2. Authentication Configuration
- **License Key**: Enter your institutional license key
- **User Profile**: Set up your admin user account
- **Institution Details**: Configure your institution information

### 3. Database Location
- Choose a secure location for your database files
- Recommended: Use a backed-up directory
- Ensure adequate disk space (minimum 1GB)

## Initial Data Import

### Setting Up Curriculum
1. Navigate to **Tools > Departmental Rules Editor**
2. Configure your department's assessment structure
3. Import curriculum unit definitions
4. Set grading scales and pass requirements

### Loading Student Data
1. Go to **Student Management** tab
2. Add students individually or import from spreadsheet
3. Verify registration numbers and personal details

## System Verification

### Test Core Functions
1. **Create a test student** to verify database connectivity
2. **Add a sample assessment** to test calculation engine
3. **Generate a test report** to verify PDF output

### Security Check
- Verify that data files are stored securely
- Confirm authentication is working
- Test backup and restore functions

## Configuration Best Practices

### Data Security
- Store database files in a secure, backed-up location
- Use strong passwords for user accounts
- Enable automatic database backups

### Performance Optimization
- Allocate sufficient RAM for large datasets
- Keep the application updated
- Regular database maintenance

## Next Steps

After completing first-run setup:

1. **[Student Management](student-management.md)** - Start managing your student database
2. **[Assessment Creation](assessments.md)** - Begin creating assessments
3. **[Report Generation](reports.md)** - Generate your first reports

## Troubleshooting First Run

### Database Initialization Fails
- Check file permissions in the chosen directory
- Ensure adequate disk space
- Verify Python/system dependencies

### License Activation Issues
- Verify internet connectivity
- Check license key format
- Contact IT support for license verification

### Performance Issues
- Close other memory-intensive applications
- Increase system RAM if possible
- Choose SSD storage for database location

For additional support, see our [Troubleshooting Guide](../technical/troubleshooting.md).

---

Ready to start? Continue to [Student Management](student-management.md)!