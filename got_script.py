import os
import pyperclip
import re

otvet=[]

os.system(r"tasklist /v | clip")

path = 'text.txt'

with open(path, "w") as f:
    f.write(pyperclip.paste())

with open(path, "r+") as f:
    text = f.read()
    text = re.split("DESKTOP-R604OCC", text)
    print(text)
    for i in text:
        resalt = re.findall("............................................docx", i)
        for d in resalt:
            if len(d)!=0:
                resalt = d
                print(resalt)
                spros=re.split(r"", d)
                print(spros)
                os.system(f"cd\\ ")
                os.system(f"dir *{}*.* /s | clip")
                path = 'text_obrabotca.txt'
                with open(path, "w") as f:
                    f.write(pyperclip.paste())
                spros.pop(0)


            
                

        # f.write(i)
        # resalt = re.findall(r" ")


# os.scandir("{}.docx")
