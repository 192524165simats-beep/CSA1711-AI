room = {'A': 1, 'B': 0}
pos = 'A'

while 0 in room.values():
    if room[pos] == 0:
        print(pos, "is dirty - Cleaning")
        room[pos] = 1
    else:
        print(pos, "is clean")

    pos = 'B' if pos == 'A' else 'A'

print("Both rooms are clean!")
