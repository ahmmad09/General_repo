import random
from sqlalchemy import false, true


def returnFitness(array : list ) -> int:
    fitnessCount = 8
    for i in range(8):
        if (checkRowFitness(array, i)==true):
            fitnessCount = fitnessCount - 1  
            continue
        elif (checkDiagonalFitness(array, i) == true):
            fitnessCount = fitnessCount - 1
        # else:
        #     print("no clash spotted")                
    return fitnessCount

#working fine
#returns true if value exists in same row
def checkRowFitness(array : list, index : int) -> bool:
    for j in range(8):
        if ((array[j] == array[index]) and (index!=j)):
            # print("returning true")
            return true
    return false            


def checkDiagonalFitness(array : list, index : int) -> bool:
    #checking forward diagonal
    fround = 0
    for j in range(index+1,8):
        fround = fround+1
        if ((array[j] == (array[index]+fround))  or (array[j] == (array[index]-fround))):
            # print("forward diagonal spotted")
            return true

    #checking backward diagonal
    bround = 0
    for k in range(index-1, -1, -1):
        bround = bround+1
        if ((array[k] == (array[index]+bround))  or (array[k] == (array[index]-bround))):
            # print("backward diagonal spotted")
            return true  

    return false            

def mutation(array1: list) ->list:
    array1[random.randint(0,7)] = random.randint(1,8)
    return array1


def crossOver(array1: list, array2: list) ->list:
    newList = []
    for i in range(0,8):
        if(i<=3):
            el = array1[i]
            newList.append(el)
        else:
            el = array2[i]
            newList.append(el)
    return newList                    
    
def crossoverAndMutation(array1: list, array2: list, reversed: bool) -> list: 
    # print("array1 is ")
    # print(array1)
    # print("\narray2 is ")
    # print(array2)

    if(reversed==false):
        tempList = crossOver(array1,array2)
        tempList = mutation(tempList)
        return tempList
    else:
        tempList = crossOver(array2,array1)
        tempList = mutation(tempList)
        return tempList

def choseBest(array1: list, array2: list) -> list: 
    f1 = returnFitness(array1)
    f2= returnFitness(array2)
    if (f1>=f2):
        return array1
    else:    
        return array2

        

#best 2
list1 = []
list2 = []

list3 = []
list4 = []


#initializing initial population of 4
for i in range(8):
    list1.append(random.randint(1,8))
    list2.append(random.randint(1,8))

# print("list4:")
# print(list4)
# print(returnFitness([4, 8, 7, 4, 1, 4, 1, 3]))

fl1 = 0
fl2 = 0
fl3 = 0
fl4 = 0

loopCounter = 0

print("running maximum 1000 iterations and showing the best result ..\n")


while (true):
    loopCounter = loopCounter+1        
    print("iteration " + str(loopCounter))

    list3 = crossoverAndMutation(list1,list2,false)    
    list4 = crossoverAndMutation(list1,list2,true)

    fl1 = returnFitness(list1)
    fl2 = returnFitness(list2)
    fl3 = returnFitness(list3)
    fl4 = returnFitness(list4)

    if (fl1==8):
        print("perfect sequence found:")
        print(list1)
        print("\ntotal iterations: " + str(loopCounter))
        break
    elif(fl2 == 8):
        print("perfect sequence found")
        print(list2)
        print("\ntotal iterations: " + str(loopCounter))        
        break

    if (loopCounter >=1000):
        list1 = choseBest(list1,list2)
        print("\nbest we found is:")
        print(list1)
        fit1 = returnFitness(list1)
        print("\nfitness: " + str(fit1) )
        break    



#shifting the best 2 individuals to list1 and list2

    if ((fl1 >= fl2 and fl2 >= fl3 and fl2>= fl4) or (fl2 >= fl1 and fl1 >= fl3 and fl1>= fl4)):   #f1,f2 highest
        continue
    elif (fl1 >= fl3 and fl3 >= fl2 and fl3>= fl4) or (fl3 >= fl1 and fl1 >= fl2 and fl1>= fl4):   #f1,f3 highest
        list2 = list3
    elif (fl1 >= fl4 and fl4 >= fl3 and fl4>= fl2) or (fl4 >= fl1 and fl1 >= fl2 and fl1>= fl3):   #f1,f4 highest
        list2 = list4  
    elif (fl2 >= fl3 and fl3 >= fl1 and fl3>= fl4) or (fl3 >= fl2 and fl2 >= fl1 and fl2>= fl4):   #f2,f3 highest
        list1 = list3   
    elif (fl2 >= fl4 and fl4 >= fl1 and fl4>= fl3) or (fl4 >= fl2 and fl2 >= fl1 and fl2>= fl3):   #f2,f4 highest
        list1 = list4 
    elif (fl3 >= fl4 and fl4 >= fl1 and fl4>= fl2) or (fl4 >= fl3 and fl3 >= fl1 and fl3>= fl2):   #f3,f4 highest
        list1 = list3 
        list2 = list4

