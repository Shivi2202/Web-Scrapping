from Rotten_task1 import*
import json
def group_by_year(c):
    my_list1=[]
    my_dict1={}
    for i in c:
        if i["year"] not in my_list1:
            my_list1.append(i["year"])
        my_list1.sort()
    for j in range(len(my_list1)):
        my_dict1[my_list1[j]]=[]
    for k in c:
        year=k["year"]
        for l in my_dict1:
            if year==l:
                my_dict1[l].append(k)
        # print(my_dict1)
    with open("rotten_year_file.json","w") as a:
        json.dump(my_dict1,a,indent=3)
    return my_dict1
second_data=group_by_year(first_data)
