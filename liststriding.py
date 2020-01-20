firstlist = ['1','2','3','4','5','6','7','8','9','10']
#say we want to use starred expressions 
first, *mid, last = firstlist
print("First = {first}.\nMid = {mid}.\nLast ={last}".format(**locals()))
print(firstlist)

#say we want even in place of even numbers
firstlist[1::2]= ["even"]*len(firstlist[1::2])
print(firstlist)

secondlist = ["Ram","is","a","boy"]
print(secondlist)
print(' '.join(secondlist))

#let's do a function
def multiplication(a,b,c):
    return a*b*c
L = [5,10,15]
print(multiplication(5,10,15))
print(multiplication(*L))
print(multiplication(5,*L[1:]))
    





