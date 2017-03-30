import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list=[]
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,"html.parser")
    for title in soup.findAll('p'):
        content = title.text
        words = content.lower().split()
        for word in words:
            word_list.append(word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_list = []
    symbols = "~`!@#$%^&*()_+-={}[“]”|\\:\"'<>?,./;"
    for word in word_list:
        for symb in symbols:
            word = word.replace(symb,"")
        if len(word)>0:
            clean_list.append(word)
    create_dict(clean_list)

def create_dict(clean_list):
    word_count={}
    for word in clean_list:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    for k,v in sorted(word_count.items(),key=operator.itemgetter(1)):
        print(k,v)

start("https://www.crummy.com/software/BeautifulSoup/bs4/doc")
