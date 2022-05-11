from operator import sub

#!/usr/bin/python

# def displayPathtoPrincess(n,grid):
#print all the moves here
direction_h = {-1:'LEFT', 1:'RIGHT'}
direction_v = { -1:'UP', 1:'DOWN'}
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

bot_pos = index_2d(grid, 'm')
princess_pos = index_2d(grid, 'p')


diff = tuple(map(sub, princess_pos, bot_pos))
if abs(diff[0]) > abs(diff[1]):
    print(direction_v[diff[0]/abs(diff[0])])
else:
    print(direction_h[diff[1]/abs(diff[1])])


# print(diff)

# displayPathtoPrincess(m,grid)