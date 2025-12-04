def highest_joltage_part1(strnum):
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

def max_in_range(digits, start, end):
    maxi = -1
    maxi_id = -1
    for i in range(start, end):
        if digits[i] > maxi:
            maxi_id = i
            maxi = digits[i]
        if maxi == 9:
            break
    return maxi, maxi_id

def highest_joltage_part2(strnum, length):
    digits = [int(c) for c in strnum]
    n = len(digits)
    startid = 0
    joltage = 0
    needed = length
    for _ in range(length):
        val, idx = max_in_range(digits, startid, n - needed + 1)
        joltage = joltage * 10 + val
        startid = idx + 1
        needed -= 1
    return joltage

joltage_sum_part1 = 0
joltage_sum_part2 = 0
with open("Day03/input.txt") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line:
            result = highest_joltage_part1(clean_line)
            if result == -1:
                raise ValueError("No valid joltage found in line for part 1:", clean_line)
            else:
                joltage_sum_part1 += result
            result = highest_joltage_part2(clean_line, 12)
            if result == -1:
                raise ValueError("No valid joltage found in line for part 2:", clean_line)
            else:
                joltage_sum_part2 += result
print(joltage_sum_part1)
print(joltage_sum_part2)
