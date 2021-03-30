from PIL import ImageGrab
import sys
import datetime


def viewErrorDialog():
    import tkinter
    from tkinter import messagebox
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror("Error", "No Image Found in Clipboard!")


def saveImageFile():
    e = datetime.datetime.now()
    filename = ("%02d-%02d-%s %02d%02d%02d" % (e.day, e.month, e.year,e.hour, e.minute, e.second))
    npwd = ""
    if len(sys.argv)>=2:
        if sys.argv[1][-1]=="\"":
            npwd+=sys.argv[1][:-1]+"\\"
        else:
            npwd+=sys.argv[1]+"\\"
    npwd+=filename+".png"
    try:        
        img = ImageGrab.grabclipboard()
        img.save(npwd, 'PNG')
    except:
        viewErrorDialog()
        sys.exit()

saveImageFile()