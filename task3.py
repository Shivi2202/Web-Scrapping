from task2 import*
import json
def group_by_decade (b):
    movie_dec={}
    new_list=[]
    for index in b:
        mod=index%10
        decade=index-mod
        if decade not in new_list:
            new_list.append(decade)
    for i in new_list:
        movie_dec[i]=[]
    for i in new_list:
        dec10=i+9
        for x in b:
            if x <= dec10 and x>=i:
                for v in b[x]:
                    movie_dec[i].append(v)
                    with open("decadefile.json","w") as g:
                        json.dump(movie_dec,g,indent=3)
    return movie_dec
group_by_decade(dec_arg)