# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:24:17 2024

@author: malli
"""

!pip install googletrans
!pip install python-docx
!pip install textblob
import tkinter
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from googletrans import Translator, LANGUAGES
import textblob
import os
import docx

root = Tk()
root.geometry('1080x500')
root.resizable(0, 0)
root.title("File Language Translator")
root.config(bg='#000000')

translator = Translator()

# Get supported language codes and names from googletrans
supported_languages = list(LANGUAGES.values())

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Word Documents", "*.docx")])
    if file_path:
        try:
            if file_path.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    text1.delete(1.0, END)
                    text1.insert(END, file_content)
            elif file_path.endswith('.docx'):
                doc = docx.Document(file_path)
                full_text = []
                for para in doc.paragraphs:
                    full_text.append(para.text)
                file_content = '\n'.join(full_text)
                text1.delete(1.0, END)
                text1.insert(END, file_content)
        except Exception as e:
            messagebox.showerror("File Error", f"Error opening file: {e}")

def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()  # Strip leading and trailing whitespaces
        source_lang = combo1.get()
        target_lang = combo2.get()
        
        if text_:  # Check if the source text is not empty
            translated = translator.translate(text_, src=source_lang, dest=target_lang)
            if translated:
                text2.delete(1.0, END)
                text2.insert(END, translated.text)
            else:
                messagebox.showerror("Translation Error", "Translation failed. Please try again.")
    except Exception as e:
        print(f"Translation Error: {str(e)}")
        messagebox.showerror("Translation Error", "Error occurred during translation. Please check the console for details.")

# GUI Components

# GUI Components
combo1 = ttk.Combobox(root, values=supported_languages, font="Roboto 14", state="readonly")
combo1.place(x=110, y=40)
combo1.set("English")

combo2 = ttk.Combobox(root, values=supported_languages, font="Roboto 14", state="readonly")
combo2.place(x=730, y=40)
combo2.set("Select Language")

text1 = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=30, y=150, width=400, height=300)

text2 = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=640, y=150, width=400, height=300)

translate_button = Button(root, text="Translate", font="Roboto 15 bold italic",
                          activebackground="green", cursor="hand2", bd=5,
                          bg="red", fg="white", command=translate_now)
translate_button.place(x=480, y=300)

upload_button = Button(root, text="Upload File", font="Roboto 15 bold italic",
                       activebackground="blue", cursor="hand2", bd=5,
                       bg="yellow", fg="black", command=select_file)
upload_button.place(x=480, y=200)

Label(root, text="© Made with ❤ by @Chhotu", font='arial 16', fg='#898989', bg='#000000', height='5', width='25').pack(side='bottom')

root.mainloop()
