from bs4 import BeautifulSoup 
import requests
import re

wiki_pedia_subject = input('please enter your favorite wikipedia subject : ')
wiki_pedia_subject = wiki_pedia_subject.replace(' ' , '_')

empty_list = []

max_requests = 25
list_of_links_downloaded = []
wiki_url = 'https://en.wikipedia.org/wiki/{}'.format(wiki_pedia_subject)
flag_jan = False
while True :
    
    if wiki_url == 'https://en.wikipedia.org/wiki/Philosophy' or max_requests > 25:
        break
    response = requests.get(wiki_url)
    print(wiki_url)
    soup = BeautifulSoup( response.content , 'html.parser')
    list_of_links_in_first_pragraph = soup.find('p' ,attrs={'class': None}).find_all('a')
    

    if  bool(re.search(".jpg", wiki_url)) == flag_jan:
        list_of_links_in_first_pragraph = soup.find('p' ,attrs={'class': None}).findNext('p' , attrs={'class': None}).find_all('a')
        flag_jan = True
    
    if list_of_links_in_first_pragraph[0].get('href') == '#cite_note-1':
        wiki_url = 'https://en.wikipedia.org{}'.format(list_of_links_in_first_pragraph[1].get('href'))
        if bool(re.search(".jpg", wiki_url)) == True:
            flag_jan = True
        if wiki_url  in list_of_links_downloaded:
            print(' loop !')
            break
        else:
            list_of_links_downloaded.append(wiki_url)
            print(list_of_links_downloaded)
    else:
        wiki_url = 'https://en.wikipedia.org{}'.format(list_of_links_in_first_pragraph[0].get('href'))
        if wiki_url  in list_of_links_downloaded:
            print(' loop !')
            break
        else:
            list_of_links_downloaded.append(wiki_url)
            print(list_of_links_downloaded)
    max_requests =+ 1