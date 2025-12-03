dial = 50
cnt = 0
with open("input.txt") as fisier:
    for line in fisier:
        for _ in range(int(line[1:])):
            if line[0] == "L":
                dial -= 1
                if dial < 0:
                    dial = 99
            elif line[0] == "R":
                dial += 1
                if dial > 99:
                    dial = 0
            if(dial == 0):
                cnt=cnt+1
print(cnt)
