from tkinter import *
import numpy as np
from perceptron import Perceptron

root = Tk()

root.geometry('250x350')
root.title("Perceptron")

canvas = Canvas(root, height=250, width=250, bg="grey")

rectColors = [[0 for x in range(5)] for x in range(5)] # Tablica z 0 i 1, gdzie 0 to szary, a 1 to zielony

perceptrons = []
for _ in range(10):
    perceptrons.append(Perceptron(5 * 5))

algorithm = ""


# Kliknięcie w piksel
def clicked(eventorigin):
    x = eventorigin.x
    y = eventorigin.y
    x = x / 50
    x = int(x)
    y = y / 50
    y = int(y)
    if rectColors[x][y] == 0:
        canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="green", tags="clicked")
        rectColors[x][y] = 1
    else:
        canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")
        rectColors[x][y] = 0


# Wszystkie piksele na szaro
def resetCanvas():
    for x in range(5):
        for y in range(5):
            canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey", tags="clicked")
            rectColors[x][y] = 0


resetCanvas()

canvas.tag_bind("clicked", "<Button-1>", clicked)

canvas.pack()

number = [[] for _ in range(10)]
number[0] = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]
number[1] = [
    [0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0]
]
number[2] = [
    [0.0, 1.0, 1.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0, 0.0, 0.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]
number[3] = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [0.0, 0.0, 0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 1.0, 1.0],
    [0.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]
number[4] = [
    [1.0, 0.0, 0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0, 1.0, 0.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0]
]
number[5] = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 0.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [0.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]
number[6] = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 0.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]
number[7] = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0, 0.0, 0.0]
]
number[8] = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]
number[9] = [
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0],
    [0.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0]
]

numbers = [np.ravel(n) for n in number]


# Rysowanie klikniętej cyfry
def makeNumber(num):
    resetCanvas()
    p = 0
    for y in range(5):
        for x in range(5):
            if numbers[num][p] == 1:
                canvas.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="green", tags="clicked")
                rectColors[x][y] = 1
            p = p + 1


def b0Clicked():
    makeNumber(0)


def b1Clicked():
    makeNumber(1)


def b2Clicked():
    makeNumber(2)


def b3Clicked():
    makeNumber(3)


def b4Clicked():
    makeNumber(4)


def b5Clicked():
    makeNumber(5)


def b6Clicked():
    makeNumber(6)


def b7Clicked():
    makeNumber(7)


def b8Clicked():
    makeNumber(8)


def b9Clicked():
    makeNumber(9)


b0 = Button(root, text="0", command=b0Clicked).place(x=0, y=255, width=50, height=25)
b1 = Button(root, text="1", command=b1Clicked).place(x=50, y=255, width=50, height=25)
b2 = Button(root, text="2", command=b2Clicked).place(x=100, y=255, width=50, height=25)
b3 = Button(root, text="3", command=b3Clicked).place(x=150, y=255, width=50, height=25)
b4 = Button(root, text="4", command=b4Clicked).place(x=200, y=255, width=50, height=25)
b5 = Button(root, text="5", command=b5Clicked).place(x=0, y=280, width=50, height=25)
b6 = Button(root, text="6", command=b6Clicked).place(x=50, y=280, width=50, height=25)
b7 = Button(root, text="7", command=b7Clicked).place(x=100, y=280, width=50, height=25)
b8 = Button(root, text="8", command=b8Clicked).place(x=150, y=280, width=50, height=25)
b9 = Button(root, text="9", command=b9Clicked).place(x=200, y=280, width=50, height=25)


# Przycisk resetuje piksele
def cleanClicked():
    resetCanvas()
    varOut.set("OUT")


# Uczenie algorytmem SPLA
def learnClicked():
    global algorithm
    algorithm = "SPLA"
    for i in range(10):
        labels = np.zeros(10)
        labels[i] = 1
        training_inputs = [np.ravel(n) for n in number]
        perceptrons[i].train(training_inputs, labels)


# Uczenie algorytmem PLA
def learnPLAClicked():
    global algorithm
    algorithm = "PLA"
    for i in range(10):
        labels = np.zeros(10)
        labels[i] = 1
        training_inputs = [np.ravel(n) for n in number]
        perceptrons[i].trainPLA(training_inputs, labels)


# Uczenie algorytmem RPLA
def learnRPLAClicked():
    global algorithm
    algorithm = "RPLA"
    for i in range(10):
        labels = np.zeros(10)
        labels[i] = 1
        training_inputs = [np.ravel(n) for n in number]
        perceptrons[i].trainRPLA(training_inputs, labels)


# Check sprawdza narysowaną cyfrę
def check(algorithm):
    global rectColors
    inputs = [0 for x in range(25)]
    j = 0
    for x in range(5):
        for y in range(5):
            inputs[j] = rectColors[y][x]
            j = j + 1
    for x in range(10):
        if algorithm == "SPLA":
            if perceptrons[x].output(inputs) == 1:
                varOut.set(x)
                break
            else:
                varOut.set("null")
        elif algorithm == "PLA":
            if perceptrons[x].outputPLA(inputs) == 1:
                varOut.set(x)
                break
            else:
                varOut.set("null")
        elif algorithm == "RPLA":
            if perceptrons[x].outputRPLA(inputs) == 1:
                varOut.set(x)
                break
            else:
                varOut.set("null")



def checkClicked():
    global algorithm
    check(algorithm)


# Resetowanie perceptronów
def resetPerceptrons():
    global perceptrons
    perceptrons = []
    for _ in range(10):
        perceptrons.append(Perceptron(5 * 5))


buttonClean = Button(root, text="Clean", command=cleanClicked).place(x=0, y=305, width=60, height=25)
buttonLearn = Button(root, text="Learn", command=learnClicked).place(x=60, y=305, width=60, height=25)
buttonCheck = Button(root, text="Check", command=checkClicked).place(x=120, y=305, width=60, height=25)
buttonLearnPLA = Button(root, text="LearnPLA", command=learnPLAClicked).place(x=0, y=330, width=80, height=25)
buttonLearnRPLA = Button(root, text="LearnRPLA", command=learnRPLAClicked).place(x=80, y=330, width=90, height=25)
buttonResetPerceptrons = Button(root, text="resetPerc", command=resetPerceptrons).place(x=170, y=330, width=80, height=25)

varOut = StringVar()
label = Label(root, textvariable=varOut, relief=RAISED).place(x=180, y=305, width=60, height=25)
varOut.set("OUT")

root.mainloop()
