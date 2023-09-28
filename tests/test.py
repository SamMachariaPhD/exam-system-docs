# # Function to prompt the user for normalization
# def prompt_normalize(reg_no_to_normalize):
#     detail_message = f"Do you want to normalize the registration number '{reg_no_to_normalize}' to '{normalize_reg_no(reg_no_to_normalize)}'? (yes/no)"
#     log_print(detail_message)

#     def on_yes():
#         reg_no_after_normalizing = normalize_reg_no(reg_no_to_normalize)
#         matching_course = None
#         for course, pattern in course_patterns.items():
#             if re.match(pattern, reg_no_after_normalizing):
#                 matching_course = course
#                 break
#         log_print(f"Normalized registration number: {reg_no_after_normalizing}")
#         return reg_no_after_normalizing, matching_course

#     def on_no():
#         matching_course = reg_no_to_normalize[:4]  # pick 1st 4 letters of reg. no.
#         log_print(f"User chose NOT to normalize the registration number.")
#         return reg_no_to_normalize, matching_course

#     def on_exit():
#         log_print(f"User chose to end the program.")
#         sys.exit(0)  # Exit the program

#     def on_window_close():
#         on_exit()  # Call on_exit when the window is closed

#     root = tk.Tk()
#     root.title("Normalize Registration Number")

#     label = tk.Label(root, text=detail_message)
#     label.pack(padx=20, pady=10)

#     yes_button = tk.Button(root, text="Yes", command=lambda: set_result(on_yes()))
#     yes_button.pack(side=tk.LEFT, padx=20)

#     no_button = tk.Button(root, text="No", command=lambda: set_result(on_no()))
#     no_button.pack(side=tk.RIGHT, padx=20)

#     exit_button = tk.Button(root, text="Exit", command=lambda: set_result(on_exit()))
#     exit_button.pack(pady=10)

#     # Bind the window's close event to on_window_close
#     root.protocol("WM_DELETE_WINDOW", on_window_close)

#     def set_result(result):
#         nonlocal result_data
#         result_data = result
#         root.destroy()

#     result_data = None

#     root.mainloop()

#     return result_data






# import tkinter as tk
# import sys

# # Function to prompt the user to continue with the most common year or halt the program
# def prompt_continue_or_halt(most_common_year):
#     detail_message = f"Do you want to continue with the most common year '{most_common_year}'? (yes/no)"
#     log_print(detail_message)

#     def on_yes():
#         log_print(f"Continuing with {most_common_year}")
#         return most_common_year

#     def on_no():
#         log_print("Program halted.")
#         sys.exit(1)  # Halt the program

#     def on_window_close():
#         on_exit()  # Call on_exit when the window is closed

#     root = tk.Tk()
#     root.title("Continue or Halt")

#     label = tk.Label(root, text=detail_message)
#     label.pack(padx=20, pady=10)

#     yes_button = tk.Button(root, text="Yes", command=lambda: set_result(on_yes()))
#     yes_button.pack(side=tk.LEFT, padx=20)

#     no_button = tk.Button(root, text="No", command=lambda: set_result(on_no()))
#     no_button.pack(side=tk.RIGHT, padx=20)

#     # Bind the window's close event to on_window_close
#     root.protocol("WM_DELETE_WINDOW", on_window_close)

#     def set_result(result):
#         nonlocal result_data
#         result_data = result
#         root.destroy()

#     result_data = None

#     root.mainloop()

#     return result_data

# # Example usage:
# most_common_year = 2023  # Replace with the actual most common year
# result = prompt_continue_or_halt(most_common_year)
# print(f"User choice: {result}")








# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# import openpyxl

# class ExcelApp(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Excel Data Analysis App")
#         self.geometry("800x600")

#         self.workbook = None
#         self.sheet_names = []
#         self.active_sheet = None
#         self.last_opened_file_path = ""

#         self.create_menu()
#         self.create_taskbar()
#         self.create_excel_view()

#     def create_menu(self):
#         menubar = tk.Menu(self)
        
#         # File menu
#         file_menu = tk.Menu(menubar, tearoff=0)
#         file_menu.add_command(label="Open", command=self.open_excel)
#         file_menu.add_command(label="Save", command=self.save_excel)
#         menubar.add_cascade(label="File", menu=file_menu)
        
