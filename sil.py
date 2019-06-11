import io
from urllib.parse import urljoin
import requests
import urllib.request

urllib.request.urlretrieve("https://www.instagram.com/p/BtBk9ibFtBj/media", "d:/local-filename1.jpg")

def get_photo(instagram_photo_link):
    url = urljoin(instagram_photo_link, 'media/?size=l')
    response = requests.get(url)
    if not response.ok:
        raise ValueError()
    file_like = ('photo.jpg', io.BytesIO(response.content))
    return file_like

def main():
    link = 'https://www.instagram.com/p/BtBk9ibFtBj/'
    #get_photo(link)


if __name__ == '__main__':
    main()

