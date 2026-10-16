import sys
import Ice

Ice.loadSlice('door.ice')
import Home

class DoorI(Home.Door):
    def __init__(self):
        self.percentage_open = 0

    def open(self, percentage, current=None):
        self.percentage_open = percentage

    def getOpening(self, current=None):
        return self.percentage_open

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints(
        "DoorAdapter", "default -p 10000")
    adapter.add(DoorI(), Ice.stringToIdentity("door1"))
    adapter.activate()
    communicator.waitForShutdown()
