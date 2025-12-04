def highest_joltage(strnum):
    maxi = -1
    digits = [int(c) for c in strnum]
    for i in range(len(strnum)):
        if digits[i] < maxi // 10:
            continue
        for j in range(i+1, len(strnum)):
            num = digits[i] * 10 + digits[j]
            if num > maxi:
                maxi = num
    return maxi
joltage_sum = 0
with open("Day03/input.txt") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line:
            joltage_sum += highest_joltage(clean_line)
print(joltage_sum)
