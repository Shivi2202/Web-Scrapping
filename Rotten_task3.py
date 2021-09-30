from Rotten_task2 import*
import json
def group_by_decade (c):
    moviedec={}
    my_list=[]
    for index in c:
        mod=index%10
        decade=index-mod
        if decade not in my_list:
            my_list.append(decade)
    for i in my_list:
        moviedec[i]=[]
    for i in my_list:
        dec10=i+9
        for x in c:
            if x <= dec10 and x>=i:
                for v in c[x]:
                    moviedec[i].append(v)
                    with open("rotten_file3.json","w") as g:
                        json.dump(moviedec,g,indent=3)
    return moviedec
group_by_decade(second_data)