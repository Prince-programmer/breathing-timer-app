import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import winsound

class BreathingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Breathing Timer")

        # Setting a modern, clean color theme
        self.root.configure(bg='#f0f0f0')

        # Create a style object for customization
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 10), padding=5)
        self.style.configure("TLabel", font=("Helvetica", 12), padding=5)
        self.style.configure("TEntry", font=("Helvetica", 10))

        # Default countdown values
        self.breath_time = tk.IntVar(value=4)  # Only asking for inhale time
        self.cycles = tk.IntVar(value=3)
        self.show_cycle = tk.BooleanVar(value=True)  # Checkbox state for showing cycles

        # Create settings UI
        self.create_settings_ui()

        # To keep track of the current cycle
        self.current_cycle = 0

    def create_settings_ui(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.pack_forget()

        # Header label for the app title
        header_label = ttk.Label(self.root, text="Breathing Exercise", font=("Helvetica", 14, "bold"), background='#f0f0f0')
        header_label.pack(pady=5)

        # Setting up labels and entries in a frame for better alignment
        self.settings_frame = ttk.Frame(self.root, padding="5")
        self.settings_frame.pack(pady=5)

        # Inhale time label and entry
        self.breath_label = ttk.Label(self.settings_frame, text="Inhale Time (s):")
        self.breath_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.breath_entry = ttk.Entry(self.settings_frame, textvariable=self.breath_time, width=5)
        self.breath_entry.grid(row=0, column=1, padx=5, pady=5)

        # Number of Cycles
        self.cycles_label = ttk.Label(self.settings_frame, text="Number of Cycles:")
        self.cycles_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.cycles_entry = ttk.Entry(self.settings_frame, textvariable=self.cycles, width=5)
        self.cycles_entry.grid(row=1, column=1, padx=5, pady=5)

        # Checkbox to show cycle
        self.cycle_checkbox = ttk.Checkbutton(self.settings_frame, text="Show Cycle", variable=self.show_cycle)
        self.cycle_checkbox.grid(row=2, columnspan=2, pady=5)

        # Start button
        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)  # Ensure some padding around the button

    def start_timer(self):
        # Switch to countdown view
        self.current_cycle = 1
        self.show_countdown_ui()
        self.run_cycle()

    def show_countdown_ui(self):
        # Clear settings UI
        for widget in self.root.winfo_children():
            widget.pack_forget()

        # Create a frame for countdown UI
        countdown_frame = ttk.Frame(self.root, padding="10")
        countdown_frame.pack(expand=True, fill=tk.BOTH)

        # Countdown label for messages
        self.countdown_message_label = ttk.Label(countdown_frame, text="", font=("Helvetica", 16), background='#f0f0f0')
        self.countdown_message_label.pack(pady=(10, 5))

        # Countdown label for the timer
        self.countdown_label = ttk.Label(countdown_frame, text="", font=("Helvetica", 32, "bold"), background='#f0f0f0')
        self.countdown_label.pack(expand=True)

        # Stop button
        self.stop_button = ttk.Button(countdown_frame, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=20)

    def stop_timer(self):
        # Stop the current countdown and return to settings UI
        self.root.after_cancel(self.timer_id)
        self.create_settings_ui()

    def run_cycle(self):
        if self.current_cycle <= self.cycles.get():
            if self.show_cycle.get():  # Check if the checkbox is selected
                self.countdown_message_label.config(text=f"Cycle {self.current_cycle}/{self.cycles.get()}")
            else:
                self.countdown_message_label.config(text="")  # Clear the message if not showing cycle
            
            # Calculate hold and exhale times
            inhale_time = self.breath_time.get()
            hold_time = inhale_time + 1
            exhale_time = inhale_time + 2
            
            self.countdown(inhale_time, "Hold...", hold_time, "Exhale...", exhale_time)
        else:
            messagebox.showinfo("Done", "All cycles completed!")
            self.create_settings_ui()  # Return to settings menu

    def countdown(self, inhale_time, hold_text, hold_time, exhale_text, exhale_time):
        if inhale_time > 0:
            self.countdown_label.config(text=f"Inhale... {inhale_time}")
            self.timer_id = self.root.after(1000, self.countdown, inhale_time - 1, hold_text, hold_time, exhale_text, exhale_time)
            if inhale_time == 1:  # Play sound at the end of hold
                winsound.Beep(200, 100)  # Beep sound for confirmation
        elif hold_time > 0:
            self.countdown_label.config(text=f"{hold_text} {hold_time}")
            self.timer_id = self.root.after(1000, self.countdown, 0, hold_text, hold_time - 1, exhale_text, exhale_time)
            if hold_time == 1:  # Play sound at the end of hold
                winsound.Beep(200, 100)  # Beep sound for confirmation
        elif exhale_time > 0:
            self.countdown_label.config(text=f"{exhale_text} {exhale_time}", foreground="blue")
            self.timer_id = self.root.after(1000, self.countdown, 0, hold_text, 0, exhale_text, exhale_time - 1)
            if exhale_time == 1:  # Play sound at the end of exhale
                winsound.Beep(200, 100)  # Beep sound for confirmation
        else:
            if self.current_cycle < self.cycles.get():
                self.current_cycle += 1
                self.run_cycle()
            else:
                messagebox.showinfo("Done", "Breathing exercise completed!")
                self.create_settings_ui()  # Return to settings menu

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BreathingApp(root)
    root.geometry("300x300")  # Set the fixed window size
    root.resizable(False, False)  # Prevent resizing
    root.mainloop()