#         # View menu
#         view_menu = tk.Menu(menubar, tearoff=0)
#         view_menu.add_command(label="Display Excel Sheet", command=self.display_excel_sheet)
#         menubar.add_cascade(label="View", menu=view_menu)
        
#         # About menu
#         about_menu = tk.Menu(menubar, tearoff=0)
#         about_menu.add_command(label="How to Use", command=self.show_how_to_use)
#         about_menu.add_command(label="Version and Licenses", command=self.show_version_and_licenses)
#         menubar.add_cascade(label="About", menu=about_menu)
        
#         self.config(menu=menubar)

#     def create_taskbar(self):
#         taskbar = tk.Frame(self)
#         taskbar.pack(side=tk.TOP, fill=tk.X)

#     def create_excel_view(self):
#         self.canvas = tk.Canvas(self)
#         self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#         self.scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
#         self.scrollbar_x.pack(side="bottom", fill="x")
#         self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

#         self.scrollbar_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         self.scrollbar_y.pack(side="right", fill="y")
#         self.canvas.configure(yscrollcommand=self.scrollbar_y.set)

#         self.frame = tk.Frame(self.canvas)
#         self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
#         self.frame.bind("<Configure>", self.on_frame_configure)

#     def on_frame_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def open_excel(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
#         if file_path:
#             self.last_opened_file_path = file_path
#             self.workbook = openpyxl.load_workbook(file_path)
#             self.sheet_names = self.workbook.sheetnames
#             self.active_sheet = None
#             self.update_excel_view()

#     def save_excel(self):
#         if self.workbook:
#             save_path = filedialog.asksaveasfilename(filetypes=[("Excel files", "*.xlsx")])
#             if save_path:
#                 self.workbook.save(save_path)
#                 messagebox.showinfo("Info", "File saved successfully!")

#     def display_excel_sheet(self):
#         if self.workbook:
#             sheet_name = self.sheet_names[0]  # Change this to the desired sheet name
#             self.select_sheet(sheet_name)

#     def update_excel_view(self):
#         for widget in self.frame.winfo_children():
#             widget.destroy()

#         if self.active_sheet:
#             for row_idx, row in enumerate(self.active_sheet.iter_rows(values_only=True), start=1):
#                 for col_idx, cell_value in enumerate(row, start=1):
#                     cell_label = tk.Label(self.frame, text=str(cell_value))
#                     cell_label.grid(row=row_idx, column=col_idx)

#     def select_sheet(self, sheet_name):
#         if self.workbook:
#             self.active_sheet = self.workbook[sheet_name]
#             self.update_excel_view()

#     def show_how_to_use(self):
#         # Add code to display information on how to use the program
#         pass

#     def show_version_and_licenses(self):
#         # Add code to display version and license information
#         pass

# if __name__ == "__main__":
#     app = ExcelApp()
#     app.mainloop()







# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# import openpyxl
# import pandas as pd
# from tkinter import ttk

# class ExcelApp(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Excel Data Analysis App")
#         self.geometry("800x600")

#         self.workbook = None
#         self.sheet_names = []
#         self.active_sheet = None
#         self.last_opened_file_path = ""

#         self.create_menu()
#         self.create_taskbar()
#         self.create_excel_view()

#     def create_menu(self):
#         menubar = tk.Menu(self)
        
#         # File menu
#         file_menu = tk.Menu(menubar, tearoff=0)
#         file_menu.add_command(label="Open", command=self.open_excel)
#         file_menu.add_command(label="Save", command=self.save_excel)
#         file_menu.add_separator()
#         file_menu.add_command(label="Exit", command=self.quit_program)
#         menubar.add_cascade(label="File", menu=file_menu)
        
#         # View menu
#         view_menu = tk.Menu(menubar, tearoff=0)
#         view_menu.add_command(label="Display Excel Sheet", command=self.display_excel_sheet)
#         menubar.add_cascade(label="View", menu=view_menu)
        
#         # About menu
#         about_menu = tk.Menu(menubar, tearoff=0)
#         about_menu.add_command(label="How to Use", command=self.show_how_to_use)
#         about_menu.add_command(label="Version and Licenses", command=self.show_version_and_licenses)
#         menubar.add_cascade(label="About", menu=about_menu)
        
