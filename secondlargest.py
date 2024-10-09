def second_large(num):
    first,second=0,0
    for i in num:
        if i>first:
            first,second=i,first
        elif first>i>second:
            second=i
    return second
num=[3,7,9,10,12,44,67,1]

print(second_large(num))