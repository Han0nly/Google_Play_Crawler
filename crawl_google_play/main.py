from scrapy.cmdline import execute

execute("scrapy crawl fda".split())


# pattern = re.compile('^.{11,}$')
# regex = Regex.from_native(pattern)
# regex.flags ^= re.UNICODE
# popular_items = collection.find({"Downloads":{'$exists': True,'$regex': pattern}},{"Link": 1 })
