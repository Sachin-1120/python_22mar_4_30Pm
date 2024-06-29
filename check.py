def check(out,res):
    if out==res:
        print('Congratulation Test case Passes Successfully and You Score 20 Points')
    else:
        j=0
        point=0
        for i in out:
            if i==res[j]:
                point+=1
            j+=1
        print(f'You Failed But Total Point Scores={20*(point/len(out))}')
if __name__=='__main__':
    check(input('Enter Output').split(),input('Enter Expected Output'))
    