#         self.config(menu=menubar)

#     def create_taskbar(self):
#         taskbar = tk.Frame(self)
#         taskbar.pack(side=tk.TOP, fill=tk.X)

#     def create_excel_view(self):
#         self.canvas = tk.Canvas(self)
#         self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#         self.scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
#         self.scrollbar_x.pack(side="bottom", fill="x")
#         self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

#         self.scrollbar_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         self.scrollbar_y.pack(side="right", fill="y")
#         self.canvas.configure(yscrollcommand=self.scrollbar_y.set)

#         self.frame = tk.Frame(self.canvas)
#         self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
#         self.frame.bind("<Configure>", self.on_frame_configure)

#     def on_frame_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def open_excel(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
#         if file_path:
#             self.last_opened_file_path = file_path
#             self.workbook = openpyxl.load_workbook(file_path)
#             self.sheet_names = self.workbook.sheetnames
#             self.active_sheet = None
#             self.update_excel_view()

#     def save_excel(self):
#         if self.workbook:
#             save_path = filedialog.asksaveasfilename(filetypes=[("Excel files", "*.xlsx")])
#             if save_path:
#                 self.workbook.save(save_path)
#                 messagebox.showinfo("Info", "File saved successfully!")

#     def display_excel_sheet(self):
#         if self.workbook:
#             sheet_name = self.sheet_names[0]  # Change this to the desired sheet name
#             self.select_sheet(sheet_name)

#     def update_excel_view(self):
#         for widget in self.frame.winfo_children():
#             widget.destroy()

#         if self.active_sheet:
#             # Read data into a pandas DataFrame for better formatting
#             df = pd.DataFrame(self.active_sheet.values)
            
#             # Create a ttk Treeview widget to display the DataFrame
#             tree = ttk.Treeview(self.frame, columns=list(df.columns), show="headings")
            
#             # Add columns to the Treeview
#             for col in df.columns:
#                 tree.heading(col, text=col)
            
#             # Insert data into the Treeview
#             for i, row in df.iterrows():
#                 tree.insert("", "end", values=list(row))
            
#             tree.grid(row=0, column=0, sticky="nsew")
#             self.frame.grid_rowconfigure(0, weight=1)
#             self.frame.grid_columnconfigure(0, weight=1)

#     def select_sheet(self, sheet_name):
#         if self.workbook:
#             self.active_sheet = self.workbook[sheet_name]
#             self.update_excel_view()

#     def show_how_to_use(self):
#         # Add code to display information on how to use the program
#         pass

#     def show_version_and_licenses(self):
#         # Add code to display version and license information
#         pass

#     def quit_program(self):
#         self.destroy()

# if __name__ == "__main__":
#     app = ExcelApp()
#     app.mainloop()





# # Initialize a global flag to remember if the user chose to normalize all
# normalize_all_flag = False

# # Function to prompt the user for normalization
# def prompt_normalize(reg_no_to_normalize):
#     global normalize_all_flag

#     if normalize_all_flag:
#         # If the user chose to normalize all in the previous call, default to on_yes()
#         return on_yes()

#     detail_message = f"Do you want to normalize the registration number '{reg_no_to_normalize}' to '{normalize_reg_no(reg_no_to_normalize)}'? (yes/no/normalize all)"
#     log_print(detail_message)

#     def on_yes():
#         reg_no_after_normalizing = normalize_reg_no(reg_no_to_normalize)
#         matching_course = None
#         for course, pattern in course_patterns.items():
#             if re.match(pattern, reg_no_after_normalizing):
#                 matching_course = course
#                 break
#         log_print(f"Normalized registration number: {reg_no_after_normalizing}")
#         return reg_no_after_normalizing, matching_course

#     def on_no():
#         matching_course = reg_no_to_normalize[:4]  # pick 1st 4 letters of reg. no.
#         log_print(f"User chose NOT to normalize the registration number.")
#         return reg_no_to_normalize, matching_course

#     def on_normalize_all():
#         global normalize_all_flag
#         normalize_all_flag = True
#         log_print(f"User chose to normalize all.")
#         return on_yes()  # Default to on_yes() when normalizing all

#     def on_exit():
#         log_print(f"User chose to end the program.")
#         sys.exit(0)  # Exit the program

