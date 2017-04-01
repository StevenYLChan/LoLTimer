
import os
import time
import sys
import subprocess
import re
from threading import Timer

def is_non_zero_file(fpath):  
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False

def new_line(line):
    #print(line)
    cooldown = [int(s) for s in line.split() if s.isdigit()]
    cooldown = int(cooldown.pop())
    description = " ".join(re.findall("[a-zA-Z]+", line))
    description = description[:].upper()
    #print("\n@" + description)
    #for i in range(cooldown,0,-1):
    #    print '%d seconds\r' % i,
    #    sys.stdout.flush()
    #    time.sleep(1)
    print(line)
    clock(cooldown,description)


def clock(cooldown,description):
    t=Timer(cooldown,clock_output,args=(description,))
    t.start()

def clock_output(description):
    print(description +" IS UP!")
    t2s = '"' + description +' IS UP!' +'"'
    subprocess.call('espeak '+t2s, shell=True)

    
def main():
    print("----LEAGUE OF LEGENDS TIMER----".center(10))
    print("\nInstructions".center(10))
    print("This program uses the notes function built into the LoL client.")
    print("While in game, type '/n' followed by anything you want. Example: /n annie f 180")
    print("The program will notify you when a cooldown is up.")

    if is_non_zero_file('directory_file.txt'):
        directory_file = open("directory_file.txt",'r')
        note_directory=str(directory_file.read())
        directory_file.close()
    else:
        print("Your default MyNotes.txt directory is:\n\tC:\Riot Games\League of Legends\RADS\solutions\lol_game_client_sln\\releases\0.0.1.125")
        print("If you do not see a MyNotes.txt file it is because you haven't used the note command before. Hop into a game and use the command to create the file.")
        directory_file = open("directory_file.txt",'w')
        note_directory=""
        while True:
            note_directory = raw_input("\nEnter MyNotes.txt directory: ")
            if not note_directory:
                print("[ERROR] Enter a directory location!")
                continue
            else:
                directory_file.writelines(note_directory)
                directory_file.close()
                break
    print("\nThe program is using " + note_directory + " as MyNotes.txt directory.")
    print("If at any time you would like to change MyNotes.txt directory, edit the directory_file.txt file.")

    #my_notes = open(note_directory + '\MyNotes.txt', 'r')
    try:
        my_notes = open('MyNotes.txt','r')
    except:
        print("[ERROR] No such file or directory. Please make sure your directory is correct and run the program again.")
        exit()
    open('MyNotes.txt', 'w').close()
    while True:

        line = my_notes.readline()
        if not line:
            time.sleep(1)
            #print 'Nothing New'
        else:
            if line.startswith("@"):
                new_line(line)

main()




