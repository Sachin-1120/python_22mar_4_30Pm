from add import add
def test(i,j,k):
    try:
        assert add(i,j)==k ,' condition Fail'
    except AssertionError as e:
        return 1
    else:
        return 0
fail_i=0

x=[(1,2,3),(-1,2,3),(4,1,10)]
for z in x:
    i,j,k=z
    fail_i+=test(i,j,k)
print('Total Pass Condition=',len(x)-fail_i)
print('Total Fail Condition=',fail_i)
