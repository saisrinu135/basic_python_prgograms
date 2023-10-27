#i/p [1,2,3,4,5,6]
#o/p ([1,3,6,10,15,21],56)

ol = []
il = [1,2,3,4,5,6]
sum = 0
i=0
while i<len(il):
    sum+=il[i]
    ol+=[sum]
    i+=1
print(ol)