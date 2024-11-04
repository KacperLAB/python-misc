from time import *

print("rozpoczynam odliczanie")
t1 = strftime("%S",gmtime())
while True:
    dif = int(strftime("%S",gmtime())) - int(t1)
    if(dif>=5):
        print("minelo 5 s")
        quit()