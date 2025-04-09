import tkinter as tk
import time
from datetime import timedelta

class TimeTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Time Tracker")
        self.root.geometry("350x300")
        self.root.resizable(False, False)
        
        # Initialize timer variables
        self.first_timer_seconds = 0
        self.first_timer_running = True
        
        self.second_timer_seconds = 0
        self.second_timer_running = False
        
        # First timer section
        self.timer1_frame = tk.LabelFrame(root, text="Idle Time", padx=10, pady=10)
        self.timer1_frame.pack(fill="both", expand=True, padx=10, pady=(10, 5))
        
        self.time1_label = tk.Label(
            self.timer1_frame, 
            text="00:00:00", 
            font=("Arial", 24, "bold")
        )
        self.time1_label.pack(pady=5)
        
        self.status1_label = tk.Label(
            self.timer1_frame,
            text="RUNNING",
            fg="green",
            font=("Arial", 10, "bold")
        )
        self.status1_label.pack()
        
        # Second timer section
        self.timer2_frame = tk.LabelFrame(root, text="Work Time", padx=10, pady=10)
        self.timer2_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        
        self.time2_label = tk.Label(
            self.timer2_frame, 
            text="00:00:00", 
            font=("Arial", 24, "bold")
        )
        self.time2_label.pack(pady=5)
        
        self.status2_label = tk.Label(
            self.timer2_frame,
            text="PAUSED",
            fg="red",
            font=("Arial", 10, "bold")
        )
        self.status2_label.pack()
        
        # Control buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)
        
        self.toggle_button = tk.Button(
            self.button_frame,
            text="Switch to Work",
            command=self.toggle_active_timer,
            width=20,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.toggle_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(
            self.button_frame,
            text="Reset Both Timers",
            command=self.reset_timers,
            width=20,
            height=2,
            font=("Arial", 10, "bold")
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Start updating the timers
        self.update_timer()
    
    def format_time(self, seconds):
        """Format time in HH:MM:SS format"""
        return str(timedelta(seconds=seconds))
    
    def update_timer(self):
        # Update seconds counters
        if self.first_timer_running:
            self.first_timer_seconds += 1
        
        if self.second_timer_running:
            self.second_timer_seconds += 1
        
        # Update displays
        formatted_time1 = self.format_time(self.first_timer_seconds)
        self.time1_label.config(text=formatted_time1)
        
        formatted_time2 = self.format_time(self.second_timer_seconds)
        self.time2_label.config(text=formatted_time2)
        
        # Schedule the next update (1 second interval)
        self.root.after(1000, self.update_timer)
    
    def toggle_active_timer(self):
        if self.first_timer_running:
            # Pause Idle timer
            self.first_timer_running = False
            self.status1_label.config(text="PAUSED", fg="red")
            
            # Start Work timer
            self.second_timer_running = True
            self.status2_label.config(text="RUNNING", fg="green")
            self.toggle_button.config(text="Switch to Idle")
        else:
            # Pause Work timer
            self.second_timer_running = False
            self.status2_label.config(text="PAUSED", fg="red")
            
            # Start Idle timer
            self.first_timer_running = True
            self.status1_label.config(text="RUNNING", fg="green")
            self.toggle_button.config(text="Switch to Work")
    
    def reset_timers(self):
        # Reset both timers
        self.first_timer_seconds = 0
        self.first_timer_running = True
        self.status1_label.config(text="RUNNING", fg="green")
        
        self.second_timer_seconds = 0
        self.second_timer_running = False
        self.status2_label.config(text="PAUSED", fg="red")
        
        # Reset toggle button text
        self.toggle_button.config(text="Switch to Work")
        
        # Update displays immediately
        self.time1_label.config(text="00:00:00")
        self.time2_label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTracker(root)
    root.mainloop()
