# coding: utf-8
import requests
from lxml import etree

def get_pic_urls(url, page):
    """
    function: 获取粉丝头像url
    params: url: 用户粉丝页面
    return: 
    """
    headers = {
    'cookie': 'd_c0="AODkAPPfvw2PTq-CV-jiwugUWGG9IUd3h_M=|1528994799"; q_c1=b30321c58cc945f8960ac0a8c139156c|1528994799000|1528994799000; _zap=497ad08b-9b13-4aff-b011-9a99167dd63c; _xsrf=c7decafc-68ff-4886-bd19-ef797233338b; capsion_ticket="2|1:0|10:1529374097|14:capsion_ticket|44:NjU3Mzk0ZmExY2M1NGIzMWFiODhhMGMzOGYwOGY1Mjc=|ae22de8dc491645e587ecd5a370636b382be04a76c65fdbf1c86e8f884dd382d"; z_c0="2|1:0|10:1529374103|4:z_c0|92:Mi4xa0VVcUFBQUFBQUFBNE9RQTg5LV9EU1lBQUFCZ0FsVk5sN01WWEFBRVF1bDNDdHVkQ2tEd3lqbGhsZndhVUFwSlR3|9fe089c88b78c6e7042a08ddebaa2f081320ba40239ec6a076c0e1752692d85c"; tgw_l7_route=27a99ac9a31c20b25b182fd9e44378b8',
    'referer': 'https://www.zhihu.com/people/excited-vczh/followers?page={}'.format(str(page)),
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'upgrade-insecure-requests': '1'
    }
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code == 200:
        html = r.text
        elements = etree.HTML(html)
        print(elements.xpath('//a[@class="UserLink-link"]/img/@src'))
        pic_urls = elements.xpath('//a[@class="UserLink-link"]/img/@src')
        return pic_urls
    else:
        print('Something error')

def save_pic(pic_urls):
    """
    function: 保存图片
    params: pic_urls: list, 图片的url
    return: None
    """
    j = 0
    for pic_url in pic_urls:
        with open('{}.jpg'.format(str(j)),'wb') as f:
            picture = requests.get(pic_url).content
            f.write(picture)
            print('正在保存第{}张图片'.format(str(j+1)))
            f.close()
        j = j + 1
    print('保存完成')



if __name__ == '__main__':
    pic_urls = []
    for page in range(1,10):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(str(page*30))
        pic_urls.extend(get_pic_urls(url, page))
    save_pic(pic_urls)
    print('Program done')
    