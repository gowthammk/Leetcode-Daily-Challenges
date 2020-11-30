import sortedcontainers


class Solution:
    def getSkyline(self, buildings):
        events = [[x, b[2], enter] for b in buildings for x, enter in zip(b[:2], [1,-1])]
        events.sort(key=lambda x: (x[0]))
        ans = []
        heights = sortedcontainers.SortedList()
        for i, event in enumerate(events):
            x, h, status = event[0], event[1], event[2]
            if status == 1:
                if not heights or h > heights[-1]:
                    ans.append([x, h])
                heights.add(h)
            else:
                heights.discard(h)
                if not heights:
                    ans.append([x, 0])
                elif h > heights[-1]:
                    ans.append([x, heights[-1]])
        return ans

print(Solution.getSkyline("", [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))