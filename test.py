import websockets.client
import asyncio

async def getdata():
    async with websockets.client.connect("wss://gps-ash-hashtag.koyeb.app") as socket:
        await socket.send("csv")
        response = await socket.recv()
        print(response)

async def cleardata():
    async with websockets.client.connect("wss://gps-ash-hashtag.koyeb.app") as socket:
        await socket.send("clear")


# asyncio.run(getdata())
asyncio.run(cleardata())


