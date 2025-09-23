import tkinter as tk
from tkinter import messagebox, ttk
from .license_manager import LicenseManager

class LoginDialog:
    """
    Login dialog for Open EProS authentication.
    """

    def __init__(self, parent=None):
        self.parent = parent
        self.license_manager = LicenseManager()
        self.user_email = None
        self.license_data = None
        self.authenticated = False

        self.dialog = None
        self.email_entry = None

    def show_login(self) -> bool:
        """
        Show login dialog and return authentication status.

        Returns:
            bool: True if authenticated successfully
        """
        self.dialog = tk.Toplevel(self.parent) if self.parent else tk.Tk()
        self.dialog.title("Open EProS - Authentication")
        self.dialog.geometry("500x400")
        self.dialog.resizable(False, False)

        # Center the dialog
        self.dialog.transient(self.parent)
        if self.parent:
            self.dialog.grab_set()

        self._create_widgets()
        self._center_dialog()

        # Wait for dialog to complete
        self.dialog.wait_window()

        return self.authenticated

    def _create_widgets(self):
        """Create the login dialog widgets."""
        # Main frame
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="Open EProS",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 5))

        subtitle_label = ttk.Label(
            main_frame,
            text="Exam Processing System",
            font=("Arial", 10)
        )
        subtitle_label.pack(pady=(0, 20))

        # System message
        try:
            system_msg = self.license_manager.get_system_message()
            msg_label = ttk.Label(
                main_frame,
                text=system_msg,
                font=("Arial", 9),
                foreground="blue"
            )
            msg_label.pack(pady=(0, 20))
        except:
            pass

        # Email input
        ttk.Label(main_frame, text="Email Address:").pack(anchor=tk.W, pady=(0, 5))

        self.email_entry = ttk.Entry(main_frame, width=50, font=("Arial", 10))
        self.email_entry.pack(fill=tk.X, pady=(0, 20))
        self.email_entry.focus()

        # Bind Enter key to login
        self.email_entry.bind('<Return>', lambda e: self._attempt_login())

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))

        ttk.Button(
            button_frame,
            text="Login",
            command=self._attempt_login
        ).pack(side=tk.RIGHT, padx=(5, 0))

        ttk.Button(
            button_frame,
            text="Cancel",
            command=self._cancel_login
        ).pack(side=tk.RIGHT)

        # Info section
        info_frame = ttk.LabelFrame(main_frame, text="Authorization Info", padding="10")
        info_frame.pack(fill=tk.X, pady=(20, 0))

        info_text = """Authorized Users:
• samuel.macharia@dkut.ac.ke
• sirmaxford@gmail.com
• All DKUT Mechatronics Engineering (@dkut.ac.ke)

For access requests, contact the system administrator."""

        ttk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 9),
            justify=tk.LEFT
        ).pack(anchor=tk.W)

    def _center_dialog(self):
        """Center the dialog on screen or parent."""
        self.dialog.update_idletasks()

        if self.parent:
            x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - (self.dialog.winfo_width() // 2)
            y = self.parent.winfo_y() + (self.parent.winfo_height() // 2) - (self.dialog.winfo_height() // 2)
        else:
            x = (self.dialog.winfo_screenwidth() // 2) - (self.dialog.winfo_width() // 2)
            y = (self.dialog.winfo_screenheight() // 2) - (self.dialog.winfo_height() // 2)

        self.dialog.geometry(f"+{x}+{y}")

    def _attempt_login(self):
        """Attempt to authenticate user."""
        email = self.email_entry.get().strip().lower()

        if not email:
            messagebox.showerror("Error", "Please enter your email address.")
            return

        if "@" not in email:
            messagebox.showerror("Error", "Please enter a valid email address.")
            return

        # Show loading message
        self.email_entry.config(state='disabled')
        self.dialog.update()

        try:
            # Verify license
            is_valid, message, license_data = self.license_manager.verify_license(email)

            if is_valid:
                self.user_email = email
                self.license_data = license_data
                self.authenticated = True

                messagebox.showinfo("Success", message)
                self._close_dialog()
            else:
                messagebox.showerror("Access Denied", message)

        except Exception as e:
            messagebox.showerror("Error", f"Authentication failed: {str(e)}")

        finally:
            self.email_entry.config(state='normal')

    def _cancel_login(self):
        """Cancel login process."""
        self.authenticated = False
        self._close_dialog()

    def _close_dialog(self):
        """Close the dialog."""
        if self.dialog:
            self.dialog.destroy()

    def get_user_info(self):
        """Get authenticated user information."""
        return {
            'email': self.user_email,
            'license_data': self.license_data,
            'authenticated': self.authenticated
        }