#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: myasyncio.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2019-03-03 22:46:18
# @Last Modified: 2019-03-03 22:46:18
#


import asyncio
import datetime
import time


async def say_after(delay, what):
    """

    :param delay:
    :param what:
    """
    await asyncio.sleep(delay)
    print(what)


async def main():
    """
        test
    """
    print(f"started at {time.strftime('%X')}")

    res = await say_after(1, 'hello')
    print(res)
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


# ----------
async def display_date():
    """
        test

    """
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 10.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


def run_without_check():
    task = asyncio.create_task(display_date())
    return 


async def block_sleep():
    num = 0
    while 1:
        await asyncio.sleep(5)
        num += 1
        print(f'{num} block sleep(10) ')


async def run_lot_sub_coroutines():
    
    run_without_check() 
    await asyncio.gather(
        block_sleep(),
        asyncio.sleep(8)
    )
    lps = asyncio.get_event_loop()
    print(1)


if __name__ == "__main__":
    #asyncio.run(display_date())
    asyncio.run(run_lot_sub_coroutines())

