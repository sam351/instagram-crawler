import argparse
import json
import os
import sys
from urllib.request import urlretrieve


def usage():
    return """
        python picture_crawler.py -u cal_foodie -l 200
        The default likes number for filtering (-l --likes option) is 100.
    """


def retrieve_pictures(username, likes):
    # Open the output binary file of crawler.py
    with open('./output/output_'+username, encoding='utf-8') as fp:
        data = fp.read()
        pass
    data_list = json.loads(data)
    print("json file successfully loaded")

    # Make a new directory to save pictures
    dir_path = './output/pictures_'+username
    if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print("Directory " , dir_path ,  " Created")
    else:    
            print("Directory " , dir_path ,  " already exists")

    # retrieve & save pictures from instagram
    # (only picutres with likes more than likes numbers)
    for idx, item in enumerate(data_list):
        idx += 1

        tmp_likes = item['likes']
        if tmp_likes < likes:
            continue

        if len(item['img_urls']) != 0:
            tmp_url = item['img_urls'][0]

            title_idx = '00'+str(idx)
            title_idx = title_idx[-3:]
            urlretrieve(tmp_url, dir_path+f'/{username}_{title_idx}_{tmp_likes}Likes.png')

        if idx % 100 == 0:
            print(f'>>> picture {idx} has been successfully downloaded.')
        pass
    print(f'download successfully completed')


def arg_required(args, fields=[]):
    for field in fields:
        if not getattr(args, field):
            parser.print_help()
            sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser( description='Retrieve pictures using urls in binary', usage=usage() )
    parser.add_argument('-u', '--username', help="instagram's username")
    parser.add_argument('-l', '--likes', type=int, default=100,
                        help="number of likes - picutres with likes less than that number would be ignored")

    args = parser.parse_args()

    arg_required('username')
    retrieve_pictures(args.username, args.likes)
    # ./output/ 디렉토리에서 바이너리 파일 오픈
    # urlRetrieve
    # ./output/유저명/유저명_index_likes 으로 저장
    pass