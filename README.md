# Google_Play_Crawler

Use scrapy framework to scrape application data from the Google Play and save to Mongodb.

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
git clone https://github.com/kejane/Google_Play_Crawler.git
cd Google_Play_Crawler
scrapy crawl google -s JOBDIR=crawl_google_play/jobs
```
