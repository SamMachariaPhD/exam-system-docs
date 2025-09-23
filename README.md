# Open EProS: Exam Processing System

**Open EProS** is a comprehensive, secure exam processing system designed for university departments. This powerful desktop application streamlines the entire exam workflow, from handling raw Excel results to generating official senate documents and maintaining student academic histories.

## Key Features

### 🔐 Secure & Licensed
- **Online license verification**: Email-based authentication with institutional control
- **Data privacy**: All student data remains local and secure
- **Version control**: Automatic updates and system messages

### 📊 Comprehensive Processing
- **Excel input processing**: Familiar format for lecturers
- **Multi-year tracking**: 5-year degree programs with semester-by-semester tracking
- **Student status management**: Academic leave, suspensions, repeats, financial holds
- **Historical validation**: Automatic flagging of status conflicts

### 📋 Official Document Generation
- **Senate documents**: PDF and DOCX formats in official university style
- **Pass/Supplementary lists**: Automated classification and formatting
- **Transcripts**: Individual and batch generation
- **Audit trails**: Complete change tracking and evidence logging

### 🏗️ Robust Architecture
- **Local database**: SQLite for fast processing and offline capability
- **Rule engine**: JSON-based academic regulations
- **Change tracking**: Monitor data modifications vs original Excel files
- **Cross-platform**: Runs on Windows, Mac, and Linux 

## Repository Structure

This project uses a **multi-repository architecture** for security and deployment:

### 🔒 Private Development Repo
**[exam-system-private](https://github.com/SamMachariaPhD/exam-system-private)** (this repo)
- Contains all source code and business logic
- Student data and databases remain local (not in git)
- Development and testing environment

### 📦 Public Releases Repo
**[exam-system-releases](https://github.com/SamMachariaPhD/exam-system-releases)**
- Compiled executables for distribution
- Installation instructions and changelog
- No source code exposed

### 🔑 Authentication Repo
**[exam-system-auth](https://github.com/SamMachariaPhD/exam-system-auth)**
- License verification JSON file
- System messages and update notifications
- API endpoint: `https://raw.githubusercontent.com/SamMachariaPhD/exam-system-auth/main/licenses.json`

## Project Organization

```
project_folder/
├── config.toml                 # Configuration file
├── data/                       # Local student data (not in git)
│   ├── inputs/                 # Raw Excel files from lecturers
│   └── outputs/                # Generated reports and documents
├── modules/
│   ├── __init__.py
│   ├── file_processing.py      # Excel file handling
│   ├── data_consolidation.py   # Data processing and PDF generation
│   ├── utilities.py            # Shared utilities and constants
│   ├── rule_engine.py          # Academic rules and recommendations
│   └── auth/                   # Authentication module (planned)
├── database/                   # SQLite databases (planned)
├── main.py                     # Main application entry point
└── requirements.txt
```

## Development Setup

### Prerequisites
- Python 3.7+
- Git
- Internet connection for license verification

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SamMachariaPhD/exam-system-private.git
   cd exam-system-private
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS and Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## Data Privacy & Security

⚠️ **Important**: This system is designed for sensitive academic data. Please ensure:

- **Never commit student data** to version control
- **Keep databases local** - they contain personal information
- **Use secure networks** for license verification
- **Follow your institution's data protection policies**

## License Management

The system requires online license verification before use. Licenses are managed through the authentication repository and include:

- Institution-specific permissions
- User email verification
- Feature access control
- Automatic update notifications

For license requests, contact the system administrator.
