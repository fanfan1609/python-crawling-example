import wget
import requests
import os

# B0401-2
##url_pattern = "https://www.jisc.go.jp/pdfa8/PDFView/GetImage/FgEAAKUbgM6Lo8notkpb?pageNo={}&width=700&seq=0"
## https://img2.sachvui.com/images/2018/conan-2/chap-602-6.jpg
url_pattern = "https://img2.sachvui.com/images/2018/conan-2/chap-{}-{}.jpg"

series = [601, 602, 603]
for serie in series:    
    if not os.path.exists(str(serie)):
        os.makedirs(str(serie))
    for i in range(1,50):
        img_url = url_pattern.format(serie, i)        
        myfile = requests.get(img_url,stream=True, proxies={'http': 'http://172.16.30.48:8080', 'https': 'http://172.16.30.48:8080'})
        open(os.path.join(str(serie),str(i) + ".jpg"), 'wb').write(myfile.content)
    

