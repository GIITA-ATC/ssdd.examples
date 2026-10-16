import sys
import Ice

Ice.loadSlice('door.ice')
import Home

with Ice.initialize(sys.argv) as communicator:
    proxy = communicator.stringToProxy("door1:default -p 10000")
    door = Home.DoorPrx.checkedCast(proxy)
    door.open(20)             # looks like a local call
    print(door.getOpening())  # looks like a local call
