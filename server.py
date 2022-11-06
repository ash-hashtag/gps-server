import csv

import asyncio
import websockets.server
from navpy import lla2ecef

addr = "0.0.0.0"
port = 8080
allowed_users = [
    "user001",
    "user002"
]

def writerow(data: str):

    #data format would be time(as iso string),id,latitude,longitude,altitude
    arr = data.split(',')

    for user in allowed_users:
        if user == arr[1]:
            try:
                with open("location.csv", "a+", newline="") as file:
                 
                    xyz = lla2ecef(float(arr[-3]), float(arr[-2]), float(arr[-1]))

                    arr = arr[:-3]
                    arr.extend(xyz)

                    print("writing row ", arr)
                            
                    csv.writer(file).writerow(arr)

            except Exception as e:
                    print("error ", e)
            return


async def echo(websocket: websockets.server.WebSocketServerProtocol):
    try:
        async for message in websocket:
            if message == "csv":
                print(message)
                try:
                    with open("location.csv", "r") as file:
                        await websocket.send(file.read())
                except Exception as e:
                        print("error opening file", e)
            elif message == "clear":
                try:
                    with open("location.csv", "w+") as file:
                        file.write("")
                except Exception as e:
                    print("error opening file ", e)
            else:
                writerow(message)
    except Exception as e:
        print("error socket ", e)

#d6FG&G&H*^G&
async def start_web_socket():
    async with websockets.server.serve(echo, addr, port):
        await asyncio.Future()

print(f"starting web socket server address: {addr} port: {port}")
asyncio.run(start_web_socket())
