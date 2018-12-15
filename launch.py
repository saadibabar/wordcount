import requests

url=input("Enter the URL :")
#url="http://www.saadibabar.blogspot.com"
filename=input("FileName to save the content:")
page = requests.get(url)

#print(page.content)


###################################
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content,'html.parser')




headers=soup.select('h1,h2,h3,h4,h5,h6,h7,p,img,li,a')




f= open(filename+".txt",'w')

for s in headers:
    print(s.get_text().encode("utf-8:"),file=f)
        


