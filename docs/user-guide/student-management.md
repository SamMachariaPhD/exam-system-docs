# Student Management

## Adding Students

### Individual Student Entry
1. Navigate to **Student Management** tab
2. Fill in the student details form:
   - **Registration Number**: Unique student identifier
   - **Surname**: Student's family name
   - **Other Names**: Given names
   - **Start Year**: Academic year of enrollment
   - **Expected Graduation**: Projected graduation year
3. Click **Add Student** to save

### Bulk Student Import
For importing multiple students:
1. Prepare a CSV file with columns: `reg_no`, `surname`, `other_names`, `start_year`, `grad_year`
2. Use **File > Import Students** (when available)
3. Map columns to appropriate fields
4. Review and confirm the import

## Managing Student Records

### Viewing Students
- The student list displays all registered students
- Use the search function to find specific students
- Sort by any column (registration number, name, year)

### Editing Student Information
1. Select a student from the list
2. Click **Edit Selected Student**
3. Modify the necessary information
4. Click **Update** to save changes

### Student Record Verification
- Ensure registration numbers follow institutional format
- Verify graduation year calculations
- Check for duplicate entries

## Student Progress Tracking

### Academic Status Monitoring
- Track each student's academic level (Year 1, 2, 3, 4)
- Monitor enrollment status (Active, Graduated, Withdrawn)
- View completion percentage across curriculum

### Progress Reports
Generate individual student progress reports:
1. Select student from the list
2. Navigate to **Reports & Analytics** tab
3. Choose **Student Progress Report**
4. Generate PDF report

## Data Management Best Practices

### Registration Number Format
- Use consistent formatting (e.g., "MET/2021/001")
- Avoid special characters that might cause issues
- Maintain institutional naming conventions

### Data Validation
- Double-check student names for accuracy
- Verify graduation year calculations
- Ensure start years match enrollment records

### Privacy and Security
- Access student data only on authorized devices
- Regular database backups are essential
- Follow institutional data protection policies

## Common Tasks

### Finding Students Quickly
- Use Ctrl+F (Cmd+F on Mac) to search the student list
- Filter by graduation year for cohort management
- Sort by surname for alphabetical organization

### Updating Academic Information
- Regularly update student academic levels
- Mark students as graduated when appropriate
- Archive withdrawn students appropriately

### Data Export
- Export student lists for institutional reporting
- Generate enrollment statistics
- Create backup data files

## Troubleshooting

### Common Issues

**Duplicate Registration Numbers**
- Check for typos in registration numbers
- Verify institutional numbering system
- Contact registrar if conflicts exist

**Import Errors**
- Verify CSV file format and encoding
- Check for required column headers
- Ensure data types match expected formats

**Missing Students**
- Check search filters and sorting options
- Verify database connectivity
- Confirm student was added successfully

For additional support, see our [Technical Troubleshooting Guide](../technical/troubleshooting.md).

---

Next: [Assessment Management](assessments.md)