#     def on_window_close():
#         on_exit()  # Call on_exit when the window is closed

#     root = tk.Tk()
#     root.title("Normalize Registration Number")

#     label = tk.Label(root, text=detail_message)
#     label.pack(padx=20, pady=10)

#     yes_button = tk.Button(root, text="Yes", command=lambda: set_result(on_yes()))
#     yes_button.pack(side=tk.LEFT, padx=20)

#     no_button = tk.Button(root, text="No", command=lambda: set_result(on_no()))
#     no_button.pack(side=tk.RIGHT, padx=20)

#     normalize_all_button = tk.Button(root, text="Normalize All", command=lambda: set_result(on_normalize_all()))
#     normalize_all_button.pack(pady=10)

#     exit_button = tk.Button(root, text="Exit", command=lambda: set_result(on_exit()))
#     exit_button.pack(pady=10)

#     # Bind the window's close event to on_window_close
#     root.protocol("WM_DELETE_WINDOW", on_window_close)

#     def set_result(result):
#         nonlocal result_data
#         result_data = result
#         root.destroy()

#     result_data = None

#     root.mainloop()

#     return result_data


# import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Suppress pygame startup message
# import pygame
# import tkinter as tk
# from tkinter import font

# # Initialize pygame mixer without opening a window
# pygame.mixer.pre_init(44100, -16, 2, 2048)  # You can adjust these parameters as needed
# pygame.mixer.init()
# pygame.init()

# # Function to close the window after a delay
# def close_window_after_delay(window):
#     window.after(5000, window.destroy)  # Close the window after 5 seconds (5000 milliseconds)

# # Function to show the completion message and perform actions
# def show_completion_message():
#     # Create a tkinter window
#     root = tk.Tk()
#     root.title("Task Completion")
#     root.geometry("400x300")  # Set the initial window size here (width x height)

#     # Specify a font that includes a better-looking checkmark symbol
#     custom_font = font.Font(family="DejaVu Sans", size=12)

#     # Create a list of messages with real tick symbols (checkmarks)
#     messages = [
#         "\u2713 Task Completed!",  # This checkmark is from the DejaVu Sans font
#         "\u2713 Check output files in the output folder."
#     ]

#     # Display the messages as labels with the custom font
#     for message in messages:
#         label = tk.Label(root, text=message, font=custom_font)
#         label.pack(anchor='w', padx=20)

#     # Specify the absolute path to the sound file
#     sound_file = os.path.abspath("../data/inputs/sounds/mixkit_co_arrow_whoosh_1491.wav")
#     if os.path.exists(sound_file):
#         pygame.mixer.music.load(sound_file)
#         pygame.mixer.music.play()

#     # Close the window after a delay
#     close_window_after_delay(root)

#     # Start the tkinter main loop
#     root.mainloop()

# # Call the function to show the completion message
# show_completion_message()

# # Quit pygame to prevent the black window from appearing
# pygame.quit()



import sys
import tkinter as tk
from tkinter import filedialog

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
            print("Input and output folders must be specified.")
            root.destroy()
            sys.exit(0)  # Exit the program
        else:
            print("Selected Input Folder:", input_path)
            print("Selected Output Folder:", output_path)
            root.destroy()

    def on_window_close():
        print("The user chose to end the program.")
        root.destroy()
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

# Call the function to select input and output folders
input_path, output_path = select_input_output_folders()
print("Input Folder Path:", input_path)
print("Output Folder Path:", output_path)












# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# import openpyxl
# import pandas as pd
# from tkinter import ttk

# class ExcelApp(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Open EProS")
#         self.geometry("800x600")

#         self.workbook = None
#         self.sheet_names = []
#         self.active_sheet = None
#         self.last_opened_file_path = ""

#         self.zoom_factor = 1.0  # Initial zoom factor

#         self.create_menu()
#         self.create_taskbar()
#         self.create_excel_view()

#     def create_menu(self):
#         menubar = tk.Menu(self)
        
#         # File menu
#         file_menu = tk.Menu(menubar, tearoff=0)
#         file_menu.add_command(label="Open", command=self.open_excel)
#         file_menu.add_command(label="Save", command=self.save_excel)
#         file_menu.add_separator()
#         file_menu.add_command(label="Exit", command=self.quit_program)
#         menubar.add_cascade(label="File", menu=file_menu)
        
