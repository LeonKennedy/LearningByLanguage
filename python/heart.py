#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: heart.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2019-01-30 14:06:42
# @Last Modified: 2019-01-30 14:06:42
#

from curses import wrapper
import curses, random, logging

def main(stdscr):
    maxy, maxx = stdscr.getmaxyx()
    stdscr.timeout(1000)
    if curses.has_colors():
        color_num = init_color()
    for w, h in custom_size():

        stdscr.clear()
        ww, hh = custom_location(w, h)
        select_color_num = random.randint(1, color_num)
        for x,y in heart(w, h):
            if h + y < maxy:
                stdscr.addstr(hh + y, x + ww ,'*', curses.color_pair(select_color_num) )
        stdscr.refresh()
        #curses.napms(300)
        c = stdscr.getch()
        if c == ord('p'):
            PrintDocument()
        elif c == ord('q'):
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0

def init_color():
    color_set = [curses.COLOR_BLACK, curses.COLOR_RED, curses.COLOR_GREEN,
        curses.COLOR_YELLOW, curses.COLOR_BLUE, curses.COLOR_MAGENTA, 
        curses.COLOR_CYAN]

# and 7:white
    num = 0
    for i in color_set:
        for j in color_set:
            if not i == j:
                num += 1
                curses.init_pair(num, i, j)
    return num

def test_main(stdscr):
    maxy, maxx = stdscr.getmaxyx()
    stdscr.clear()
    w, h = 75, 92

    for i in range(w*2):
        for j in range(h*2):
            if j < maxy:
                stdscr.addstr(j, i ,'-')
    for x, y in heart(w,h):
        if y+h < maxy:
            stdscr.addstr( h + y, x + w ,'*')
    stdscr.refresh()
    stdscr.getkey()


def custom_size():
    while 1:
        hh = random.randint(5,44)
        w = random.randint(hh,100)
        yield w, hh
    
    
def custom_location(w,h):
    ww = random.randint(w, 100)
    hh = random.randint(h, 45)
    return ww, hh

def heart(w,h):
    ws, hs = 1.2, 1.5
    c = [  (x ,y) for x in range(-w, w) for y in range(-h ,h) if ((x/w* ws)**2+(y/h *hs)**2-1)**3+(x/w * ws)**2*(y/h*hs)**3 <= 0]
    yield from c

wrapper(main)



'''
print('\n'.join(
    [''.join(
        [ 
            ( 'Lovemimi'[(x-y)%8] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') 
            for x in range(-35,35)
            
        ]
        
        )for y in range(16,-16,-1)
        
    ]
))
'''
