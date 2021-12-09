#!/usr/bin/env python
# encoding: utf-8
"""
@author: coffee
@license: (C) Copyright 2017-2020, Node Supply Chain Manager Corporation Limited.
@contact: lionhe0119@hotmail.com
@file: async_wait_condition.py
@time: 2021/4/3 3:46 下午
@desc:
"""
import asyncio


async def execute_on(condition, coro, predicate):
    async with condition:
        await condition.wait_for(predicate)
        await coro


async def print_coro(text):
    print(text)


async def worker(numbers):
    while numbers:
        print("Numers:", numbers)
        numbers.pop()
        await asyncio.sleep(0.25)


async def main():
    numbers = list(range(10))
    condition = asyncio.Condition()
    is_empty = lambda: not numbers
    await worker(numbers)
    await execute_on(condition, print_coro("Finish"), is_empty)


if __name__ == '__main__':
    asyncio.run(main())
