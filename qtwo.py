mark = [45,78,62,89,55,92,38,76]

highest = max(mark)
lowest = min(mark)
average = sum (mark) / len(mark)

above_average = 0
for m in mark:

    if m> average:
        above_average += 1
        ascending = sorted(mark)
        print("higest mark:", highest)
        print("lowest mark:", lowest)
        print("average mark:", average)
        print("students above average:", above_average)