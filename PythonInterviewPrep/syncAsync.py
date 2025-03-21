#sync and async
#sync: line by line
#asyc
#if one of the task is blocked next task will be immediately start

import asyncio
import time


def task(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"finished {name}")

task("rahul")
task("shetty")

async def task(name):
    print(f"starting {name}")
    await asyncio.sleep( 2 )
    print(f"finished {name}")

async def main():
    await asyncio.gather(task("rahul"),task("shetty"))


asyncio.run(main())
