import tkinter as tk
from tkinter import messagebox

def display_text():
    entered_text = text_entry.get("1.0", tk.END)
    output_label.config(text=entered_text)

# Create the main window
root = tk.Tk()
root.title("Fake News Detection System")
root.geometry("700x500")  # Set the window size to 500x700

# Create a label for the entry
entry_label = tk.Label(root, text="Enter the Article for Analysis:")
entry_label.pack()

# Create a text entry widget
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Create a button that will display the entered text
display_button = tk.Button(root, text="Display Text", command=display_text)
display_button.pack()

# Create a label for the output
output_label = tk.Label(root, text="", wraplength=400)
output_label.pack()

# Run the main loop
root.mainloop()
