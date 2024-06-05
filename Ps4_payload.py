import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading
import socket

class Ps4Payload:
    def __init__(self, root):
        self.root = root
        self.root.title("PS4 Payload Injector")
        self.payload_path = tk.StringVar()
        self.destination_ip = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Payload Path:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.payload_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_payload).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(self.root, text="Destination IP:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.root, textvariable=self.destination_ip, width=50).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Send Payload", command=self.send_payload).grid(row=2, column=0, columnspan=3, pady=20)

    def browse_payload(self):
        file_path = filedialog.askopenfilename(filetypes=[("Payload Files", "*.bin")])
        if file_path:
            self.payload_path.set(file_path)

    def send_payload(self):
        payload = self.payload_path.get()
        ip = self.destination_ip.get()

        if not payload:
            messagebox.showerror("Error", "Please select a payload file.")
            return

        if not ip:
            messagebox.showerror("Error", "Please enter the destination IP.")
            return

        threading.Thread(target=self.transfer_payload, args=(payload, ip)).start()

    def transfer_payload(self, payload, ip):
        try:
            with open(payload, "rb") as payload_file:
                payload_data = payload_file.read()
            
            payload_size = len(payload_data)
            payload_size_bytes = payload_size.to_bytes(4, byteorder='big')

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, 9999))
                s.sendall(payload_size_bytes + payload_data)

                response = s.recv(1024)
                print(response.decode())
                messagebox.showinfo("Success", f"Payload {os.path.basename(payload)} sent to {ip}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send payload: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Ps4Payload(root)
    root.mainloop()
