#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: text_simulate.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: DES Discrete Event Simulation for texi
# @Create: 2018-12-01 10:52:08
# @Last Modified: 2018-12-01 10:52:08

from collections import namedtuple
import random, queue

Event = namedtuple('Event', 'time proc action')

def text_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'go home')

class Simulate:
    def __init__(self, process):
        self.queue = queue.PriorityQueue()
        self.proc = dict(process)

    def run(self, end_time):
        for _,proc in self.proc.items():
            a = next(proc)
            self.queue.put(a)

        start_time = 0
        while start_time < end_time:
            if self.queue.empty():
                print('**** end  event ****')
                break
            texi = self.queue.get()
            t , p, a = texi
            print('text:',t,p*' ', texi)
            start_time = t
            current_proc = self.proc[p]
            try:
                new_event = current_proc.send(t + random.randint(1,10))
            except StopIteration:
                del self.proc[p]
            else:
                self.queue.put(new_event)
        else:
            print('*** end of simulation time:{} ***'.format(end_time))



if __name__ == "__main__":
    data = { 0: text_process(0, 3, 0),
            1:  text_process(1, 4, 5),
            2:  text_process(2, 2, 10)}

    s = Simulate(data)
    s.run(30)
