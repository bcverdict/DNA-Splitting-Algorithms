import time

main_dict = {}
def main(arr):
    index = 0
    for i in arr:
        if i not in main_dict:
            tempArr = [[]]
            tempArr[0]= arr[0:index]
            main_dict[i]=(index, tempArr)
        elif main_dict[i][1]==[[]]:
            tempArr=[arr[main_dict[i][0]+1:index]]
            main_dict[i]=(index,tempArr)
        elif index-main_dict[i][0]-1:
            tempArr = main_dict[i][1]
            tempArr.append(arr[main_dict[i][0]+1:index])
            main_dict[i]=(index,tempArr)
        else:
            tempIndex = main_dict[i][0]+1
            main_dict[i]=(tempIndex,tempArr)
        index+=1
    for i in main_dict:
        if main_dict[i][0]<index-1:
            if main_dict[i][1]==[[]]:
                tempArr=[arr[main_dict[i][0]+1:index]]
                main_dict[i]=(index,tempArr)
            else:
                tempArr = main_dict[i][1]
                tempArr.append(arr[main_dict[i][0]+1:index])
                main_dict[i]=(index,tempArr)
#-----------------------------------------------------------
no_items_dict = {}
def main_no_items(arr, length):
    index = 0
    for i in arr:
        if i not in no_items_dict:
            if index!=0:
                no_items_dict[i]=([index],index)
            else:
                no_items_dict[i]=([],index)
        elif no_items_dict[i][1]<index-1:
            tempArr=no_items_dict[i][0]
            tempArr.append(index-no_items_dict[i][1]-1)
            no_items_dict[i]=(tempArr,index)
        else:
            tempArr = no_items_dict[i][0]
            tempInd = no_items_dict[i][1]+1
            no_items_dict[i]=(tempArr,tempInd)
        index+=1
    for i in no_items_dict:
        if no_items_dict[i][1]!=length-1:
            tempArr=no_items_dict[i][0]
            tempArr.append(length-no_items_dict[i][1]-1)
            no_items_dict[i]=(tempArr,index)
#-----------------------------------------------------------
speed_up_dict = {}
def main_speed_up(arr, length):
    index = 0
    for i in arr:
        endArrSize=length-index-1
        if i not in speed_up_dict:
            if index!=0:
                if endArrSize: #true when is not last element
                    speed_up_dict[i]=([index,endArrSize],index)
                else: #is last element
                    speed_up_dict[i]=([],index)
            else: #if is first element
                speed_up_dict[i]=([endArrSize],index)
        elif speed_up_dict[i][1]<index-1:
            tempArr = speed_up_dict[i][0]
            if not tempArr: #fires when dict[i][0] is empty
                tempArr=[endArrSize]
            elif len(tempArr)==1: #fires when dict[i][0] is 1
                tempArr=[index-speed_up_dict[i][1]-1,endArrSize]
            elif index!=length-1: #is not last element
                tempArr = tempArr[0:len(tempArr)-1]+[index-speed_up_dict[i][1]-1,endArrSize]
            else: #is last element
                tempArr = tempArr[0:len(tempArr)-1]+[index-speed_up_dict[i][1]-1]
            speed_up_dict[i]=(tempArr,index)
        else: #next to each other
            tempArr=speed_up_dict[i][0]
            if (not tempArr) or len(tempArr)==1: #fires when dict[arr[0]][0] is empty
                tempArr=[endArrSize]
            elif endArrSize:
                tempArr[len(tempArr)-1]-=1
            else:
                tempArr=tempArr[0:len(tempArr)-1]
            tempInd = speed_up_dict[i][1]+1
            speed_up_dict[i]=(tempArr,tempInd)
        index+=1
