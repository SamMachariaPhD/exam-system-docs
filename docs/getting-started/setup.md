# First Setup Guide

Configure DEEPS for your institution with this comprehensive setup guide.

## :material-rocket: Initial Configuration

### Launch DEEPS for the First Time

When you first start DEEPS, you'll be guided through essential setup steps:

1. **License Verification** - Confirm your educational institution license
2. **Institution Profile** - Configure your university/college details
3. **Database Setup** - Initialize the local student database
4. **Administrator Account** - Create your first user account

---

## :material-school: Institution Configuration

### Basic Information Setup

Configure your institution's basic details:

=== "University Settings"
    ```
    Institution Name: [Your University Name]
    Department: [Your Department/Faculty]
    Academic Year Format: 2023/2024 or 2023-2024
    Grading System: Letter grades (A, B, C...) or GPA scale
    ```

=== "Contact Information"
    ```
    Registrar Office: [Contact Details]
    Academic Office: [Contact Details]
    IT Support: [Contact Details]
    Email Domain: @youruniversity.edu
    ```

### Academic Structure

Define your institution's academic organization:

**Year Structure:**
- Traditional 4-year undergraduate programs
- Graduate programs (Masters/PhD)
- Professional programs with different durations

**Semester/Term System:**
- Semester-based (Fall/Spring)
- Quarter-based (Fall/Winter/Spring/Summer)
- Trimester system
- Custom academic calendar

---

## :material-database: Database Initialization

### Local Database Setup

DEEPS creates a secure local SQLite database to store student records:

```
📁 DEEPS Data Directory
├── 📁 databases/
│   ├── students.db          # Main student records
│   ├── courses.db           # Course definitions
│   └── academic_history.db  # Historical data
├── 📁 exports/              # Generated reports
├── 📁 imports/              # Excel file processing
└── 📁 backups/              # Automatic backups
```

### Database Security

DEEPS implements multiple security layers:

- **Local-only storage** - No data transmitted externally
- **Encrypted connections** - Secure database access
- **User authentication** - Role-based access control
- **Audit logging** - Track all data changes

---

## :material-account: User Account Management

### Administrator Account Creation

Set up your first administrator account:

1. **Username**: Choose a memorable administrator username
2. **Password**: Create a strong password (minimum 8 characters)
3. **Email**: Institutional email for notifications
4. **Recovery**: Set up account recovery options

### User Roles and Permissions

Configure different access levels for your team:

=== "Administrator"
    **Full System Access:**
    - User account management
    - System configuration changes
    - Database backup/restore
    - All reporting features

=== "Academic Staff"
    **Processing and Reports:**
    - Import exam results from Excel
    - Generate student reports
    - Process graduation requirements
    - View academic history

=== "Registrar Staff"
    **Student Records:**
    - Access complete student records
    - Generate official transcripts
    - Process enrollment changes
    - Create senate documents

=== "Read-Only Users"
    **View Access Only:**
    - View processed reports
    - Access student summaries
    - Export basic data
    - No editing capabilities

---

## :material-file-import: Data Import Configuration

### Excel Template Setup

Configure DEEPS to work with your existing Excel formats:

**Standard Column Mapping:**
- Student ID/Registration Number
- Student Name
- Course Code
- Course Name
- Marks/Grades
- Academic Year/Semester

**Custom Field Configuration:**
- Additional student information fields
- Institution-specific course codes
- Special grading categories
- Academic status indicators

### Import Validation Rules

Set up automatic validation for imported data:

- **Student ID format validation**
- **Grade range checking**
- **Course prerequisite verification**
- **Duplicate detection**
- **Missing data alerts**

---

## :material-cog: System Preferences

### Display and Interface

Customize the DEEPS interface for your workflow:

**Theme Selection:**
- Light theme (default)
- Dark theme for low-light environments
- High contrast for accessibility

**Layout Preferences:**
- Default report formats
- Column display options
- Page size for large datasets

### Backup Configuration

Set up automatic data protection:

**Automatic Backups:**
- Daily incremental backups
- Weekly full system backup
- Retention policy (30 days default)

**Backup Location:**
- Local backup folder
- Network drive for institutional backup
- External storage integration

---

## :material-test-tube: Verify Your Setup

### Test System Functionality

Before processing real data, test your DEEPS installation:

1. **Import Sample Data**
   - Use provided sample Excel files
   - Verify column mapping works correctly
   - Check data validation rules

2. **Generate Test Reports**
   - Create sample transcript
   - Generate pass/supplementary lists
   - Test PDF export functionality

3. **User Access Testing**
   - Create additional test user accounts
   - Verify role-based permissions
   - Test password reset functionality

### Sample Data Download

DEEPS includes sample datasets for testing:

- Sample student records (anonymized)
- Example course structures
- Template Excel files for lecturers
- Test report outputs

---

## :material-network-outline: Network Setup (Multi-User)

### Shared Database Configuration

For multi-user environments with shared access:

1. **Network Storage Setup**
   - Configure shared network drive
   - Set proper read/write permissions
   - Test network connectivity stability

2. **Concurrent Access Management**
   - Limit simultaneous editors
   - Enable automatic conflict resolution
   - Configure user session management

3. **Network Security**
   - Use VPN for remote access
   - Enable network encryption
   - Configure firewall rules

---

## :material-check-all: Setup Completion Checklist

Verify your DEEPS setup is complete:

**Basic Configuration:**
- [ ] License verification completed
- [ ] Institution profile configured
- [ ] Administrator account created
- [ ] Database initialized successfully

**Data Management:**
- [ ] Sample data import tested
- [ ] Column mapping configured
- [ ] Validation rules active
- [ ] Backup system enabled

**User Management:**
- [ ] User roles defined
- [ ] Staff accounts created
- [ ] Permissions tested
- [ ] Password policies set

**System Testing:**
- [ ] Sample reports generated
- [ ] Export functionality verified
- [ ] Performance acceptable
- [ ] All features accessible

---

## :material-help-circle: Next Steps

Your DEEPS system is now ready for production use:

1. **[Learn the User Interface](../user-guide/overview.md)** - Get familiar with DEEPS features
2. **[Import Your First Data](../user-guide/processing.md)** - Process real exam results
3. **[Generate Reports](../user-guide/reports.md)** - Create institutional documents

---

*Setup complete? Start using DEEPS with the [User Guide](../user-guide/overview.md).*