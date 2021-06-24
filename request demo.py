import requests

r=requests.get('https://imgs.xkcd.com/comics/python.pn')

with open('comic.png','wb') as f:
    f.write(r.content)
    