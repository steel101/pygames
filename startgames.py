import sys
import os
from tkinter import *

window=Tk()

window.title("start Python Games")
window.geometry('550x200')


def runpong():
    os.chdir('pong')
    os.system('python ./main.py')
    os.chdir('..')
def runBerzerk():
    os.chdir('Berzerk')
    os.system('C:\Python27\python.exe .\pyberzerk.py')
    os.chdir('..')
def runpacman():
    os.chdir('Pacman')
    os.system('python ./run.py')
    os.chdir('..')
def runtron():
    os.chdir('tron')
    os.system('python ./tron.py')
    os.chdir('..')
def runflippy():
    os.chdir('flippy')
    os.system('python ./flippy.py')
    os.chdir('..')
def runfourinarow():
    os.chdir('fourinarow')
    os.system('python ./fourinarow.py')
    os.chdir('..')
def rungemgem():
    os.chdir('gemgem')
    os.system('python ./gemgem.py')
    os.chdir('..')
def runmemorypuzzle():
    os.chdir('memorypuzzle')
    os.system('python ./memorypuzzle.py')
    os.chdir('..')
def runmemorypuzzle_obfuscated():
    os.chdir('memorypuzzle_obfuscated')
    os.system('python ./memorypuzzle_obfuscated.py')
    os.chdir('..')
def runpentomino():
    os.chdir('pentomino')
    os.system('python ./pentomino.py')
    os.chdir('..')
def runsimulate():
    os.chdir('simulate')
    os.system('python ./simulate.py')
    os.chdir('..')
def runslidepuzzle():
    os.chdir('slidepuzzle')
    os.system('python ./slidepuzzle.py')
    os.chdir('..')
def runstarpusher():
    os.chdir('starpusher')
    os.system('python ./starpusher.py')
    os.chdir('..')
def runtetris():
    os.chdir('tetris')
    os.system('python ./tetris.py')
    os.chdir('..')
def runtictactoe():
    os.chdir('tictactoe')
    os.system('python ./tictactoe.py')
    os.chdir('..')
def runsnake():
    os.system('python ./snake.py')
def runSpaceInvaders():
    os.chdir('Space-Invaders')
    os.system('python ./Space-Invaders.py')
    os.chdir('..')


btn = Button(window, text="flippy", bg="black", fg="white",command=runflippy)
btn.grid(column=0, row=0)

btn = Button(window, text="pacman", bg="black", fg="white",command=runpacman)
btn.grid(column=1, row=0)

btn = Button(window, text="fourinarow", bg="black", fg="white",command=runfourinarow)
btn.grid(column=2, row=0)

btn = Button(window, text="gemgem", bg="black", fg="white",command=rungemgem)
btn.grid(column=3, row=0)

btn = Button(window, text="memorypuzzle", bg="black", fg="white",command=runmemorypuzzle)
btn.grid(column=0, row=5)

btn = Button(window, text="memorypuzzle_obfuscated", bg="black", fg="white",command=runmemorypuzzle_obfuscated)
btn.grid(column=1, row=5)

btn = Button(window, text="pentomino", bg="black", fg="white",command=runpentomino)
btn.grid(column=2, row=5)

btn = Button(window, text="simulate", bg="black", fg="white",command=runsimulate)
btn.grid(column=3, row=5)


btn = Button(window, text="slidepuzzle", bg="black", fg="white",command=runslidepuzzle)
btn.grid(column=0, row=10)

btn = Button(window, text="starpusher", bg="black", fg="white",command=runstarpusher)
btn.grid(column=1, row=10)

btn = Button(window, text="tetris", bg="black", fg="white",command=runtetris)
btn.grid(column=2, row=10)

btn = Button(window, text="tictactoe", bg="black", fg="white",command=runtictactoe)
btn.grid(column=3, row=10)

btn = Button(window, text="snake", bg="black", fg="white",command=runsnake)
btn.grid(column=1, row=20)

btn = Button(window, text="Space-Invaders", bg="black", fg="white",command=runSpaceInvaders)
btn.grid(column=0, row=20)

btn = Button(window, text="Pong", bg="black", fg="white",command
=runpong)
btn.grid(column=2, row=20)

btn = Button(window, text="tron", bg="black", fg="white",command=runtron)
btn.grid(column=3, row=20)


btn = Button(window, text="berzerk", bg="black", fg="white",command=runBerzerk)
btn.grid(column=0, row=30)

window.mainloop()