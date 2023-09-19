import re
import toml

config_path = "config.toml"  # Specify the path to your TOML configuration file
config = toml.load(config_path)

# Load the course patterns from the configuration
course_patterns = config["course_patterns"]

# Define a function to normalize registration numbers
def normalize_reg_no(reg_no):
    # Replace O with 0 and remove spaces
    normalized_reg_no = reg_no.replace('O', '0').replace(' ', '')

    # Replace common hyphen variations with a standard hyphen
    normalized_reg_no = re.sub(r'[-‐]', '-', normalized_reg_no)

    return normalized_reg_no

# Function to prompt the user for normalization
def prompt_normalize(reg_no):
    normalized_reg_no = normalize_reg_no(reg_no)
    print(f"Do you want to normalize the registration number '{reg_no}' to '{normalized_reg_no}'? (yes/no): ")
    choice = input().strip().lower()
    
    if choice == 'yes':
        return normalized_reg_no
    else:
        return reg_no

# Check the course pattern for each course
def check_course_pattern(reg_no_value, data, name_value, excel_file, internal_marks, file_course_code):
    matching_course = None
    reg_no_value = prompt_normalize(reg_no_value)  # Prompt user for normalization
    
    for course, pattern in course_patterns.items():
        if re.match(pattern, reg_no_value):
            matching_course = course
            break

    if matching_course:
        data.append((matching_course, file_course_code, reg_no_value, name_value, internal_marks))
    else:
        print(f"Anomaly in file '{excel_file}': Reg. No. value '{reg_no_value}' does not match any of the expected course patterns")

# Example usage of the function
check_course_pattern('E022-01-1415 /2021', data, 'John Doe', 'EMT 3105.xlsx', 95, 'EMT 3105')
