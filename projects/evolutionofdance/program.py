from pgl import *
from dancers import *
from random import choice
from copy import deepcopy
from time import sleep
### defining constants
GWX=400
GWY=600
xmid=GWX//2


### Initializing the window
win=GWindow(GWX,GWY)

### Defining Helpful Functions
def make_floor(GWX=GWX, GWY=GWY, size=25):
    c_idx=0
    colors=['light_grey','grey']
    for i in range(4, GWY//size - 5):
        for j in range(1 ,GWX//size -1):
            sq=GRect(j*size,i*size,size,size)
            sq.set_filled(True)
            sq.set_fill_color(colors[c_idx % 2])
            win.add(sq)
            c_idx+=1
        c_idx+=1
def set_center(obj:GLabel,new_str:str):
    y=obj.get_location().get_y()
    obj.set_label(new_str)
    obj.set_location(xmid-obj.get_bounds().get_width()//2,y)

### Making the objects
win.set_window_title('\U0001FAA9 Dance Off! \U0001FAA9')
now_playing=GLabel('Now Playing: ')
featured_dancer=GLabel('')
featured_dancer.set_font('30px "times new roman"')
announcement=GLabel('')
round_counter_title=GLabel('Round')
disco_ball=GLabel('\U0001FAA9',0,100)
disco_ball.set_font('40px "times new roman"')
dcx,dcy = xmid, 100
win.disco_rays=[
    GLine(dcx,dcy,dcx+100,dcy+20),
    GLine(dcx,dcy,dcx-90,dcy+40),
    GLine(dcx,dcy,dcx-80,dcy+60),
    GLine(dcx,dcy,dcx-60,dcy+80),
    GLine(dcx,dcy,dcx-40,dcy+90),
    GLine(dcx,dcy,dcx-20,dcy+95),
    GLine(dcx,dcy,dcx,dcy+100),
    GLine(dcx,dcy,dcx+20,dcy+95),
    GLine(dcx,dcy,dcx+40,dcy+90),
    GLine(dcx,dcy,dcx+60,dcy+80),
    GLine(dcx,dcy,dcx+80,dcy+60),
    GLine(dcx,dcy,dcx+90,dcy+40),
    GLine(dcx,dcy,dcx-100,dcy+20),
            
]
win.ray_colors=['pink','red', 'salmon', 'aqua','blue']


### Initializing the Dancing
df=Dance_Floor()
dance_line=GLabel(('ABC'*(1+len(df.dancer_list)) +'\n'))
dance_line.set_visible(False)
dance_line.set_font('20px "times new roman"')

### Add the objects
make_floor()
win.add(now_playing,xmid-now_playing.get_width()//2,50)
win.add(featured_dancer,xmid-featured_dancer.get_width()//2,GWY*(3/4))
win.add(announcement,xmid-announcement.get_width()//2,GWY*(7/8)+10)
win.add(round_counter_title, xmid-round_counter_title.get_width()//2, GWY*(15/16))
win.add(dance_line,xmid-(dance_line.get_width() // 2), GWY*(2/3))
for idx,line in enumerate(win.disco_rays):
    line.set_color(win.ray_colors[idx%4])
    line.set_line_width(3)
    win.add(line)
set_center(disco_ball, '\U0001FAA9')
win.add(disco_ball)


###  defining interacting functions
win.prev_line_depth=dance_line.get_height()
def next_round():
    if not win.stop:
        if win.iters % 20 == 0:
            rdx=randrange(len(df.dances_list))
            new_dancer=deepcopy(choice(df.dancer_list))
            new_dance=df.dances_list[rdx]

            set_center(announcement, f'{new_dancer.name} joins, hitting the {new_dance}!')
            set_center(now_playing, 'Now Playing: ' + new_dancer.music)
            dance_line.set_label(str(df))
            dance_line.move(0,win.prev_line_depth-dance_line.get_height())
            win.prev_line_depth=dance_line.get_height()
            dance_line.set_visible(True)
            set_center(featured_dancer,str(new_dancer))
            set_center(round_counter_title, "Round: "+str(win.rounds+1))
            
            df.next_round(new_dancer,rdx+1)
            if win.rounds % 6 == 0:
                df.pop_back()
                df.pop_front()
            
            win.rounds+=1

        for idx,line in enumerate(win.disco_rays):
            idx+=win.iters
            line.set_color(win.ray_colors[idx%5])
        win.iters+=1
        if win.rounds == win.reqrounds:
            print("Keep Dancing?")
            request_rounds()
def key(key):
    win.stop = not win.stop
def request_rounds():
    popup=GLabel('',0,GWY//2)
    popup.set_font('50px "Times New Roman"')
    set_center(popup, 'Look To Terminal')
    win.add(popup)
    win.reqrounds=int(input('How Many Rounds? Enter 0 to quit.  '))
    win.remove(popup)
    win.stop=False
    win.rounds=0
    win.iters=0

    if win.reqrounds == 0:
        win.close()

request_rounds()
print('Press any key to pause/unpause')
win.add_event_listener('key',key)
win.set_interval(next_round,100)




