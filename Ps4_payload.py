import os
import socket
import subprocess
import threading
import time
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.my_variable = 0
        self.master = master
        self.master.title("PS4 Server Tool")

        # IP address and DNS entries
        self.ip_var = StringVar()
        self.dns1_var = StringVar()
        self.dns2_var = StringVar()
        self.ip_label = Label(master, text="IP address:")
        self.ip_label.grid(row=0, column=0, sticky=W)
        self.ip_entry = Entry(master, textvariable=self.ip_var)
        self.ip_entry.grid(row=0, column=1)
        self.dns1_label = Label(master, text="DNS 1:")
        self.dns1_label.grid(row=1, column=0, sticky=W)
        self.dns1_entry = Entry(master, textvariable=self.dns1_var)
        self.dns1_entry.grid(row=1, column=1)
        self.dns2_label = Label(master, text="DNS 2:")
        self.dns2_label.grid(row=2, column=0, sticky=W)
        self.dns2_entry = Entry(master, textvariable=self.dns2_var)
        self.dns2_entry.grid(row=2, column=1)

        # File selection
        self.bin_path = StringVar()
        self.file_label = Label(master, text="Select .bin file:")
        self.file_label.grid(row=3, column=0, sticky=W)
        self.file_entry = Entry(master, textvariable=self.bin_path)
        self.file_entry.grid(row=3, column=1)
        self.browse_button = Button(master, text="Browse", command=self.select_file)
        self.browse_button.grid(row=3, column=2)

        # Timer display
        self.timer_var = StringVar()
        self.timer_label = Label(master, textvariable=self.timer_var)
        self.timer_label.grid(row=4, column=1)

        # Start button
        self.start_button = Button(master, text="Start", command=self.start_server)
        self.start_button.grid(row=5, column=0)

        # Stop button
        self.stop_button = Button(master, text="Stop", command=self.stop_server, state=DISABLED)
        self.stop_button.grid(row=5, column=1)

        # Exit button
        self.exit_button = Button(master, text="Exit", command=self.exit_program)
        self.exit_button.grid(row=5, column=2)

        # Server thread and timer
        self.server_thread = None
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.timer_running = False
        self.update_timer()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.bin_path.set(file_path)

    def start_server(self):
     self.my_variable = 0
    global start_time
    if not self.running:
        # Parse IP address and DNS entries
        ip = self.ip_var.get()
        dns1 = self.dns1_var.get()
        dns2 = self.dns2_var.get()
        if not ip or not dns1 or not dns2:
            messagebox.showerror("Error", "Please enter IP address and DNS entries")
            
        # Parse .bin file path
        bin_path = self.bin_path.get()
        if not os.path.isfile(bin_path):
            messagebox.showerror("Error", "Please select a valid .bin file")
           

        # Start server thread
        self.server_thread = threading.Thread(target=self.run_server, args=(ip, dns1, dns2, bin_path))
        self.server_thread.start()

        # Start timer thread
        self.timer_thread = threading.Thread(target=self.run_timer)
        self.timer_thread.start()

def run_server(self, ip, dns1, dns2, bin_path):
    # Generate IP address
    ip_address = ip

    # Generate DNS entries
    dns_entries = [dns1, dns2]

    # Start server
    cmd = ["python", "-m", "http.server", "80", "--bind", ip_address]
    subprocess.Popen(cmd, cwd=bin_path)

    # Force installation of the .bin file
    # Code for forcing installation of the .bin file goes here


    def start_server(self):
    # Generate IP address
     ip_address = "192.168.1.1"

    # Generate DNS entries
    dns1 = "ps4payload.local"
    dns2 = "ps4exploit.local"

    # Start server
    # Code for starting the server goes here

    def run_timer(self):
        global start_time
    # Initialize timer variables
    start_time = time.time()
    elapsed_time = 0

    while self.timer_running:
        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Format elapsed time as a string
        elapsed_time_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

        # Update timer display
        self.timer_label.config(text=elapsed_time_str)

        # Wait for one second before updating timer again
        time.sleep(1)

    def stop(self):
    # Set timer running flag to false
     self.timer_running = False

    # Stop server
    # Code for stopping the server goes here

    def quit(self):
    # Stop server
     self.stop()

    # Exit application
    self.root.destroy()
# the GUI
    gui = GUI()

#Run the GUI
    gui.root.mainloop()