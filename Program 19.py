from tkinter import *

def main():
    mainwin = Tk()
    mainwin.title('Program 19')
    color = 'lightblue'

    wcan = Canvas(
        mainwin,
        bg = color,
        width = 600,
        height = 800)
    
    wcan.pack()

    wcan.create_oval(100, 100, 525, 525,
                     fill = 'yellow', outline = 'black', width = 5)

    wcan.create_oval(200, 200, 300, 300,
                     fill = 'white', outline = 'black', width = 5)

    wcan.create_oval(330, 200, 430, 300,
                     fill = 'white', outline = 'black', width = 5)
    
    wcan.create_oval(240, 240, 260, 260,
                     fill = 'black')
    
    wcan.create_oval(370, 240, 390, 260,
                     fill = 'black')

    wcan.create_line(240, 380, 400, 380,
                     fill = 'red', width = 30)

    wcan.create_line(240, 450, 400, 450,
                     fill = 'black', width = 20)

    wcan.create_line(246, 450, 333, 550,
                     fill = 'black', width = 20)

    wcan.create_line(392, 450, 321, 550,
                     fill = 'black', width = 20)

    thetext = 'Pac-Man!'
    wcan.create_text(220, 55, text = thetext,
                     font = 'Courier 32', anchor = 'w')

main()
