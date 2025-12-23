import tkinter as tk
from tkinter import messagebox
import sys
import random
import string
import threading
import time

class FakeRansomware:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OOPS! Your files have been encrypted!")
        self.root.configure(bg='#8B0000')
        
        # Make fullscreen and prevent closing easily
        self.root.attributes('-fullscreen', True)
        # Removed topmost to allow Task Manager to appear
        
        # Disable window close button - ONLY Ctrl+Shift+Q can close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing_attempt)
        
        # Secret key combination to close (Ctrl+Shift+Q)
        self.root.bind('<Control-Shift-Q>', self.close_program)
        
        # Generate fake Bitcoin address
        self.btc_address = self.generate_fake_btc()
        
        # Timer variables (72 hours = 259200 seconds)
        self.time_remaining = 72 * 60 * 60  # 72 hours in seconds
        self.timer_running = True
        
        self.setup_ui()
        
    def generate_fake_btc(self):
        """Generate a fake Bitcoin address"""
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return '1' + ''.join(random.choices(chars, k=33))
    
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#8B0000')
        main_frame.pack(expand=True, fill='both', padx=50, pady=50)
        
        # Skull icon (using text)
        skull_label = tk.Label(main_frame, text="☠", font=('Arial', 120), 
                              fg='white', bg='#8B0000')
        skull_label.pack(pady=20)
        
        # Main title
        title = tk.Label(main_frame, text="OOPS! YOUR FILES HAVE BEEN ENCRYPTED!", 
                        font=('Arial', 28, 'bold'), fg='white', bg='#8B0000')
        title.pack(pady=10)
        
        # Warning message
        warning_text = """
        All your important files have been encrypted!
        
        Your documents, photos, videos, databases and other files
        are no longer accessible because they have been encrypted.
        
        Nobody can recover your files without our decryption service.
        """
        warning = tk.Label(main_frame, text=warning_text, 
                          font=('Arial', 14), fg='white', bg='#8B0000',
                          justify='center')
        warning.pack(pady=20)
        
        # Payment section
        payment_frame = tk.Frame(main_frame, bg='black', bd=3, relief='solid')
        payment_frame.pack(pady=20, padx=50, fill='x')
        
        payment_title = tk.Label(payment_frame, text="HOW TO DECRYPT YOUR FILES?", 
                                font=('Arial', 18, 'bold'), fg='red', bg='black')
        payment_title.pack(pady=10)
        
        payment_text = f"""
        1. Send $50,000 in Bitcoin to this address:
        
        {self.btc_address}
        
        2. After payment, send your unique ID to: decrypt@llgzionvoara.org
        
        3. You will receive the decryption key within 24 hours
        
        WARNING: You have 72 hours to pay or the price will double!
        """
        payment_info = tk.Label(payment_frame, text=payment_text, 
                               font=('Courier', 12), fg='yellow', bg='black',
                               justify='left')
        payment_info.pack(pady=10, padx=20)
        
        # Timer (real countdown)
        self.timer_label = tk.Label(main_frame, text="Time remaining: 72:00:00", 
                              font=('Arial', 16, 'bold'), fg='yellow', bg='#8B0000')
        self.timer_label.pack(pady=10)
        
        # Your unique ID
        unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        id_label = tk.Label(main_frame, text=f"Your Unique ID: {unique_id}", 
                           font=('Courier', 14), fg='white', bg='#8B0000')
        id_label.pack(pady=10)
        
        # Hidden exit instruction
        exit_info = tk.Label(main_frame, 
                            text="[Security Awareness Test - Press Ctrl+Shift+Q to exit]", 
                            font=('Arial', 10), fg='#8B0000', bg='#8B0000')
        exit_info.pack(side='bottom', pady=5)
        
    def update_timer(self):
        """Update the countdown timer every second"""
        while self.timer_running and self.time_remaining > 0:
            hours = self.time_remaining // 3600
            minutes = (self.time_remaining % 3600) // 60
            seconds = self.time_remaining % 60
            
            time_str = f"Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}"
            
            # Update the label in the main thread
            try:
                self.timer_label.config(text=time_str)
            except:
                break
            
            time.sleep(1)
            self.time_remaining -= 1
        
        # When timer reaches 0
        if self.time_remaining <= 0 and self.timer_running:
            try:
                self.timer_label.config(text="TIME'S UP! Price doubled: $100,000", fg='red')
            except:
                pass
    
    def on_closing_attempt(self):
        """Prevent closing through normal methods - user must use Ctrl+Shift+Q"""
        messagebox.showwarning("Access Denied", 
                              "You cannot close this window!\n\n"
                              "Your files are encrypted and will remain inaccessible.")
    
    def close_program(self, event=None):
        """Close the program with secret key combination"""
        result = messagebox.askyesno("Exit Fake Ransomware", 
                                     "This was a SECURITY AWARENESS TEST!\n\n"
                                     "No files have been encrypted or damaged.\n\n"
                                     "Are you sure you want to exit?")
        if result:
            self.timer_running = False
            self.root.destroy()
            sys.exit(0)
    
    def run(self):
        # Start the timer in a separate thread
        timer_thread = threading.Thread(target=self.update_timer, daemon=True)
        timer_thread.start()
        
        self.root.mainloop()

if __name__ == "__main__":
    app = FakeRansomware()
    app.run()
