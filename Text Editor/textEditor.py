import tkinter as tk
from tkinter import filedialog , messagebox

def open_file():
    try:
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
                return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file: # "r" is read mode for the input file
            text = input_file.read()
            txt_edit.insert(tk.END, text) #to add the text in the end of the window
            window.title(f"Almadrsa Text Editor - {filepath}") #update window title and add the opened file path  
    except Exception as e:
        messagebox.showerror("Open File", f"Failed to open file\n{e}")


def save_file():
    try:
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not filepath:
            return
        with open(filepath, "w") as output_file: #"w" is the write mode
            text = txt_edit.get(1.0, tk.END) #get the text from line 1 character 0
            output_file.write(text)
        window.title(f"Almadrsa Text Editor - {filepath}")
    except Exception as e:
        messagebox.showerror("Save File", f"Failed to save file\n{e}")

window = tk.Tk()
txt_edit = tk.Text(window)
window.title("Almadrsa Text Editor")
window.rowconfigure(0,minsize=600)
window.columnconfigure(1,minsize=800)

frame_buttons = tk.Frame(window,relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save File",command=save_file)

btn_open.grid(column=0 , row=0 , sticky="ew" , padx=5 , pady=5)
btn_save.grid(column=0 , row=1 , sticky="ew" , padx=5 , pady=5)

frame_buttons.grid(column=0 , row=0 , sticky="ns")
txt_edit.grid(column=1 , row=0 , sticky="nsew")

window.mainloop()
