# imports
from guizero import App,Combo
from string import ascii_letters

app = App("Enter your name")

a_letter = Combo(app,options=" "+ascii_letters,align="left")

app.display()