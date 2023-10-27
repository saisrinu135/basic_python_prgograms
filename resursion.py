#using resursion
#inputs written in the baove program are written in the function arguments

def upper(a = "Hello woRld",res= "", i=0):
    if i==len(a):
        return res
    if 'a'<=a[i]<='z':
        res+=chr(ord(a[i])-32)
    else:
        res+=a[i]
    return upper(a,res,i+1)

print(upper())