# DownLoad PDF book from YUNZHAN365
## For Study and research use only

### Active the Virtual Env
``` python
python3 -m virtualenv venv;source venv/bin/activate
```

### Install packages
``` python
pip install -r requirements.txt
```

### Edit the config
in main.py

#### Target File url
url = "https://book.yunzhan365.com/xqcsj/yfly/mobile/index.html"

#### WebDriver path, you could download driver for Firefox, Edge ...
service = Service("/home/kaoru/Documents/docsdownload/chromedriver")

#### xpath to get the image, maybe other page use the different rule
x_filter = f"//html/body/div[@id='tmpContainer']/div[@id='bookContainer']/div[@class='book'][1]/div[@id='pageMask{page}']/div[@id='page{page}']/div[@class='side-content']/div[@class='side-image']"


### Fetch the image
``` python
python ./main.py
```


### Conver to pdf
if you just want to have a file in pdf, after fetch the image.
``` python
python ./combine.py
```
