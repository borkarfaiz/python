import urllib.request
import random

def download_image(url):
    name = random.randint(1,1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

download_image('http://desktopwall.net/wp-content/uploads/Funney/list10/Joker%203D%20Artwork%20Desktop%20Wallpaper-800x600.jpg')