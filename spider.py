from urllib.request import urlopen
from link_finder import LinkFinder
from base import *

class spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        spider.project_name = project_name
        spider.base_url = base_url
        spider.crawled_file = domain_name
        spider.queue_file = spider.project_name+'/queue.txt'
        spider.crawled_file = spider.project_name+'/crawled.txt'
        self.boot()
        self.crawl_page()

    @staticmethod
    def boot(self):
        create_project_dir(spider.project_name)
        create_data_files(spider.project_name, spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        print(thread_name+' now crawling '+page_url)
        print('Queue '+str(len(spider.queue)) + ' | Crawled '+str(len(spider.crawled)))
        spider.add_links_to_queue(spider.gather_link(page_url))
        spider.queue.remove(page_url)
        spider.crawled.add(page_url)
        spider.update_files()