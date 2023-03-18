n=int(input())

for i in range(n):
    #Get Input string
    string=input()
    #Variable to store characters in even index
    even=''
    #Variable to store characters in even index
    odd=''
    for j in range(len(string)):
        #if index is even
        if j%2==0:
            even+=string[j]
        #if index is odd
        else:
            odd+=string[j]
    print("{} {}".form
