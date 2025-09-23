import os
import sys
import toml
import tkinter as tk
from modules.file_processing import *
from modules.data_consolidation import *
from modules.utilities import *
from modules.auth.login_dialog import LoginDialog


def authenticate_user():
    """Authenticate user before allowing system access."""
    root = tk.Tk()
    root.withdraw()  # Hide main window during login

    login_dialog = LoginDialog()

    if login_dialog.show_login():
        user_info = login_dialog.get_user_info()
        log_print(f"User authenticated: {user_info['email']}")
        root.destroy()
        return True, user_info
    else:
        log_print("Authentication failed or cancelled.")
        root.destroy()
        return False, None


if __name__ == "__main__":
    print("=" * 50)
    print("Open EProS - Exam Processing System")
    print("=" * 50)

    # Authenticate user first
    authenticated, user_info = authenticate_user()

    if not authenticated:
        print("Authentication required. Exiting...")
        sys.exit(1)

    print(f"Welcome, {user_info['email']}!")
    print("-" * 50)

    config_path = "config.toml"  # Specify the path to your TOML configuration file

    running_report_path = None  # Initialize the global variable
    # Load paths from configuration
    config = toml.load(config_path)
    input_path, output_path = select_input_output_folders()

    # input_folder_path = config["input_folder"]["path"]
    input_folder_path = input_path 

    # consolidated_excel_output_path = config["consolidated_excel_output"]["path"]
    consolidated_excel_output_path = output_path + "/consolidated.xlsx"

    # pass_list_pdf_output_path = config["pass_list_pdf_output"]["path"]
    pass_list_pdf_output_path = output_path + "/pass_list.pdf"

    # supp_list_pdf_output_path = config["supp_list_pdf_output"]["path"]
    supp_list_pdf_output_path = output_path + "/supp_list.pdf"

    # senate_doc_pdf_output_path = config["senate_documents_output"]["path"]
    senate_doc_pdf_output_path = output_path + "/senate_doc.pdf"

    mechatronics_units_path = config["mechatronics_engineering_units"]["path"]
    
    # running_report_path = config["running_report"]["path"]
    running_report_path = output_path + "/running_report.txt"

    setup_logging(running_report_path)
    # exit()
    # Log the output to the file and print to the console
    log_print("Starting the program...")

    # Get the Excel files using the function from the utilities module
    excel_files = list_excel_files(input_folder_path)

    consolidate_mark_sheet(mechatronics_units_path, input_folder_path, excel_files, consolidated_excel_output_path, pass_list_pdf_output_path, supp_list_pdf_output_path, senate_doc_pdf_output_path, running_report_path, config_path)

    log_print(f"Mark sheet consolidated and saved as '{consolidated_excel_output_path}'.")

    # Call the function to show the completion message
    show_completion_message()