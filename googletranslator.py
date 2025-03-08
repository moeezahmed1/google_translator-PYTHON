from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from textblob import TextBlob

root = Tk()
root.title("Google Translator")
root.geometry('1080x400')
translator = googletrans.Translator()

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    global language
    try: 
        text_ = text1.get(1.0, END).strip()  # Use .strip() to remove extra whitespace
        if not text_:  # If the text box is empty, show a warning
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        c2 = combo1.get()  # Source language
        c3 = combo2.get()  # Target language

        # Detect the language of the input text
        detected_lang = translator.detect(text_).lang

        # Create a TextBlob object
        words = TextBlob(text_)

        # Find the target language code
        target_lang_code = None
        for i, j in language.items():
            if j == c3:
                target_lang_code = i
                break

        if not target_lang_code:
            messagebox.showerror("Language Error", "Invalid target language selected.")
            return

        # Perform the translation
        translated = words.translate(from_lang=detected_lang, to=target_lang_code)

        # Display the translated text
        text2.delete(1.0, END)
        text2.insert(END, translated)

    except Exception as e:
        messagebox.showerror('Google_Trans', f'An error occurred: {str(e)}')

# Load the icon
try:
    image_icon = PhotoImage(file="googletranslator.png")
    root.iconphoto(False, image_icon)
except Exception as e:
    print(f"Icon loading error: {e}")

# Load the arrow image
try:
    arrow_image = PhotoImage(file='arrow1.png')
    image_label = Label(root, image=arrow_image, width=150)
    image_label.place(x=460, y=50)
except Exception as e:
    print(f"Arrow image loading error: {e}")

# Language setup
language = googletrans.LANGUAGES
languageV = list(language.values())

# First language combo box
combo1 = ttk.Combobox(root, values=languageV, font='Roboto 14', state='readonly')
combo1.place(x=110, y=20)
combo1.set('English')

# Label for the first text box
label1 = Label(root, text="English", font='Segoe 30 bold', bg='white', width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Frame and text box for the input text
f = Frame(root, bg='Black', bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font='Roboto 20', bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side='right', fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Second language combo box
combo2 = ttk.Combobox(root, values=languageV, font='Roboto 14', state='readonly')
combo2.place(x=730, y=20)
combo2.set('Select Language')

# Label for the second text box
label2 = Label(root, text="English", font='Segoe 30 bold', bg='white', width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Frame and text box for the translated text
f1 = Frame(root, bg='Black', bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font='Roboto 20', bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side='right', fill='y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text='Translate', font='Roboto 15 bold italic',
                  activebackground='grey', cursor='hand2', bd=5,
                  bg='red', fg='white', command=translate_now)
translate.place(x=480, y=250)

# Start the label update loop
label_change()

# Configure the root window
root.configure(bg='white')
root.mainloop()