from tkinter import *

def calculate(kelvin_entry, celsius_entry, fahrenheit_entry, error_entry):
    kelvin_value = kelvin_entry.get()

    kelvin_entry.configure(bg='white')
    error_entry.configure(bg='white')
    error_entry.delete(0, END)

    if kelvin_value == '':
        kelvin_entry.configure(bg = 'red')
        error_entry.configure(bg = 'red')
        error_entry.insert(0, "Error. Please enter a positive number. Can't be blank.")
        return

    test_value = kelvin_value.replace('.', '', 1)
    if not test_value.isdigit():
        kelvin_entry.configure(bg = 'red')
        error_entry.configure(bg = 'red')
        error_entry.insert(0, 'Error. Please enter a postive number.')
        return

    kelvin = float(kelvin_value)

    if kelvin <= 0:
        kelvin_entry.configure(bg = 'red')
        error_entry.configure(bg = 'red')
        error_entry.insert(0, 'Error. Must be greater than 0.')
        return

    celsius = kelvin - 273.15
    fahrenheit = (9 / 5) * (kelvin - 273) + 32

    celsius_entry.delete(0, END)
    celsius_entry.insert(0, str(celsius))

    fahrenheit_entry.delete(0, END)
    fahrenheit_entry.insert(0, str(fahrenheit))

def clear_all(kelvin_entry, celsius_entry, fahrenheit_entry, error_entry):
    kelvin_entry.delete(0, END)
    celsius_entry.delete(0, END)
    fahrenheit_entry.delete(0, END)
    error_entry.delete(0, END)

    kelvin_entry.configure(bg = 'white')
    error_entry.configure(bg = 'white')

def main():
    win = Tk()
    win.geometry('600x350')
    win.title('Program 18')
    win.configure(bg = 'lightgrey')

    title = Label(win, text = 'Temperature Conversion', font = ('Arial Bold', 20), fg = 'darkblue', bg = 'lightgrey')
    title.place(x = 150, y = 20)

    kelvin_label = Label(win, text = 'Kelvin:', font = ('Arial Bold', 14), bg = 'lightgrey', fg = 'black')
    kelvin_label.place(x = 50, y = 80)
    kelvin_entry = Entry(win, font=('Arial', 14))
    kelvin_entry.place(x = 200, y = 80, width = 200)

    celsius_label = Label(win, text = 'Celsius:', font = ('Arial Bold', 14), bg = 'lightgrey', fg = 'black')
    celsius_label.place(x = 50, y = 120)
    celsius_entry = Entry(win, font = ('Arial', 14))
    celsius_entry.place(x = 200, y = 120, width = 200)

    fahrenheit_label = Label(win, text = 'Fahrenheit:', font = ('Arial Bold', 14), bg = 'lightgrey', fg = 'black')
    fahrenheit_label.place(x = 50, y = 160)
    fahrenheit_entry = Entry(win, font = ('Arial', 14))
    fahrenheit_entry.place(x = 200, y = 160, width = 200)

    error_entry = Entry(win, font = ('Arial', 12))
    error_entry.place(x = 50, y = 210, width = 400)

    calculate_btn = Button(win, text = 'Calculate', font = ('Arial Bold', 14),
                           command = lambda: calculate(kelvin_entry, celsius_entry, fahrenheit_entry, error_entry))
    calculate_btn.place(x = 150, y = 260)

    clear_btn = Button(win, text = 'Clear', font = ('Arial Bold', 14),
                       command = lambda: clear_all(kelvin_entry, celsius_entry, fahrenheit_entry, error_entry))
    clear_btn.place(x = 300, y = 260)

    win.mainloop()

main()
