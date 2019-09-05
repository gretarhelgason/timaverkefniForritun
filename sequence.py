n = int(input("Enter the length of the sequence: ")) # Do not change this line

seqArray = [1, 2, 3]

counter = 3
while counter < n:
    seqArray.append(sum(seqArray[-3:]))
    counter +=1

for i in seqArray:
    print(i)

