import requests
from bs4 import BeautifulSoup

def list_movies(max_page,file_name):
    page = 1
    fi = open(file_name+".txt",'w')
    while(page<=max_page):
        url = 'https://yts.ag/browse-movies?page='+str(page)
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html,"html.parser")
        for movie in soup.findAll('a',{'class':'browse-movie-title'}):
            fi.write(movie.string+"\n")
        page+=1
    fi.close()
list_movies(1,'movies')
