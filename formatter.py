import math
hex_alpa =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']


def print_formatted(num):
    dec_space = math.ceil(math.log(num+1,10))
    hex_space = math.ceil(math.log(num+1,16))
    oct_space = math.ceil(math.log(num+1,8))
    bin_space = math.ceil(math.log(num+1,2))
    for number in range(1,num+1):
        dec_num = number
        hex_stack=[]
        oct_stack=[]
        bin_stack=[]
        while number>0:
            bin_stack.append(hex_alpa[number%2])
            number=number//2
        length=len(bin_stack)
        oct_list =  [bin_stack[i:i+3] for i in range(0, length, 3)]
        hex_list =  [bin_stack[i:i+4] for i in range(0, length, 4)]
        for li in oct_list:
            octal = 0
            for i in range(len(li)):
                octal = octal+int(li[i])*(2**i)
            oct_stack.append(hex_alpa[octal])  
        for li in hex_list:
            hexa = 0
            for i in range(len(li)):
                hexa = hexa+int(li[i])*(2**i)
            hex_stack.append(hex_alpa[hexa])
        oct_stack.reverse()
        hex_stack.reverse()
        bin_stack.reverse()
        oct_stack = ''.join(oct_stack)
        hex_stack = ''.join(hex_stack)
        bin_stack = ''.join(bin_stack)
        dec_num = str(dec_num)
        print(dec_num.rjust(dec_space,' ')+" "+oct_stack.rjust(oct_space,' ')+" "+hex_stack.rjust(hex_space,' ')+" "+bin_stack.rjust(bin_space,' '))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)