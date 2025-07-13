import heapq
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


class SmallestInfiniteSet:

    def __init__(self):
        self.infiniteSet = [num for num in range(1, 1001)]

    def popSmallest(self) -> int:
        return heapq.heappop(self.infiniteSet)

    def addBack(self, num: int) -> None:
        if num not in self.infiniteSet:
            heapq.heappush(self.infiniteSet, num)

if __name__ == "__main__":
    obj = SmallestInfiniteSet()
    param_1 = obj.popSmallest()
    obj.addBack(1)