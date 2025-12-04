def is_invalid(number):
    strnum = str(number)
    for d in range(1, len(strnum)//2 + 1):
        if len(strnum) % d != 0:
            continue
        pattern = strnum[:d]
        repeats = len(strnum) // d
        if pattern * repeats == strnum:
            return True
    return False

sum = 0
with open("Day02/input.txt") as file:
    intervals = file.read().split(",")
    for interval in intervals:
        parts = interval.split("-")
        start = int(parts[0])
        end = int(parts[1])
        for num in range(start, end + 1):
            if is_invalid(num):
                sum += num
print(sum)