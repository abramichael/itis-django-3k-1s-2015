#find max with one line
print(reduce(lambda x,y: x if x > y else y, map(int, raw_input().split())))

