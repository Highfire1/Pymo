import sys
import asyncio
from core.game import Game
from core.server.server import Server

async def main(argv):
    if len(argv) == 0:
        g = Game()
        await g.mainLoop()
    elif argv[0] == "-s":
        s = Server()
        await s.mainLoop()
    else:
        print("Unknown Argument...")

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))