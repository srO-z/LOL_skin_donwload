import os

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'}

# 获取英雄名字
url_hero_list = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
url_hero_list_resp = requests.get(url_hero_list, headers=headers).json()
json_data_hero_list = url_hero_list_resp['hero']
new_hero_name = ()
new_hero_title = ()

# 清空目标本
# a = ''
# with open('C:/Users/HuanHuan/Desktop/1.txt', 'w') as f:
#     f.write(a)

for i in json_data_hero_list:
    heroId = i['heroId']
    hero_name = i['name']
    hero_title = i['title']
    new_hero_name = hero_name
    new_hero_title = hero_title
    new_hero_id = heroId
    os.makedirs(f"C:/Users/HuanHuan/Desktop/code/Python/Item/LOL/NameDirIMG/{new_hero_name}")
    print(f"\033[2;33;40m已创建{new_hero_name}文件夹\033[0m")
    # 获取英雄皮肤
    url_hero_skin_list = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{new_hero_id}.js'
    url_hero_skin_list_resp = requests.get(url_hero_skin_list, headers=headers).json()
    json_data_skin_list = url_hero_skin_list_resp['skins']
    for j in json_data_skin_list:
        url_skin = j['mainImg']
        skin_name = j['name']
        if len(url_skin) > 0:
            new_url_skin = url_skin
            # print(new_url_skin)
            new_skin_name = skin_name.replace('/', ' ')
            # print(new_skin_name)

            resp = requests.get(new_url_skin, headers=headers)
            with open(f"C:/Users/HuanHuan/Desktop/code/Python/Item/LOL/NameDirIMG/{new_hero_name}/{new_skin_name}.jpg",
                      'wb') as f:
                f.write(resp.content)

                print(f"\033[2;34;40m已下载{new_skin_name}\033[0m")

    print(f"\033[2;32;40m{new_hero_name}的皮肤已下载完毕\033[0m")

print("\033[2;33;40m所有皮肤已下载完毕！\033[0m")
# 写入文本
#             f = open('C:/Users/HuanHuan/Desktop/1.txt', 'a')
#             f.write(skin_name)
#             f.write('\n')
#             f.write(new_url_skin)
#             f.write('\n')
#             print('成功写入')
