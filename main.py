import pyqrcode
import os, shutil

# also open terminal and install pyqrcode using following command: pip install pyqrcode

title = input("Set qr title: \n")
text = input("What would you like qr code to contain(webpage link or sth.)? \n")

file_name_svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)
url.png(file_name_png, scale=10)

# specify path to your desktop... for easier specifying open your command prompt/ terminal

# for example: C:\user\main\Desktop\{title}

os.mkdir(fr"NameOfDisk:\User\user_name\Desktop\{title}")

# specify path to your desktop... for easier specifying open your command prompt/ terminal

shutil.move(f"{file_name_png}", fr"NameOfDisk:\User\user_name\Desktop\{title}")
shutil.move(f"{file_name_svg}", fr"NameOfDisk:\User\user_name\Desktop\{title}")
