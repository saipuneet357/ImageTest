# try:
#     from googlesearch import search
# except ImportError:
#     print("No module named 'google' found")
#
#
# def list_of_sites(query):
#     site_list = search(query, tld="co.in", num=10, stop=10, pause=2)
#     return site_list
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler
from icrawler import ImageDownloader
from six.moves.urllib.parse import urlparse
import base64


class MyImageDownloader(ImageDownloader):

    def get_filename(self, task, default_ext):
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in [
                    'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
            ]:
                extension = default_ext
        else:
            extension = default_ext
        # works for python3
        filename = 'chanakya'
        return '{}.{}'.format(filename, extension)


def crawl(key):
    google_crawler = BingImageCrawler(downloader_cls=MyImageDownloader, storage={
                                      'root_dir': 'E:\capi\opencv\ImageTest'})
    google_crawler.crawl(keyword=key, max_num=1)
    return
