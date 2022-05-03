# Search-Engine-Project
Shortcut Links to:

* [Web Scraper using Scrapy](https://github.com/vpagador/publications-IR-project/blob/main/search_engine_project/crawler/crawler/crawler/spiders/publication_spider.py)
* [Indexer](https://github.com/vpagador/publications-IR-project/blob/main/query_processor/query_processor.py)
* [Query Processor](https://github.com/vpagador/publications-IR-project/blob/main/query_processor/query_processor.py)
* [Serach Engine](https://github.com/vpagador/publications-IR-project/blob/main/query_processor/search_engine.py)
* 

Brief Description:
This project is an coding exercise that aims to create a simple search engine from three parts: a web scrapper, an indexer and a query processor. 

* Webscraper
The scraper is built using Scrapy - a python framework which helps make powerful, yet simple web scrapers - which is used to scrape items from the following website: https://pureportal.coventry.ac.uk/en/organisations/school-of-computing-electronics-and-maths/publications/ 
The items that are scraped are the title, publication link, author, author link, date of publication and the article and these are stored in a JSON file called 'publications.json'.

* Indexer
This function indexes all keywords found amongst the publication titles in the json file using the nltk package to filter out stopwords and recording the number of document occurances for each word as a key-value pair. Essentially, this follows an inverted indexing pattern where the document occurances of each word are recorded, rather than the word occurance of each document as in an occurance matrix. The former method is far more efficient for data space than the latter. The indexer is recorded as a JSON file called indexer.json.

* Query Processor/Search Engine
This function takes in user input (that can come in multiple words) and references each word to the indexer and returns all the listed documents along with other associated items i.e. abstract, authors etc as results. 

Quick Demo:

https://user-images.githubusercontent.com/80417833/166460306-b869a7bb-678f-4272-9eb4-917472eada2d.mp4

