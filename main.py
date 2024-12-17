from PIL import Image, ImageEnhance
import subprocess
import os
from gpiozero import Button
from random import randrange
from signal import pause

ChristmasSpirit = True

def Santa(cmc):
    directory = f"/home/fabry/momir-basic/xmas/{cmc}"
    filelist = []
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            filelist.append(item)
    selection = filelist[randrange(len(filelist))]
    image = Image.open(f"{directory}/{selection}")
    qr = Image.open(f"{directory}/qr/{selection}")
    printCard(image)
    storeQRCode(qr)

def Momir(cmc):
    directory = f"/home/fabry/momir-basic/creatures/{cmc}"
    filelist = []
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            filelist.append(item)
    selection = filelist[randrange(len(filelist))]
    image = Image.open(selection)
    printCard(image)
     
def StonehewerGiant(cmc):
    directory = f"/home/fabry/momir-basic/equipment/{randrange(cmc)}"
    filelist = []
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            filelist.append(item)
    selection = filelist[randrange(len(filelist))]
    image = Image.open(selection)
    printCard(image)

def JhoiraInstant():
    for i in range(3):
        directory = f"/home/fabry/momir-basic/instants"
        filelist = []
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)):
                filelist.append(item)
        selection = filelist[randrange(len(filelist))]
        image = Image.open(selection)
        printCard(image)
     
def JhoiraSorceries():
    for i in range(3):
        directory = f"/home/fabry/momir-basic/sorceries"
        filelist = []
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)):
                filelist.append(item)
        selection = filelist[randrange(len(filelist))]
        image = Image.open(selection)
        printCard(image)

def printCard(img):
    img = img.convert('L')
    #enhancer = ImageEnhance.Contrast(img)
    #img = enhancer.enhance(10)
    filename = "/home/fabry/momir-basic/img.png"
    img.save(filename)

    #subprocess.run(['lp', '-o', 'fit-to-page', filename])
def storeQRCode(img):
    filename = "/home/fabry/momir-basic/qr.png"
    img.save(filename)

def print_lastQRCode():
    subprocess.run(['lp', '-o', 'fit-to-page', '/home/fabry/momir-basic/qr.png'])

def b0_cb():
    print(0)
    if ChristmasSpirit:
        print_lastQRCode()
    else:
        Momir(0)

def b1_cb():
    print(1)
    if ChristmasSpirit:
        Santa(0)
    else:
        Momir(1)

def b2_cb():
    print(2)
    if ChristmasSpirit:
        Santa(1)
    else:
        Momir(2)

def b3_cb():
    print(3)
    if ChristmasSpirit:
        Santa(2)
    else:
        Momir(3)

def b4_cb():
    print(4)
    if ChristmasSpirit:
        Santa(3)
    else:
        Momir(4)

def b5_cb():
    print(5)
    if ChristmasSpirit:
        Santa(4)
    else:
        Momir(5)

def b6_cb():
    print(6)
    if ChristmasSpirit:
       Santa(5)
    else:
        Momir(6)

def b7_cb():
    print(7)
    if ChristmasSpirit:
        Santa(6)
    else:
        Momir(7)

def b8_cb():
    print(8)
    if ChristmasSpirit:
        Santa(7)
    else:
        Momir(8)

def b9_cb():
    print(9)
    if ChristmasSpirit:
        Santa(8)
    else:
        Momir(9)

def b10_cb():
    print(10)
    if ChristmasSpirit:
        Santa(9)
    else:
        Momir(10)

def b11_cb():
    print(11)
    if ChristmasSpirit:
        Santa(10)
    else:
        Momir(11)

def b12_cb():
    print(12)
    if ChristmasSpirit:
        Santa(11)
    else:
        Momir(12)

def b13_cb():
    print(13)
    if ChristmasSpirit:
        Santa(12)
    else:
        Momir(13)

def b14_cb():
    print(14)
    if ChristmasSpirit:
        Santa(randrange(13,17))
    else:
        Momir(14)

def b15_cb():
    print(15)
    if ChristmasSpirit:
        Santa(randrange(0,17))
    else:
        Momir(15)
             

button0 = Button(14, pull_up=True, bounce_time=0.1)
button1 = Button(15, pull_up=True, bounce_time=0.1)
button2 = Button(18, pull_up=True, bounce_time=0.1)
button3 = Button(23, pull_up=True, bounce_time=0.1)
button4 = Button(24, pull_up=True, bounce_time=0.1)
button5 = Button(25, pull_up=True, bounce_time=0.1)
button6 = Button(8, pull_up=True, bounce_time=0.1)
button7 = Button(7, pull_up=True, bounce_time=0.1)
button8 = Button(1, pull_up=True, bounce_time=0.1)
button9 = Button(12, pull_up=True, bounce_time=0.1)
button10 = Button(16, pull_up=True, bounce_time=0.1)
button11 = Button(20, pull_up=True, bounce_time=0.1)
button12 = Button(21, pull_up=True, bounce_time=0.1)
button13 = Button(26, pull_up=True, bounce_time=0.1)
button14 = Button(19, pull_up=True, bounce_time=0.1)
button15 = Button(13, pull_up=True, bounce_time=0.1)

button0.when_pressed = b0_cb
button1.when_pressed = b1_cb
button2.when_pressed = b2_cb
button3.when_pressed = b3_cb
button4.when_pressed = b4_cb
button5.when_pressed = b5_cb
button6.when_pressed = b6_cb
button7.when_pressed = b7_cb
button8.when_pressed = b8_cb
button9.when_pressed = b9_cb
button10.when_pressed = b10_cb
button11.when_pressed = b11_cb
button12.when_pressed = b12_cb
button13.when_pressed = b13_cb
button14.when_pressed = b14_cb
button15.when_pressed = b15_cb

pause()