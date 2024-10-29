# import asyncio


# # python 3.4
# # Синтаксис не работает после python 3.8
# @asyncio.coroutine
# def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         yield from asyncio.sleep(1)

# @asyncio.coroutine
# def print_time():
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print("{} seconds have passed".format(count))
#         count += 1
#         yield from asyncio.sleep(1)


# @asyncio.coroutine
# def main():
#     task1 = asyncio.ensure_future(print_nums())
#     task2 = asyncio.ensure_future(print_time())

#     yield from asyncio.gather(task1, task2)

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()


# # python 3.8

# async def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         await asyncio.sleep(1)


# async def print_time():
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print("{} seconds have passed".format(count))
#         count += 1
#         await asyncio.sleep(1)


# async def main():
#     task1 = asyncio.create_task(print_nums())
#     task2 = asyncio.create_task(print_time())

#     await asyncio.gather(task1, task2)

# if __name__ == '__main__':
#     asyncio.run(main())


# # Не асинхронный код для приёма файлов по сети

# import requests
# from time import time


# def get_file(url):
#     r = requests.get(url, allow_redirects=True)
#     return r


# def write_file(response):
#     filename = response.url.split('/')[-1]
#     with open(filename, 'wb') as file:
#         file.write(response.content)

# def main():
#     t0 = time()

#     url = 'https://loremflickr.com/320/240'

#     for i in range(10):
#         write_file(get_file(url))

#     print(time() - t0)

# if __name__ == '__main__':
#     main()


# Асинхронный код для приёма файлов по сети


import asyncio
import aiohttp
from time import time


def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':

    t0 = time()
    asyncio.run(main())
    print(time() - t0)
