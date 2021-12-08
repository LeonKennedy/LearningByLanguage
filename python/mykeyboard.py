#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: mykeyboard.py
@time: 2021/10/4 4:56 下午
@desc:
"""

import keyboard
import time


def record():
    # 录制回放
    keyboard.start_recording()
    time.sleep(10)
    events = keyboard.stop_recording()
    keyboard.replay(events)


def capture():
    # 补货
    print('Press and release your desired hotkey: ')
    hotkey = keyboard.read_hotkey()
    print('Hotkey selected: ', hotkey)

    def on_triggered():
        print("Triggered!")

    keyboard.add_hotkey(hotkey, on_triggered)
    keyboard.write('The quick brown fox jumps over the lazy dog.')
    time.sleep(10)
    print("Press ESC to stop.")


def write_to_console():
    keyboard.write('The quick brown fox jumps over the lazy dog.')


if __name__ == '__main__':
    capture()
