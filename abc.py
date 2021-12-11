def gen_list(n):
    return [chr(97+x) for x in range(n)]

def print_rangoli(size):
    alpha_list = gen_list(size) 
    canv = [['-']*(4*size-3)]*(2*size-1)
    temp = []
    for i in range(1,size+1):
        letter = alpha_list[-i:]
        middle = size*2-1
        for j in range(len(letter)):
            j = 2*j
            canv[i-1][middle-j-1] = letter[j//2]
            canv[i-1][middle+j-1] = letter[j//2]

        temp.append(''.join(canv[i-1]))  
    
    for i in range(len(temp)-1):
        print(temp[i])
    for i in range(len(temp)-1,-1,-1):
        print(temp[i])

    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

