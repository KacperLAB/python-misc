import time

def generuj_kombinacje(n, znaki,szukane):
  if n == 0:
    return [""]
  else:
    kombinacje = []
    for znak in znaki:
      poprzednie_kombinacje = generuj_kombinacje(n - 1, znaki,szukane)
      if kombinacje.__contains__(szukane):
           print("znaleziono na pozycji: ")
           print(kombinacje.index(szukane))
           break
      for poprzednia_kombinacja in poprzednie_kombinacje:
        kombinacje.append(znak + poprzednia_kombinacja)
    return kombinacje

def generuj_znaki():
    znaki = []
    for i in range(48,58):  # 0-9
        znaki.append(chr(i))
    #for i in range(65,91):  # A-Z
    #    znaki.append(chr(i))
    #for i in range(97,123): # a-z
    #    znaki.append(chr(i))
    return znaki

n = 7
szukane = None
znaki = generuj_znaki()
start = time.perf_counter()
kombinacje = generuj_kombinacje(n, znaki,szukane)
print(time.perf_counter() - start)


