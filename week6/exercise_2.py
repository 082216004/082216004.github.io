mystring = "hello"
myfloat = 10.0
myint = 20
# isinstance(x,y) 判斷y是否為x型態
# print內的%是key 後面擺元素型態
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat,float) and myfloat ==10.0:
    print("Float: %f" % myfloat)
if isinstance(myint,int) and myint ==20:
    print("Integer: %d" % myint)