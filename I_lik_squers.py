nums=[1,2,3,4,5,6,7,8,9,10]
squares=[]
for n in nums:
    squares.append(n**2)

even=[]
odd=[]
for s in squares:
    if s%2==0:
        even.append(s)
    else:
        odd.append(s)
print("squares:",squares)
print("even squares:",even)
print("odd squares:",odd)
