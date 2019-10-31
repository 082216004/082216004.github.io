# mini cost = 0.1a+0.15b
# 5a+10b => 45(蛋白需求) //constraints1
# 4a+3b => 24(維他命需求) //constraints2
# 0.5a => 1.5(鐵需求) //constraints3
# a,b => 0(非負) //constraints4

ans=[]
x=float
y=float

def ot(x,y):
    return 0.1*x+0.5*y

def c1(x,y):
    egw=5*x+10*y
    if(egw >= 45):
        return 1
    else :
        return 0 

def c2(x,y):
    vit=4*x+3*y
    if(vit >= 24):
        return 1
    else :
        return 0

def c3(x):
    if(x>=3):
        return 1
    else :
        return 0

def c4(x,y):
    if(x >= 0 and y >= 0 ):
        return 1
    else :
        return 0

for i in range(100):
    for j in range(100):
        c1r=c1(i,j)
        c2r=c2(i,j)
        c3r=c3(i)
        c4r=c4(i,j)
        if((c1r==1) and (c2r==1) and (c3r==1) and (c4r==1)):
            ans.append({"cost":(ot(i,j)),"a":i,"b":j})
            # result.append({ot(i,j)})

print(ans[0:30])