#         # View menu
#         view_menu = tk.Menu(menubar, tearoff=0)
#         view_menu.add_command(label="Display Excel Sheet", command=self.display_excel_sheet)
#         view_menu.add_command(label="Zoom In", command=self.zoom_in)
#         view_menu.add_command(label="Zoom Out", command=self.zoom_out)
#         menubar.add_cascade(label="View", menu=view_menu)
        
#         # About menu
#         about_menu = tk.Menu(menubar, tearoff=0)
#         about_menu.add_command(label="How to Use", command=self.show_how_to_use)
#         about_menu.add_command(label="Version and Licenses", command=self.show_version_and_licenses)
#         menubar.add_cascade(label="About", menu=about_menu)
        
#         self.config(menu=menubar)

#     def create_taskbar(self):
#         taskbar = tk.Frame(self)
#         taskbar.pack(side=tk.TOP, fill=tk.X)

#     def create_excel_view(self):
#         self.canvas = tk.Canvas(self)
#         self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#         self.scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
#         self.scrollbar_x.pack(side="bottom", fill="x")
#         self.canvas.configure(xscrollcommand=self.scrollbar_x.set)

#         self.scrollbar_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         self.scrollbar_y.pack(side="right", fill="y")
#         self.canvas.configure(yscrollcommand=self.scrollbar_y.set)

#         self.frame = tk.Frame(self.canvas)
#         self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
#         self.frame.bind("<Configure>", self.on_frame_configure)

#     def on_frame_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def open_excel(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
#         if file_path:
#             self.last_opened_file_path = file_path
#             self.workbook = openpyxl.load_workbook(file_path)
#             self.sheet_names = self.workbook.sheetnames
#             self.active_sheet = None
#             self.update_excel_view()

#     def save_excel(self):
#         if self.workbook:
#             save_path = filedialog.asksaveasfilename(filetypes=[("Excel files", "*.xlsx")])
#             if save_path:
#                 self.workbook.save(save_path)
#                 messagebox.showinfo("Info", "File saved successfully!")

#     def display_excel_sheet(self):
#         if self.workbook:
#             sheet_name = self.sheet_names[0]  # Change this to the desired sheet name
#             self.select_sheet(sheet_name)

#     def update_excel_view(self):
#         for widget in self.frame.winfo_children():
#             widget.destroy()

#         if self.active_sheet:
#             # Read data into a pandas DataFrame for better formatting
#             df = pd.DataFrame(self.active_sheet.values)
            
#             # Create a ttk Treeview widget to display the DataFrame
#             tree = ttk.Treeview(self.frame, columns=list(df.columns), show="headings", height=len(df) + 1)
            
#             # Add columns to the Treeview
#             for col in df.columns:
#                 tree.heading(col, text=col)
            
#             # Set cell sizes based on zoom factor
#             cell_width = int(80 * self.zoom_factor)
#             cell_height = int(25 * self.zoom_factor)
#             tree.column("#1", width=cell_width, stretch=tk.NO)
#             for col in df.columns:
#                 tree.column(col, width=cell_width, stretch=tk.NO)
#                 tree.heading(col, text=col, anchor=tk.W)
            
#             # Insert data into the Treeview
#             for i, row in df.iterrows():
#                 tree.insert("", "end", values=list(row))
            
#             tree.grid(row=0, column=0, sticky="nsew")
#             self.frame.grid_rowconfigure(0, weight=1)
#             self.frame.grid_columnconfigure(0, weight=1)

#     def select_sheet(self, sheet_name):
#         if self.workbook:
#             self.active_sheet = self.workbook[sheet_name]
#             self.update_excel_view()

#     def show_how_to_use(self):
#         # Code to display information on how to use the program
#         pass

#     def show_version_and_licenses(self):
#         # Code to display version and license information
#         pass

#     def quit_program(self):
#         self.destroy()

#     def zoom_in(self):
#         self.zoom_factor *= 1.2  # Increase zoom factor by 20%
#         self.update_excel_view()

#     def zoom_out(self):
#         self.zoom_factor /= 1.2  # Decrease zoom factor by 20%
#         self.update_excel_view()

# if __name__ == "__main__":
#     app = ExcelApp()
#     app.mainloop()
