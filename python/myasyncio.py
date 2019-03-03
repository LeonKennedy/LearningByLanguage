#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: myasyncio.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2019-03-03 22:46:18
# @Last Modified: 2019-03-03 22:46:18
#


import asyncio
import time, datetime

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    res = await say_after(1, 'hello')
    print(res)
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


# ----------
async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

#asyncio.run(display_date())
# ------------
