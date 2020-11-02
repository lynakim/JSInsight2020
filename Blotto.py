import numpy as np
import pandas as pd


df = pd.read_csv ('/Users/jackknickrehm/Desktop/Python/castle-solutions-4.csv')
df1 = pd.read_csv ('/Users/jackknickrehm/Desktop/Python/Random10digits.csv')
array1=np.array(df)
array1=np.delete(array1,[276,851],0)
array1=array1.astype(float)
array1=array1.astype(int)
array2=np.array(df1)
arr=np.vstack((array1,array2))


def first_consecutive_negative_island(a, N):
    mask = np.convolve(np.less(a,0),np.ones(N,dtype=int))>=N
    if mask.any():
        return mask.argmax() - N + 2
    else:
        return 0

def testOne(sub,remain):
    wins=0
    for x in range(np.shape(remain)[0]):
        total=0
        for y in range(np.shape(sub)[0]):
            if int(float(sub[y]))>int(float(remain[x,y])):
                total+=y+1
        B=first_consecutive_negative_island(sub-remain[x], 3)
        A=first_consecutive_negative_island(remain[x]-sub, 3)
        C=sum(np.where(remain[x]-sub == 0)[0])
        if A<B:
            add=sum(range(A, 10, 1))
            min=sum(np.argwhere((remain[x]-sub)>0)+1)
            total=total+add-min
        if A>B:
            min=sum(np.argwhere((sub-remain[x])>0)+1)
            total=total-min
        if (total>(55-C)/2):
            wins+=1
    return(wins)

#test=np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
#print(testOne(test,arr))
print(np.shape(arr))
def testAll(arr):
    wins=np.zeros(np.shape(arr)[0])
    wins[0]=testOne(arr[0],arr[0:])
    for x in range(len(arr)-1):
        win=testOne(arr[x+1],np.vstack((arr[:x],arr[x+1:])))
        wins[x]=win
        print(x)
    return(wins)
wins=testAll(arr)
print(wins)
max_index = np.argmax(wins, axis=0)
print(max_index)
print(arr[max_index])

saveArr=np.ones((np.shape(arr)[0],np.shape(arr)[1]+1))
print(np.shape(saveArr))
saveArr[:,:np.shape(arr)[1]]=arr
saveArr[:,np.shape(arr)[1]]=wins
print(saveArr)
np.savetxt("/Users/jackknickrehm/Desktop/Python/ResultsBlottoAll.csv", saveArr, delimiter=",")
