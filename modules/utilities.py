import os, json 
import re, sys 
import toml
import numpy as np
import pandas as pd

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Must be before pygame to SUPPRESS pygame startup message
import pygame
from tkinter import font


config_path = "config.toml"  # Specify the path to your TOML configuration file

# Load the configuration from the TOML file
config = toml.load(config_path)

# input_folder_path = config["input_folder"]["path"]
# running_report_path = config["running_report"]["path"]

# Load the course patterns from the configuration
course_patterns = config["course_patterns"]
# course_patterns = config["course_patterns"]["E022"] # Mechatronics 
# print(course_patterns)

# excel_files = [file for file in os.listdir(input_folder_path) if file.endswith('.xlsx')]



def list_excel_files(input_folder_path):
    """
    Lists all Excel files in the specified input folder.

    Args:
        input_folder_path (str): The path to the input folder.

    Returns:
        List[str]: A list of Excel file names in the input folder.
    """
    excel_files = [file for file in os.listdir(input_folder_path) if file.endswith('.xlsx')]
    return excel_files



# List to store collected data
collected_data = []

# Dictionary to track courses found in each Excel file
course_files = {}
course_code = []
course_code_data = []
# file_course_code = []

# List to track files without "REG. NO." cell
files_without_reg_no = []



def loop_to_consolidate(input_folder_path, excel_files, consolidated_df, collected_data):
    # Loop through each Excel file and consolidate the data
    for excel_file in excel_files:
        file_path = os.path.join(input_folder_path, excel_file)
        # global file_course_code 
        file_course_code = file_path.split("/")[-1].split(".xlsx")[0]
        # print(file_course_code)
        # df = pd.read_excel(file_path, header=None)  # Read without header

        # Read the Excel sheet into a Pandas DataFrame
        initial_df = pd.read_excel(file_path, header=None)

        # Define a regular expression pattern for the keyword variations
        summary_keyword_pattern = r'summary\s*of\s*results|summary|analysis'

        # Find the index where the keyword pattern appears (case-insensitive)
        split_indices = initial_df[initial_df.apply(lambda row: re.search(summary_keyword_pattern, str(row), re.IGNORECASE), axis=1).notna()].index

        # Check if any indices were found
        if len(split_indices) > 0:
            # Keep only the rows before the first keyword pattern
            split_index = split_indices[0]
            df = initial_df.iloc[:split_index]
        else:
            # Handle the case where the keyword pattern was not found
            print("Summary keyword pattern for {} not found in the DataFrame.".format(file_path))
            print("Please add the keyword 'summary' or delete the file and rerun.")
            sys.exit(1)

        # Search for the cell containing 'REG. NO.'
        get_reg_no_data(df, excel_file, file_course_code)
    # print(course_code)

    # Extract course codes from course_code_data[0] and remove ".xlsx" and "E022"
    course_code = [key.split('.')[0] for key in course_code_data[0].keys()]

    # Print the resulting list
    # print(course_code)
    return course_code



