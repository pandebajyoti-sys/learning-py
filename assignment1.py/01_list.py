numbers=[5,6,3,7,8,9,1,2,4,8]
print("List:", numbers)

#lenghth of the list
length=0
for i in numbers:
    length+=1
print("Length of the list:", length)

#maxium 
maximum= numbers[0]
for x in numbers:
    if x > maximum:
        maximum=x
        print("Maximum:", maximum)
        
#minimum
minimum= numbers[0]
for x in numbers:
    if x < minimum:
        minimum=x
        print("Minimum:", minimum)