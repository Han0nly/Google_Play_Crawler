from scrapy.cmdline import execute

execute("scrapy crawl google -s JOBDIR=crawl_google_play/jobs".split())
