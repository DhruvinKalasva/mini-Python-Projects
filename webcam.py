import cv2
import tkinter as tk
import time


def CaptureImage():
    imgcapture = cv2.VideoCapture(0)
    result = True

    while(result):

        imgname = int(round(time.time() * 1000))
        imgname = 'D:/Projects/Python Project/WebcamImages/{}.jpg'.format(imgname)

        ret , frame = imgcapture.read()
        cv2.imwrite(imgname,frame)
        result = False
        print("Image Captured!")

    imgcapture.release()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Capture the Image",
    command=CaptureImage
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()