a=int(input(),2)
b=int(input(),2)
mask =2**100000-1
print(bin(a&b)[2:].zfill(10**5))
print(bin(a|b)[2:].zfill(10**5))
print(bin(a^b)[2:].zfill(10**5))
print(bin(a^mask)[2:].zfill(10**5))
print(bin(b^mask)[2:].zfill(10**5))