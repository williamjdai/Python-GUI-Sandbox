import pywhatkit
import datetime
from tkinter import *

mainWindow = Tk()
mainWindow.geometry('1080x750')
mainWindow.title("Palindromic Age Detector")



q1 = Label(mainWindow, text = "Welcome to the Palindromic Age Detector")
q1.grid()

currentDate = datetime.datetime.now()
months = {1:"January", 2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
formattedDate = "" + months[currentDate.month] + " " + str(currentDate.day) + ", " + str(currentDate.year)
q2 = Label(mainWindow, text = "Today's date is " + formattedDate)
q2.grid()

q3 = Label(mainWindow, text = "Please enter your birthday! Use MM/DD/YYYY format ^_^")
q3.grid(column=0,row=2)

txt = Entry(mainWindow, width=10)
txt.grid(column=1, row=2)

def clicked():
    month = int(txt.get()[0:2])
    day = int(txt.get()[3:5])
    year = int(txt.get()[6:])
    print("" + months[month] + " " + str(day) + ", " + str(year))
    #todo? no age verification, so nonsensical inputs like 13/99/9999 are allowed.
    if day >= currentDate.day and month>=currentDate.month:
        #birthday has passed
        age = currentDate.year - year
    else:
        age = currentDate.year - year - 1
    print(age)
    if age==22:
        pywhatkit.playonyt("https://www.youtube.com/watch?v=AgFeZr5ptV8")
    if str(age)==str(age)[::-1]:
        congrats = Label(mainWindow, text = "CONGRATULATIONS! YOUR AGE IS A PALINDROME")
        congrats.grid()

btn = Button(mainWindow, text = "submit", fg = "red", command=clicked)
btn.grid(column=2, row=2)



mainWindow.mainloop()

#pywhatkit.playonyt("https://www.youtube.com/watch?v=AgFeZr5ptV8")