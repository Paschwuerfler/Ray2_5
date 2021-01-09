import os

os.system("pip install clear_screen")


import rich
print("test")
print ("\033[A \033[A")
from clear_screen import clear
clear()