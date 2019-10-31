# 3000x+900y<=75000 c1
# 5x>=y c2
# 5<=x<15 c3
# x>=0,y>=0 c4

ans=[]

def ad(x,y):
    return( x*200000 + y*80000 )

def c1(x,y):
    if( 3000*x + 900*y <= 75000 ):
        return 1
    else :
        return 0

def c2(x,y):
    if( 5*x >= y):
        return 1
    else :
        return 0

def c3(x):
    if( x >= 5 and x < 15 ):
        return 1
    else :
        return 0

def c4(x,y):
    if( x >= 0 and y >=0 ):
        return 1
    else:
        return 0

for i in range(100): #x
    for j in range(100): #y
        c1r=c1(i,j)
        c2r=c2(i,j)
        c3r=c3(i)
        c4r=c4(i,j)
        if(c1r==1 and c2r==1 and c3r==1 and c4r==1):
            # ans.append({"effective":ad(i,j),"Inter-net":i,"media":j})
            ans.append([ad(i,j),i,j])

ans.sort(key=lambda x:x[0],reverse=True)
print(ans[0])