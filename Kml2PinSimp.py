import tkinter as tk
import lxml.etree as le
import re

from tkinter import filedialog

root = tk.Tk()
root.withdraw()

##file_path = filedialog.askopenfilename(filetypes=[("KML Files", ".kml")("Any","")])
file_path = filedialog.askopenfilename()
writeIt = True
seenName = False
name = ""
nameNum = 0
i = 0
nameOfPole = ""
with open(file_path, "r") as f:
    lines = f.readlines()
with open(file_path, "w") as f:
    for line in lines:
        if (line.strip("\n") == "<description><![CDATA[<center><table><tr><th colspan='2' align='center'><em>Attributes</em></th></tr><tr bgcolor=\"#E3E3F3\">"):
            writeIt = False
            print("deleting description and extended data\n")
        if (line.strip("\n") == "<Point>"):
            writeIt = True
            print("continue writing point")
        if ("<name>" in line):
            if(nameNum == 0):
                nameOfPole = line
                delimited = re.split('<name>| |</name>',nameOfPole)
                nameOfPole = "<name>" + delimited[3] + "</name>"
                print("saving pole name")
            if(nameNum == 2 ):
                line = nameOfPole 
        #print("i see name " + str(i))
            #print(line)
            seenName = True
            nameNum = nameNum + 1
            i = i + 1
            
                   

        
        #if (not seenName) and ("name" in line):
           # print("I see name")
            #seenName = True
        if(writeIt):
            f.write(line)
print("Complete")