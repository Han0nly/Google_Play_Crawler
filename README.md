# Google_Play_Crawler

Use scrapy framework to scrape application data from the Google Play and save to Mongodb.

I crawled about 230k apps using this script, but I know there are about 1.3 millon apps in Google Play Store, meaning that this recursive way miss part of the apps in Google Play. It may because of the Dynamic Loading/AJAX used in Google's website, but I can't parse the ajax request correctly. If you know how to crawl all apps in Google Play, please contact me at byxiaohanzhang@foxmail.com

## Prerequirement

### Install Python3

### Install Mongodb

Please Follow the [Mongodb Manual](https://docs.mongodb.com/manual/installation/)

### Install Scrapy Framework

```
python3 -m pip install scrapy
python3 -m pip install scrapy-mongodb
```

## Usage

```
git clone https://github.com/han0nly/Google_Play_Crawler.git
cd Google_Play_Crawler
scrapy crawl google -s JOBDIR=crawl_google_play/jobs
```
