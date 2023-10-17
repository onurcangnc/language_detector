import tkinter as tk
from tkinter import scrolledtext
from langdetect import detect_langs, DetectorFactory

# Set the seed to ensure consistent language detection results
DetectorFactory.seed = 0

def detect_language():
    input_text = text_entry.get("1.0", "end-1c")  # Get text from the input field
    detected_languages = detect_langs(input_text)
    result_text.config(state="normal")  # Enable text widget for editing
    result_text.delete("1.0", "end")  # Clear previous results
    for language in detected_languages:
        formatted_prob = "{:.2f}".format(language.prob * 100)  # Format as a percentage
        result_text.insert("end", f"{language.lang}: {formatted_prob}%\n")
    result_text.config(state="disabled")  # Disable text widget

# Create the main window
window = tk.Tk()
window.title("Language Detection")

# Create and configure the text input field
text_label = tk.Label(window, text="Enter Text:")
text_label.pack()
text_entry = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
text_entry.pack()

# Create the Detect button
detect_button = tk.Button(window, text="Detect Language", command=detect_language)
detect_button.pack()

# Create and configure the result text widget
result_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
result_text.pack()
result_text.config(state="disabled")  # Disable text widget initially

window.mainloop()
