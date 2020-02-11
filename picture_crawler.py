import json
from urllib.request import urlretrieve
import os
user_name = 'fashionsnapcom'

# 1. Open the output binary file of crawler.py
with open('./output/output_'+user_name, encoding='utf-8') as fp:
    data = fp.read()
    pass
data_list = json.loads(data)
# data_list  # check the result
# len(data_list)  # check the result
# len(data_list[101]['img_urls'])  # check the result

# 2. Make a new directory to save pictures
dir_path = './output/pictures_'+user_name
if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print("Directory " , dir_path ,  " Created ")
else:    
        print("Directory " , dir_path ,  " already exists")

# 3. retrieve & save pictures from instagram
for idx, item in enumerate(data_list):
    idx += 1
    if len(item['img_urls']) != 0:
        tmp_url = item['img_urls'][0]
        urlretrieve(tmp_url, dir_path+f'/{user_name}_{idx}.png')

    if idx % 100 == 0:
        print(f'>>> picture {idx} has been successfully downloaded.')
    pass
print(f'download successfully completed')


# ---------- ignore : To be developed (for running in prompt) -----------
# < Example : python picture_crawler.py -o output_(유저명) --likes 200 >
if __name__ == '__main__':
    # ./output/ 디렉토리에서 바이너리 파일 오픈
    # urlRetrieve
    # ./output/유저명/유저명_index_likes 으로 저장
    pass


