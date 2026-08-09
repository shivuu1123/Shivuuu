import pypdf
import pyttsx3
from tkinter.filedialog import askopenfilename
book = askopenfilename()
if book:  
    pdfreader = pypdf.PdfReader(book)
    pages = len(pdfreader.pages)
    player = pyttsx3.init()

    for num in range(0, pages):
        page = pdfreader.pages[num] #
        text = page.extract_text()  
        
        if text: 
            player.say(text)
            player.runAndWait()
      