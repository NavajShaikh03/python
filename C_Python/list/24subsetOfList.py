lst = [1,2,3,4,5,6,7,8,9,10]    # list devide into sublist parttion 
lst.sort()

tem_sub_list = []    # this is tem list when the creat sub the clear it 

allSublist = []
for i in range(0,len(lst),2):
    tem_sub_list.append(i)
    for j in range(i+1,len(lst)):
        tem_sub_list.append(j)
        break
    allSubList = allSublist + tem_sub_list
    print(tem_sub_list)    
    allSublist.append(tem_sub_list)
    tem_sub_list.clear()             
print(allSublist)   # this print but empty why not ??
 
 
# other way to solve question      using list comprenssion

ans = [[i,j]for i in lst for j in lst if i-j ==3 or i-j ==-3 ]    ## this is list compression add the list to sub_list
print(ans)  
        
        