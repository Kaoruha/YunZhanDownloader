# DownLoad PDF book from YUNZHAN365
# For Study and research use only

### Active the Virtual Env
python3 -m virtualenv venv;source venv/bin/activate

### Install packages
pip install -r requirements.txt

### Edit the config
in main.py

url = "https://book.yunzhan365.com/xqcsj/yfly/mobile/index.html" ==> target_file url
service = Service("/home/kaoru/Documents/docsdownload/chromedriver") ==> WebDriver path, you could download driver for Firefox, Edge ...
x_filter = f"//html/body/div[@id='tmpContainer']/div[@id='bookContainer']/div[@class='book'][1]/div[@id='pageMask{page}']/div[@id='page{page}']/div[@class='side-content']/div[@class='side-image']" ==> xpath to get the img


### Fetch the image
python ./main.py


### Conver to pdf
if you just want to have a file in pdf, after fetch the image.
python ./combine.py