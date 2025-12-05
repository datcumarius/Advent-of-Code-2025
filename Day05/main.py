from dataclasses import dataclass

@dataclass(frozen=True)
class Interval:
    start: int
    end: int

# Read input file and separate intervals from ingredient IDs
with open("Day05/input.txt") as file:
    blocks = file.read().split("\n\n")
    intervals = []
    for line in blocks[0].splitlines():
        parts = line.strip().split("-")
        new_interval = Interval(start = int(parts[0]), end = int(parts[1]))
        intervals.append(new_interval)
    ids = [int(line.strip()) for line in blocks[1].splitlines()]

fresh_count = 0
#for every id, check if it falls within any of the intervals
for idx in ids:
    for interval in intervals:
        if interval.start <= idx <= interval.end:
            fresh_count += 1
            break
#part 1
print(f"{fresh_count} ingredients are fresh (part 1)")

#sort and merge intervals for part 2
#sort by start value
intervals.sort(key=lambda x: x.start)

merged_intervals = []
current_interval_start = intervals[0].start
current_interval_end = intervals[0].end

for i in range(1, len(intervals)):
    next_interval = intervals[i]

    if current_interval_end >= next_interval.start:
        #overlapping intervals, merge them
        current_interval_end = max(current_interval_end, next_interval.end)
    else:
        #no overlap, add current to merged and move to next
        merged_intervals.append(Interval(start=current_interval_start, end=current_interval_end))
        current_interval_start = next_interval.start
        current_interval_end = next_interval.end

#add the last interval
merged_intervals.append(Interval(start=current_interval_start, end=current_interval_end))

#for every interval, count the number of possible fresh ingredients
number_of_fresh_ids = 0
for interval in merged_intervals:
    number_of_fresh_ids += interval.end - interval.start + 1

print(f"{number_of_fresh_ids} ingredients could be fresh (part 2)")