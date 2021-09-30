import requests
import json 
from bs4 import BeautifulSoup
def scrap_data():
    url = "https://www.imdb.com/india/top-rated-indian-movies/?sort=rk,asc&mode=simple&page=1"
    page = requests.get(url)
    htmlcontent=page.content
    soup=BeautifulSoup(htmlcontent,"html.parser")
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    # print(tbody)
    trs=tbody.find_all("tr")
    # print(trs)
    position=0
    final_list=[]
    for tr in trs:
        position+=1
        movie_name=(tr.find("td",class_="titleColumn").a.get_text())
        # print(movie_name)
        movie_year=int((tr.find("td",class_="titleColumn").span.get_text())[1:5])
    
        movie_rating=(tr.find("td",class_="ratingColumn imdbRating").strong.get_text())
        movie_urls=(tr.find("td",class_="titleColumn").a["href"])
        urls="https://www.imdb.com" + movie_urls

        my_dict={"position":position,"name":movie_name,"year":movie_year,"rating":movie_rating,"urls":urls}

        final_list.append(my_dict)

    with open("file.json","w") as file_1:
        json.dump(final_list,file_1,indent=3)
    return final_list
scrapped=scrap_data()






















# import requests
# import json 
# from bs4 import BeautifulSoup
# import pprint
# def rotten_data():
#     url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
#     page=requests.get(url)
#     HTMLContent=BeautifulSoup(page.content,"html.parser")
#     # print(HTMLContent)
#     Tabledata= HTMLContent.find("table",class_="table")
#     # pprint.pprint(Tabledata)
#     rank=Tabledata.find_all('td',class_='bold')
#     rating=Tabledata.find_all("span",class_="tMeterScore")
#     title=Tabledata.find_all("a",class_="unstyled articleLink")
#     # pprint.pprint(title)
#     reviews=Tabledata.find_all("td",class_="right hidden-xs")
#     main_list=[]
#     for i in range(len(rank)):
#         ranking=rank[i].get_text()
#         Rating=rating[i].get_text().strip()
#         Title=title[i].get_text().strip()
#         a = Title.split()
#         urls="https://www.rottentomatoes.com"+title[i]["href"]
#         years=int(a[-1][1:5])
#         Reviews=reviews[i].get_text()
#         main_dict={"rank":ranking,"title":Title,"Ratings":Rating,"Reviews":Reviews,"url":urls,"year":years}
#         main_list.append(main_dict)
#     with open("rotten_file1.json","w") as file_1:
#         json.dump(main_list,file_1,indent=3)
#         return main_list
# first_data=rotten_data()