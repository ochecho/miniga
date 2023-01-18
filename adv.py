def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var12 = func3(arg1, var7)
    var17 = func4(var7, arg2)
    var22 = func5(arg2, var12)
    var23 = -302 & var17
    if arg2 < var7:
        var24 = var22 | var17
    else:
        var24 = (arg2 | var12 ^ arg2) & -1972786203
    var25 = var22 ^ var23
    var26 = var22 & (338 & var12)
    var27 = -40255389 - ((-985 ^ var25) & 1752346111)
    var28 = (var17 | (var17 + arg2)) & var22
    var29 = (var28 + var26) - arg2 + var23
    var30 = (-225 | -171) + var27 + arg1
    var31 = arg2 ^ var29
    var32 = ((var26 & arg1) - var17) & arg2
    var33 = (var27 ^ var30 - var26) ^ var30
    var34 = var12 | var29 | var30
    var35 = var25 - var34
    var36 = (arg1 - var30) + arg1 | var28
    var37 = (arg2 + var34 ^ var23) ^ var31
    var38 = var26 ^ var23
    var39 = (var37 ^ (var33 + var27)) + arg1
    result = (var23 ^ arg2) | var39
    return result
def func5(arg18, arg19):
    var20 = 0
    for var21 in xrange(42):
        var20 += var20 ^ var20
    return var20
def func4(arg13, arg14):
    var15 = 0
    for var16 in range(31):
        var15 += arg14 - var15
    return var15
def func3(arg8, arg9):
    var10 = 0
    for var11 in range(4):
        var10 += (arg8 & var10) & arg8
    return var10
def func2(arg3, arg4):
    var5 = 0
    for var6 in ((4 + arg4) & arg4 for i in xrange(5)):
        var5 += arg3 - var5 + arg3
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 6'
    print 'arg_number: 40'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