#-----------------------------------------------------------
conquer_dict={}
def divide_conquer(arr, index, length):
    if(len(arr)>1):
        divide_conquer(arr[0:len(arr)//2],index, length)
        divide_conquer(arr[len(arr)//2:len(arr)], index+len(arr)//2, length)
    else:
        if arr[0] not in conquer_dict:
            if index!=0:
                conquer_dict[arr[0]]=([index],index)
            else:
                conquer_dict[arr[0]]=([],index)
        elif conquer_dict[arr[0]][1]<index-1:
            tempArr=conquer_dict[arr[0]][0]
            tempArr.append(index-conquer_dict[arr[0]][1]-1)
            conquer_dict[arr[0]]=(tempArr,index)
        else:
            tempArr = conquer_dict[arr[0]][0]
            tempInd = conquer_dict[arr[0]][1]+1
            conquer_dict[arr[0]]=(tempArr,tempInd)
    if(len(arr)==length):
        for i in conquer_dict:
            if conquer_dict[i][1]!=length-1:
                tempArr=conquer_dict[i][0]
                tempArr.append(length-conquer_dict[i][1]-1)
                conquer_dict[i]=(tempArr,index)
#---------------------------------------------------
conquer_dict2={}
def divide_conquer2(arr, index, length):
    if(len(arr)>1):
        divide_conquer2(arr[0:len(arr)//2],index, length)
        divide_conquer2(arr[len(arr)//2:len(arr)], index+len(arr)//2, length)
    else:
        endArrSize=length-index-1
        if arr[0] not in conquer_dict2:
            if index!=0:
                if endArrSize: #true when is not last element
                    conquer_dict2[arr[0]]=([index,endArrSize],index)
                else: #is last element
                    conquer_dict2[arr[0]]=([],index)
            else: #if is first element
                conquer_dict2[arr[0]]=([endArrSize],index)
        elif conquer_dict2[arr[0]][1]<index-1:
            tempArr = conquer_dict2[arr[0]][0]
            if not tempArr: #fires when dict[arr[0]][0] is empty
                tempArr=[endArrSize]
            elif len(tempArr)==1: #fires when dict[arr[0]][0] is 1
                tempArr=[index-conquer_dict2[arr[0]][1]-1,endArrSize]
            elif index!=length-1: #is not last element
                tempArr = tempArr[0:len(tempArr)-1]+[index-conquer_dict2[arr[0]][1]-1,endArrSize]
            else: #is last element
                tempArr = tempArr[0:len(tempArr)-1]+[index-conquer_dict2[arr[0]][1]-1]
            conquer_dict2[arr[0]]=(tempArr,index)
        else: #next to each other
            tempArr=conquer_dict2[arr[0]][0]
            if (not tempArr) or len(tempArr)==1: #fires when dict[arr[0]][0] is empty
                tempArr=[endArrSize]
            elif endArrSize:
                tempArr[len(tempArr)-1]-=1
            else:
                tempArr=tempArr[0:len(tempArr)-1]
            tempInd = conquer_dict2[arr[0]][1]+1
            conquer_dict2[arr[0]]=(tempArr,tempInd)
#-----------------------------------------------------------    
def input_for_divide():
    inputFile = input("Enter file name: ");
    inputFile = open(inputFile)
    arr = []
    index = 0
    for line in inputFile:
        for i in line.split():
            arr.append(i)
            
    last_time = time.time()
    main(arr)
    print('Iterative took           {} seconds'.format(time.time()-last_time))
    
    last_time = time.time()
    main_no_items(arr,len(arr))
    print('Iterative_no_items took  {} seconds'.format(time.time()-last_time))

    last_time = time.time()
    main_speed_up(arr, len(arr))
    print('Iterative_speed_up took  {} seconds'.format(time.time()-last_time))
    
    last_time = time.time()
    divide_conquer(arr,0,len(arr))
    print('First conquer took       {} seconds'.format(time.time()-last_time))
    
    last_time = time.time()
    divide_conquer2(arr, 0, len(arr))
    print('Second conquer took      {} seconds'.format(time.time()-last_time))
    
    last_time = time.time()
#-----------------------------------------------------------    
input_for_divide()
'''
print('main dict: ',main_dict)
print('main_no_items dict: ',no_items_dict)
print('main_speed_up dict: ',speed_up_dict)
print('conquer_dict:',conquer_dict)
print('conquer_dict2:',conquer_dict2)
'''
