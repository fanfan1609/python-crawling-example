import wget
import requests
import os

# JISB0401-1 
# https://www.jisc.go.jp/pdfb1/PDFView/ShowPDF/oQIAAMPoeXG1jIZtd-Bs
# https://www.jisc.go.jp/pdfa7/PDFView/GetImage/hwEAAC2Ky-6M4s5Mruw8?pageNo={}&width=700&seq=0

# B0401-2
##url_pattern = "https://www.jisc.go.jp/pdfa8/PDFView/GetImage/FgEAAKUbgM6Lo8notkpb?pageNo={}&width=700&seq=0"
## https://img2.sachvui.com/images/2018/conan-2/chap-602-6.jpg
url_pattern = "https://img2.sachvui.com/images/2018/conan-2/chap-602-{}.jpg"
path = "file_1"
for i in range(1,50):
    img_url = url_pattern.format(i)
      
    myfile = requests.get(img_url,stream=True, proxies={'http': 'http://172.16.30.48:8080', 'https': 'http://172.16.30.48:8080'})
    open(os.path.join(path,str(i) + ".png"), 'wb').write(myfile.content)
    