def get_reg_no_data(df, excel_file, file_course_code):
    # Search for the cell containing 'REG. NO.'
    # Improved search resilient to variations and potential errors in the input files

    reg_no_cell = None
    internal_marks_cell = None
    for index, row in df.iterrows():
        lower_row_values = [str(val).lower() for val in row.values]

        # Define a pattern for 'REG. NO.' and 'INTERNAL EXAMINER MARKS /100' variations using regular expressions
        reg_no_pattern = re.compile(r'reg\s*\.?\s*no\s*\.?|reg_no', re.IGNORECASE)


        # Define a regular expression pattern to match all variations
        internal_marks_cell_pattern = re.compile(r'(int\.?|internal)\s*examiner\s*marks\s*/?\s*100', re.IGNORECASE)

        matching_indices = [i for i, val in enumerate(lower_row_values) if reg_no_pattern.search(val)]
        # print(matching_indices)
        internal_marks_indices = [i for i, val in enumerate(lower_row_values) if internal_marks_cell_pattern.search(val)]
        # print(internal_marks_indices)
        if matching_indices: # access when it is fist not empty 
            reg_no_cell = (index, matching_indices[0])
            # print(reg_no_cell)
            internal_marks_cell = (index, internal_marks_indices[0]) if internal_marks_indices else None
            # print(internal_marks_cell)
            # print(excel_file)
            # break # don't break otherwise you'll stop search 
        

    if reg_no_cell is not None and internal_marks_cell is not None:
        reg_no_row = reg_no_cell[0]
        reg_no_col = reg_no_cell[1]
        internal_marks_row = internal_marks_cell[0]
        internal_marks_col = internal_marks_cell[1]

        # Collect data below the 'REG. NO.' cell and corresponding data to the right
        data = []
        for row_idx in range(reg_no_row + 1, len(df)):
            global reg_no_value
            reg_no_value = df.iloc[row_idx, reg_no_col]
            name_value = df.iloc[row_idx, reg_no_col + 1]
            internal_marks = df.iloc[row_idx, internal_marks_col]
            # print(internal_marks)
            if isinstance(reg_no_value, str):
                reg_no_value = reg_no_value.strip()  # Strip whitespace from value


                if isinstance(internal_marks, str):
                    internal_marks = internal_marks.replace("-", "").strip()
                    if internal_marks.isdigit():
                        internal_marks = int(internal_marks)
                    else:
                        internal_marks = np.nan
                elif isinstance(internal_marks, int):
                    pass
                else:
                    # Convert the integer to float (if needed) and handle other non-string cases
                    if not isinstance(internal_marks, (int, float)):
                        internal_marks = np.nan

                # Check the course pattern for each course and add data
                check_course_pattern(reg_no_value, data, name_value, excel_file, internal_marks, file_course_code)
                
        # open('data0.txt', 'w').writelines('\n'.join(map(str, data)) + '\n')

        # Add the collected data to the list, eliminating duplicates
        for course, file_course_code, reg_no, name, internal_marks in data:
            # open('data0.txt', 'w').writelines('\n'.join(map(str, data)) + '\n')
            if (reg_no, name) not in collected_data:
                collected_data.append((course, file_course_code, reg_no, name, internal_marks))
                open('../collected_data.txt', 'w').writelines('\n'.join(map(str, collected_data)) + '\n')

        # Store courses found in the current file
        course_files[excel_file] = set(course for course, _, _, _, _, in data)
        course_code_data.append(course_files)
        # print(course_files)
        # print(excel_file)
    elif reg_no_cell is None:
        files_without_reg_no.append(excel_file)
    elif internal_marks_cell is None:
        log_print("Maybe 'INTERNAL EXAMINER MARKS /100' cell is missing in {}.".format(excel_file))

    # Check for mixed courses in each Excel file
    for excel_file, courses in course_files.items():
        if len(courses) > 1:
            log_print(f"Warning: Excel file '{excel_file}' contains data from multiple courses: {', '.join(courses)}.")

    # print(course_code_data)



# Define a function to normalize registration numbers
def normalize_reg_no(reg_no_to_normalize):
    # Replace O with 0 and remove spaces
    normalized_reg_no = reg_no_to_normalize.replace('O', '0').replace(' ', '')

    # Replace common hyphen variations with a standard hyphen
    normalized_reg_no = re.sub(r'[-‐]', '-', normalized_reg_no)

    return normalized_reg_no




# Initialize a global flag to remember if the user chose to normalize all
normalize_all_flag = False

