import cv2
from pyzbar.pyzbar import decode
import pandas as pd
import csv
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
import threading
from sys import exit

cap = cv2.VideoCapture(0)

# Function to load student data from a CSV file using pandas
def load_student_data_from_csv(file_path):
    try:
        student_data = pd.read_csv(file_path)
        return student_data
    except Exception as e:
        print(f"Error loading student data from CSV: {e}")
        exit(1)

# Load student data from a CSV file
student_data = load_student_data_from_csv("student_data.csv")

print(student_data)

# Create a Tkinter window
root = tk.Tk()
root.title("Attendo-UI")

# Make the window wider
root.geometry("690x400")  # Adjust the width as needed

# Create a frame for displaying the scanned data
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='both', expand=True)

# Apply the "forest-dark" theme
style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")  # Make sure the theme files are available
style.theme_use('forest-dark')

# Create a text widget to display scanned data
scanned_data_text = tk.Text(frame, wrap=tk.WORD, width=80, height=15)  # Adjust width as needed
scanned_data_text.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

# Create a scrollbar for the text widget
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=scanned_data_text.yview)
scrollbar.grid(row=0, column=1, padx=5, pady=5, sticky='ns')
scanned_data_text.config(yscrollcommand=scrollbar.set)

# Dictionary to store the last entry timestamp for each barcode
last_entry_timestamp = {}

# Create a CSV file for data logging
csv_file = open("scanned_data.csv", mode='a', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Entry Time", "brcode_no","Divsion","Student Name","Rollno","RFID"])

# Function for barcode scannin
def scan_barcode():
    # Initialize variables with default values
    student_name = ""
    division = ""
    rfid = ""
    rollno = ""
    # Initialize the camera when the application starts
     # Initialize the camera outside the scanning function

    # Function to start scanning
    def start_scanning():
        # Capture a few frames to "warm up" the camera (discard these frames)
        for _ in range(5):
            cap.read()

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply histogram equalization to the grayscale frame
        equalized_frame = cv2.equalizeHist(gray_frame)

        # Decode barcodes in the frame
        decoded_objects = decode(gray_frame)

        # Loop through the detected barcodes
        for obj in decoded_objects:
            # Extract the barcode data
            barcode_data = obj.data.decode('utf-8')

            # Check if the barcode has been scanned within the last 3 minutes
            if barcode_data in last_entry_timestamp:
                last_timestamp = last_entry_timestamp[barcode_data]
                current_timestamp = datetime.now()
                time_difference = current_timestamp - last_timestamp
                if time_difference < timedelta(seconds=180):
                    continue  # Skip this entry

            # Look up the student's name using pandas
            student_info = student_data[student_data['brcode_no'] == str(barcode_data)]
            if not student_info.empty:
                student_name = student_info['student_name'].values[0]
                division = student_info['Division'].values[0]  # Extract Division from student_data
                rfid = student_info['RFID'].values[0]  # Extract RFID from student_data
                rollno=student_info['RollNo'].values[0]  #Extract out roll_no


            entry_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            scanned_data_text.insert(tk.END, f"{entry_time}: Student Name: {student_name}\n")

            # Write the data to the CSV file
            csv_writer.writerow([entry_time, barcode_data,division, student_name,rollno,rfid])
            csv_file.flush()  # Flush the buffer to write immediately

            # Update the last entry timestamp for this barcode
            last_entry_timestamp[barcode_data] = datetime.now()

        # Display the frame
        cv2.imshow("bcodeScn_window", frame)

        # Exit the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

# Function for periodic GUI updates
def update_gui():
    root.update()
    root.after(1000, update_gui)

# Create a button to start scanning
scan_button = ttk.Button(root, text="Start Scanning", command=lambda: threading.Thread(target=scan_barcode).start())
scan_button.pack(padx=10, pady=10)

# Start periodic GUI updates
root.after(1000, update_gui)

# Create a label at the bottom for "Created and curated with ❤️"
made_with_heart = ttk.Label(root, text="Created and Curated with ❤️ ")
made_with_heart.pack(side="bottom", pady=5)

# Create a function to close the CSV file and the Tkinter window
# Create a function to close the CSV file and the Tkinter window
def close_window():
    # Close the CSV file
    csv_file.close()
    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close the OpenCV window
    root.destroy()

# Create a button to close the window
close_button = ttk.Button(root, text="Close", command=close_window)
close_button.pack(padx=10, pady=10)

root.mainloop()
