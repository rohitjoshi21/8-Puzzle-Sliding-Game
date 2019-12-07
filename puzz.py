#!/usr/bin/python3

from tkinter import *
import random
import time

ROOT_DIR = 'photos/'
IMAGE_FORMAT = 'img%s.png'


class Main:
    def __init__(self):
        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=260, height=260)
        self.canvas.pack()
        self.text = self.canvas.create_text(130, 130, text="Go to hell", font=(
            "Times", 40), fill="orange", state="hidden")
        self.orgimages = []
        self.images = []
        self.canvas.bind_all('<Key>', self.onkeypressed)

    def start(self):
        self.load_image()
        self.shuffleImg()
        self.tk.update()

    def shuffleImg(self):
        r = random.randint(50, 100)
        a = ["Right", "Up", "Left", "Down"]
        fixed = [4, 3, 3, 4, 2, 2, 1, 3, 1, 3, 4]
        for z in fixed:
            self.change(z)
        for i in range(r):
            random.shuffle(a)
            self.change(a[1])

    def change(self, a):
        i = self.images.index(self.blank)
        if a == "space":
            self.shuffleImg()
        if i != 0 and i != 3 and i != 6 and (a == "Right" or a == 4):
            self.images[i] = self.images[i - 1]
            self.images[i - 1] = self.blank
        if i != 2 and i != 5 and i != 8 and (a == "Left" or a == 1):
            self.images[i] = self.images[i + 1]
            self.images[i + 1] = self.blank
        if i != 0 and i != 1 and i != 2 and (a == "Down" or a == 3):
            self.images[i] = self.images[i - 3]
            self.images[i - 3] = self.blank
        if i != 6 and i != 7 and i != 8 and (a == "Up" or a == 2):
            self.images[i] = self.images[i + 3]
            self.images[i + 3] = self.blank
        self.draw_image()
        self.checkForWin()

    def draw_image(self):
        i = 0
        yp = 0
        for y in range(0, 3):
            xp = 5
            yp += 5
            for x in range(0, 3):
                self.canvas.create_image(
                    x * 80 + xp, y * 80 + yp, image=self.images[i], anchor='nw')
                i += 1
                xp += 5

    def load_image(self):
        for i in range(8):
            img = PhotoImage(file=ROOT_DIR + IMAGE_FORMAT % i)
            self.images.append(img)
            self.orgimages.append(img)
        self.blank = PhotoImage(file=ROOT_DIR + IMAGE_FORMAT % '9')
        self.images.append(self.blank)
        self.orgimages.append(self.blank)

    def onkeypressed(self, evt):
        key = evt.keysym
        self.change(key)

    def checkForWin(self):
        if self.images == self.orgimages:
            self.canvas.itemconfig(self.text, state="normal")
            self.canvas.tag_raise(self.text, "all")
        else:
            self.canvas.itemconfig(self.text, state="hidden")


g = Main()
g.start()
g.tk.mainloop()
