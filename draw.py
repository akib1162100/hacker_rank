
def draw(n,m):
    subs=['.','|','.']
    welcome=['W','E','L','C','O','M','E']
    canv = [['-']*m]*n
    for i in range(1,n+1):
        temp_subs = subs*(2*i-1)
        rindx =int(m/2)-(int(len(temp_subs)/2))
        if i==int((n/2)+1):
            canv[i-1]=canv[i-1][:(int(m/2)-3)]+welcome+canv[i-1][-(int(m/2)-3):]
            continue
        if rindx<0:
            rev_i=(n+1)-i
            temp_subs = subs*(2*rev_i-1)
            rindx = -rindx
        canv[i-1]=canv[i-1][:rindx]+temp_subs+canv[i-1][-rindx:]
        
    print('\n'.join([''.join(x) for x in canv]))
        

n , m = input().split()

draw(int(n),int(m))