# Function to prompt the user for normalization
def prompt_normalize(reg_no_to_normalize):
    global normalize_all_flag

    def on_yes():
        reg_no_after_normalizing = normalize_reg_no(reg_no_to_normalize)
        matching_course = None
        for course, pattern in course_patterns.items():
            if re.match(pattern, reg_no_after_normalizing):
                matching_course = course
                break
        log_print(f"Normalized registration number: {reg_no_after_normalizing}")
        return reg_no_after_normalizing, matching_course

    if normalize_all_flag:
        # If the user chose to normalize all in the previous call, default to on_yes()
        return on_yes()

    detail_message = f"Do you want to normalize the registration number '{reg_no_to_normalize}' to '{normalize_reg_no(reg_no_to_normalize)}'? (yes/no)"
    log_print(detail_message)

    def on_no():
        matching_course = reg_no_to_normalize[:4]  # pick 1st 4 letters of reg. no.
        log_print(f"User chose NOT to normalize the registration number.")
        return reg_no_to_normalize, matching_course

    def on_normalize_all():
        global normalize_all_flag
        normalize_all_flag = True
        log_print(f"User chose to normalize all.")
        return on_yes()  # Default to on_yes() when normalizing all

    def on_exit():
        log_print(f"User chose to end the program.")
        sys.exit(0)  # Exit the program

    def on_window_close():
        on_exit()  # Call on_exit when the window is closed

    root = tk.Tk()
    root.title("Normalize Registration Number")

    label = tk.Label(root, text=detail_message)
    label.pack(padx=20, pady=10)

    yes_button = tk.Button(root, text="Yes", command=lambda: set_result(on_yes()))
    yes_button.pack(side=tk.LEFT, padx=20)

    no_button = tk.Button(root, text="No", command=lambda: set_result(on_no()))
    no_button.pack(side=tk.RIGHT, padx=20)

    normalize_all_button = tk.Button(root, text="Normalize All", command=lambda: set_result(on_normalize_all()))
    normalize_all_button.pack(pady=10)

    # exit_button = tk.Button(root, text="Exit", command=lambda: set_result(on_exit()))
    # exit_button.pack(pady=10)

    # Bind the window's close event to on_window_close
    root.protocol("WM_DELETE_WINDOW", on_window_close)

    def set_result(result):
        nonlocal result_data
        result_data = result
        root.destroy()

    result_data = None

    root.mainloop()

    return result_data



# Check the course pattern for each course
def check_course_pattern(reg_no_value, data, name_value, excel_file, internal_marks, file_course_code):
    # global matching_course
    matching_course = None
    for course, pattern in course_patterns.items():
        if re.match(pattern, reg_no_value):
            matching_course = course
            break # break loop if no match 

    if not matching_course:
        log_print(f"Anomaly in file '{excel_file}': Reg. No. value '{reg_no_value}' does not match any of the expected course patterns")
        reg_no_value, matching_course = prompt_normalize(reg_no_value)  # Prompt user for normalization
            
    data.append((matching_course, file_course_code, reg_no_value, name_value, internal_marks))



# def setup_logging(running_report_path):
#     # Create or recreate the 'running_reports.txt' file
#     with open(running_report_path, 'w') as log_file:
#         pass  # This will create an empty file if it doesn't exist or truncate it if it does

# def log_print(text):
#     # Append the text to 'running_reports.txt'
#     with open(running_report_path, 'a') as log_file:
#         log_file.write(text + '\n')
    
#     # Print the text to the console
#     print(text)


# running_report_path = None  # Initialize the global variable
# print(f"outside utils: {running_report_path}")

def setup_logging(log_path):
    global running_report_path
    running_report_path = log_path
    # print(f"setup: {running_report_path}")
    # Create or recreate the 'running_reports.txt' file
    with open(running_report_path, 'w') as log_file:
        # pass  # This will create an empty file if it doesn't exist or truncate it if it does
        for message in init_path_messages:
            log_file.write(message + "\n")


def log_print(text):
    global running_report_path
    # print(f"log: {running_report_path}")
    # Append the text to 'running_reports.txt'
    with open(running_report_path, 'a') as log_file:
        log_file.write(text + '\n')
    
    # Print the text to the console
    print(text)



# Find unit name given unit code 
def find_unit_name(mechatronics_units_path, unit_code):
    mechatronics_json_data = json.load(open(mechatronics_units_path))
    for year, semesters in mechatronics_json_data.items():
        for semester, units in semesters.items():
            if isinstance(units, list):
                for unit in units:
                    if unit["Unit Code"] == unit_code:
                        return unit["Unit Title"]
            elif isinstance(units, dict):
                for option, option_units in units.items():
                    for unit in option_units:
                        if unit["Unit Code"] == unit_code:
                            return unit["Unit Title"]
    return "Unit not found"





# Initialize pygame mixer without opening a window
pygame.mixer.pre_init(44100, -16, 2, 2048)  # You can adjust these parameters as needed
pygame.mixer.init()
pygame.init()

