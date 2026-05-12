def sum_up(n:int) ->int:
    if n <=1:
        return n
    else:
        return sum_up(n-1)+n**3

print(sum_up(5))

print(sum([i**3 for i in range(1,6)]))

