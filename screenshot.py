import time
import pyautogui
import tkinter as tk

def screenshot():
    imgname = int(round(time.time() * 1000))
    imgname = 'D:/Projects/Python Project/screenshots/{}.png'.format(imgname)
    # time.sleep(4)
    img = pyautogui.screenshot(imgname)
    img.show()



root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take Screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()

