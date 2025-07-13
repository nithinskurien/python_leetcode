class Solution:
    def __init__(self):
        self.stack = None
        self.vistedRooms = None

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        self.vistedRooms = set()
        self.stack = [0]
        while self.stack:
            currRoom = self.stack.pop()
            if not currRoom in self.vistedRooms:
                self.vistedRooms.add(currRoom)
                self.stack.extend(rooms[currRoom])
        return len(self.vistedRooms) == len(rooms)
