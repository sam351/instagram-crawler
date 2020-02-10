# How-to for Trip_Fashion_Recommend Team



## Install

1. instagram-crawler/inscrawler/bin/ 경로에 chromedriver.exe 다운로드

2. git bash 실행 > instagram-crawler로 디렉토리 이동 > $ cp inscrawler/secret.py.dist inscrawler/secret.py

   

   < 가상환경 세팅 >

3. 아나콘다 프롬프트 실행

4. conda create -n instagram-crawler python=3.7

   - 가상환경 이름은 instagram-crawler 대신 원하는 이름으로 변경 가능

5. conda activate instagram-crawler

6. cd  ... /instagram-crawler

   - 크롤러가 있는 디렉토리로 이동

7. pip install -r requirements.txt



8. output/ 폴더 생성
   - crawler.py 의 결과물을 저장할 디렉토리



## Example

```
python crawler.py posts_full -u (유저명) -n 100 -o ./output/output_(유저명) --fetch_likes_plays

# picture_crawler.py 는 아직 개발중
python picture_crawler.py -u (유저명) --likes 200  # 좋아요 200개 이상인 사진만 크롤링
```

