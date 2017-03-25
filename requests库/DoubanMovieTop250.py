import requests
from bs4 import BeautifulSoup
import re

html_response = requests.get("https://movie.douban.com/top250?start=100&filter=")
html_response.encoding = html_response.apparent_encoding
soup = BeautifulSoup(html_response.text, "html.parser")
movies_list = soup.find('ol', 'grid_view')

for per_movie in movies_list.find_all('li'):
    info_dic = {}
    info_dic['rank'] = per_movie.find('em').string
    string_ = ''
    for string in per_movie.find('div', 'info').find('a').stripped_strings:
        string_ += string
        info_dic['name'] = re.sub('\xa0', ' ', string_)
    # string_ = ''
    # for string in per_movie.find('div', 'bd').find('p').stripped_strings:
    #     string_ += string
    #     info_dic['intro'] = string_.split('\xa0')
    info_dic['score'] = per_movie.find('span', 'rating_num').string
    if per_movie.find('span', 'inq'):
        info_dic['quote'] = per_movie.find('span', 'inq').string

    print(info_dic)



