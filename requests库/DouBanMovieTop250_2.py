from bs4 import BeautifulSoup
import requests
import time
import re

def get_url(start):
    string = 'https://movie.douban.com/top250?start='+str(start)+'&filter='
    return string

def get_information(url):
    try:
        html_response = requests.get(url)
        html_response.raise_for_status()
        soup = BeautifulSoup(html_response.text, "html.parser")
        movie_list = []
        for per_movie in soup.find('ol', 'grid_view').find_all('li'):
            info_dic = {}
            info_dic['rank'] = per_movie.find('em').string
            _string = ''
            for string in per_movie.find('div', 'info').find('a').stripped_strings:
                _string += string
                info_dic['name'] = re.sub('\xa0', ' ', _string)
            _string = ''
            for string in per_movie.find('div', 'bd').find('p').stripped_strings:
                _string += string
                info_dic['intro'] = re.sub('\xa0', ' ', _string)
            info_dic['score'] = per_movie.find('span', 'rating_num').string
            if per_movie.find('span', 'inq'):
                info_dic['quote'] = per_movie.find('span', 'inq').string
            movie_list.append(info_dic)
        return movie_list
    except:
        return False


if __name__ =='__main__':
    start = 0
    f = open('MovieTop250.doc', 'a', encoding='utf-8')
    while start < 250:
        url = get_url(start)
        movie_list = get_information(url)
        if movie_list:
            for movie in movie_list:
                txt = '排名：' + movie['rank'] + '  电影名称：' + movie['name'] + '\n' + movie['intro'] + '\n' + '豆瓣评分：' + movie['score'] + '\n' + '评论：' + movie.get('quote', '暂无评论') + '\n\n'
                f.write(txt)
            start += 25
            print('获取%d成功' % start)
            time.sleep(1)
        else:
            print('获取%d失败' % start)
            break
    else:
        print('获取成功')
    f.close()