# Function to play a sound
def play_sound(sound_path):
    if os.path.exists(sound_path):
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        pygame.time.delay(3000)  # Delay for 3 seconds (3000) to allow sound to play



# Function to show the completion message and perform actions
def show_completion_message():
    # Create a tkinter window
    root = tk.Tk()
    root.withdraw()

    # Display the success message with a built-in icon
    tk.messagebox.showinfo("Task Completed", "Task Completed!\nCheck the output folder.")

    # Specify the absolute path to the sound file
    sound_file = os.path.abspath("data/inputs/sounds/mixkit_co_arrow_whoosh_1491.wav")
    play_sound(sound_file)

    # Start the tkinter main loop
    root.destroy()




init_path_messages = []


def select_input_output_folders():
    def choose_input_folder():
        input_folder = filedialog.askdirectory()
        input_folder_path.set(input_folder)

    def choose_output_folder():
        output_folder = filedialog.askdirectory()
        output_folder_path.set(output_folder)

    def okay_button_clicked():
        input_path = input_folder_path.get()
        output_path = output_folder_path.get()

        if not input_path or not output_path:
            # log_print("Exit: Input and output folders must be specified.")
            init_path_messages.append("Exit: Input and output folders must be specified.")
            root.destroy()

            warning_window = tk.Tk()
            warning_window.withdraw()  # Hide the warning window
            tk.messagebox.showwarning("Warning", "Input and output folders must be specified.")

            # Play a warning sound
            # Specify the absolute path to the sound file
            sound_file = os.path.abspath("data/inputs/sounds/mixkit_co_martial_arts_fast_punch_2047.wav")
            play_sound(sound_file)


            sys.exit(0)  # Exit the program
        else:
            # log_print(f"Selected Input Folder: {input_path}")
            init_path_messages.append(f"Selected Input Folder: {input_path}")
            # log_print(f"Selected Output Folder: {output_path}")
            init_path_messages.append(f"Selected Output Folder: {output_path}")
            root.destroy()

    def on_window_close():
        # log_print("The user chose to end the program.")
        init_path_messages.append("The user chose to end the program.")
        root.destroy()
        warning_window = tk.Tk()
        warning_window.withdraw()  # Hide the warning window
        tk.messagebox.showwarning("Warning", "The user chose to end the program.")

        # Play a warning sound
        # Specify the absolute path to the sound file
        sound_file = os.path.abspath("data/inputs/sounds/mixkit_co_martial_arts_fast_punch_2047.wav")
        play_sound(sound_file)
        sys.exit(0)  # Exit the program

    # Create the main window
    root = tk.Tk()
    root.title("Folder Selection")

    # Variables to store folder paths
    input_folder_path = tk.StringVar()
    output_folder_path = tk.StringVar()

    # Input folder label and "Browse" button
    input_label = tk.Label(root, text="Select Input Folder:")
    input_label.grid(row=0, column=0, sticky="w", padx=(20, 0))
    input_button = tk.Button(root, text="Browse", command=choose_input_folder)
    input_button.grid(row=0, column=1, padx=(0, 20))

    # Chosen input folder path label
    input_path_label = tk.Label(root, textvariable=input_folder_path)
    input_path_label.grid(row=1, column=0, columnspan=2, padx=20)

    # Output folder label and "Browse" button
    output_label = tk.Label(root, text="Select Output Folder:")
    output_label.grid(row=2, column=0, sticky="w", padx=(20, 0))
    output_button = tk.Button(root, text="Browse", command=choose_output_folder)
    output_button.grid(row=2, column=1, padx=(0, 20))

    # Chosen output folder path label
    output_path_label = tk.Label(root, textvariable=output_folder_path)
    output_path_label.grid(row=3, column=0, columnspan=2, padx=20)

    # "Okay" button to validate and close the window
    okay_button = tk.Button(root, text="Okay", command=okay_button_clicked)
    okay_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

    # Bind the window's close event to on_window_close
    root.protocol("WM_DELETE_WINDOW", on_window_close)

    root.mainloop()

    # Return the selected input and output folder paths
    return input_folder_path.get(), output_folder_path.get()
