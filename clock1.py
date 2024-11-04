from time import sleep
import os

h=0
m=0
s=0
run = True
while run:
    os.system('cls||clear')
    print(h,':',m,':',s)
    sleep(1)
    s += 1
    if(s==60):
        s=0
        m += 1
    if(m==60):
        m=0
        h += 1
    if(h==24):
        run = False
    