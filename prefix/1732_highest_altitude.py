class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = [0]
        max_altitude = 0
        for index in range(len(gain)):
            new_altitude = gain[index] + altitude[index]
            altitude.append(new_altitude)
            max_altitude = max(max_altitude, new_altitude)
        return max_altitude

