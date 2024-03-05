from .world import World
import time
from .kbhit import KBHit


def main():
    filename=input("**** Welcome to the Game of Life! **** \n type in file name for grid configuration or hit enter for random. \n ")
    if filename == '':
        size=input('Enter desired board size: \n')
    else: 
        filename='projects/gameoflife/'+filename+'.txt'
        with open(filename,'r') as fh:
            size=len(fh.readline().split(','))
    if size == '': size=10
    world=World(int(size),filename)

    speed_input=input('Enter Desired Simulation Speed From 1-10, \n enter man for frame by frame: \n')
    loop=True
    k=KBHit()
    if speed_input == '':
        speed_input=20
        print('You found a cheat code!')
        time.sleep(.5)
    if speed_input != 'man':
        time_step=float(speed_input)**-1
        while loop:
            loop=world.progress()
            time.sleep(time_step)
            if k.kbhit(): 
                loop=False
                k.getch()
    else:
        loop=world.progress()
        print('Hit enter to continue, or Q to quit')
        while loop:
            khit=k.getch()
            if khit == '\n':
                loop=world.progress()
                print('Hit enter to continue, or Q to quit')
            elif khit == 'q':
                break
    print('Hit enter to play again or anything else to quit \n')
    if k.getch() == '\n':
        main()
            
            




if __name__ == '__main__':
    main()
    


    
