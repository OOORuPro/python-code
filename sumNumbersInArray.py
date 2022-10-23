def sumArray(a):
    sumArr=0
    if type(a) != 0:
        for i in range(0,len(a),1):
            sumArr+=a[i]
    else:
        return sumArr
    return sumArr
print(sumArray([0]))