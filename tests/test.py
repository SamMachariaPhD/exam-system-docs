# Function to prompt the user for normalization
def prompt_normalize(reg_no_to_normalize):
    detail_message = f"Do you want to normalize the registration number '{reg_no_to_normalize}' to '{normalize_reg_no(reg_no_to_normalize)}'? (yes/no)"
    log_print(detail_message)

    def on_yes():
        reg_no_after_normalizing = normalize_reg_no(reg_no_to_normalize)
        matching_course = None
        for course, pattern in course_patterns.items():
            if re.match(pattern, reg_no_after_normalizing):
                matching_course = course
                break
        log_print(f"Normalized registration number: {reg_no_after_normalizing}")
        return reg_no_after_normalizing, matching_course

    def on_no():
        matching_course = reg_no_to_normalize[:4]  # pick 1st 4 letters of reg. no.
        log_print(f"User chose NOT to normalize the registration number.")
        return reg_no_to_normalize, matching_course

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

    exit_button = tk.Button(root, text="Exit", command=lambda: set_result(on_exit()))
    exit_button.pack(pady=10)

    # Bind the window's close event to on_window_close
    root.protocol("WM_DELETE_WINDOW", on_window_close)

    def set_result(result):
        nonlocal result_data
        result_data = result
        root.destroy()

    result_data = None

    root.mainloop()

    return result_data