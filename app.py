import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('sales_prediction_model.pkl')

# Function to make predictions
def predict_sales():
    try:
        # Get the values from the entry fields
        tv = float(entry_tv.get())
        radio = float(entry_radio.get())
        newspaper = float(entry_newspaper.get())

        # Create a DataFrame for the input data
        input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])

        # Make prediction
        predicted_sales = model.predict(input_data)[0]

        # Show the result
        messagebox.showinfo("Prediction", f"Predicted Sales: ${predicted_sales:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")

# Validation function for the entry fields
def validate_input(input_value):
    if input_value == "" or input_value.replace('.', '', 1).isdigit():
        return True
    return False

# Create the main window
window = tk.Tk()
window.title("Sales Prediction App")
window.configure(bg='#E0F7FA')  # Light baby blue background

# Define the window size
window_width = 650
window_height = 500

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position to center the window
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

# Set the window size and position
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and place the title label
title_label = tk.Label(window, text="Sales Prediction App", bg='#E0F7FA', font=('Arial', 24, 'bold'), fg='#00796B')
title_label.pack(pady=20)

# Create a frame for the input form
frame_form = tk.Frame(window, bg='#FFFFFF', padx=20, pady=20, relief=tk.RAISED, borderwidth=2)
frame_form.pack(pady=10)

# Define font styles
label_font = ('Arial', 12)
entry_font = ('Arial', 12)

# Validation command for entries
vcmd = (window.register(validate_input), '%P')

# Create and place labels and entry widgets
labels_texts = ["TV Advertising ($):", "Radio Advertising ($):", "Newspaper Advertising ($):"]
entries = []

for i, text in enumerate(labels_texts):
    tk.Label(frame_form, text=text, bg='#FFFFFF', font=label_font).grid(row=i, column=0, padx=10, pady=10, sticky='e')
    entry = tk.Entry(frame_form, font=entry_font, width=20, validate='key', validatecommand=vcmd)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entries.append(entry)

entry_tv, entry_radio, entry_newspaper = entries

# Create and place the predict button with improved styling
btn_predict = tk.Button(window, text="Predict Sales", command=predict_sales, font=('Arial', 14, 'bold'), bg='#00796B', fg='white', padx=20, pady=10, relief='raised')
btn_predict.pack(pady=20)

# Add a footer label for additional information or credits
footer_label = tk.Label(window, text="Sales Prediction Model - © 2024", bg='#E0F7FA', font=('Arial', 10), fg='#004D40')
footer_label.pack(side='bottom', pady=10)

# Add a brief instruction
instruction_label = tk.Label(window, text="Enter the advertising costs and click 'Predict Sales'.", bg='#E0F7FA', font=('Arial', 12, 'italic'), fg='#004D40')
instruction_label.pack(pady=10)

# Run the application
window.mainloop()
