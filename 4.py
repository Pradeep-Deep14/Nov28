def modify(n):
    return n+2
data=[2,4,6,8]
result=[modify(x) for x in data if x%4==0]

print(len(result))