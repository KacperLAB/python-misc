#import PySimpleGUI as sg

def read():
    text = input("Enter text:")
    return text
def write_to_file(text):
    file = open("file.txt","a")
    file.write(text)
    file.write('\n')
    file.close
def print_txt():
    file = open("file.txt","r")
    lines = file.readlines()
    for line in lines:
        print(line.strip())
    
#sg.Window(title="Apk", layout=[[]], margins=(100,100)).read()

running = True
while(running):
    option = input("Chose action | [1] - write to file, [2] - read txt file, [0] - exit: \n")
    match option:
        case '1':
            write_to_file(read())
        case '2':
            print_txt()
        case '0':
            print("Exiting")
            running = False
        case _:
            print("Error - wrong input")

