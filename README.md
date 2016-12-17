# Senior Project for Rachel Malloy and Kasia McLellan

Our project is called 'Methods for Identifying Brand Logos in Images Shared on Social Media'. We analyze whether or not images pulled from Twitter contain a brand logo by using three different computer vision classifiers. We also collected a sentiment score from the text of each tweet. 

## Getting Started

These instructions will get you a copy of our project up and running on your local machine for development and testing purposes. 

### Prerequisites

Install Matlab on your device

```
Matlab download link: https://www.mathworks.com/products/new_products/latest_features.html?s_tid=hp_spot_R2016b_0914
```

Install Vlfeat on your device

```
VLFeat download link: http://www.vlfeat.org/download.html
```

Set up your database and adapter (we used Postgresql with psycopg2)

```
postgresql download link: https://www.postgresql.org/download/
psycopg2 download link : https://pypi.python.org/pypi/psycopg2
```

Get Tweepy (Twitter API) Access

```
Create a Twitter account to get a secret key and credentials for collecting tweets. 
Tweepy Docs: http://tweepy.readthedocs.io/en/v3.5.0/
```

Get Watson Access

```
A session key is needed for the Alchemny sentiment analysis API.
Watson Cloud Developer portal: https://www.ibm.com/watson/developercloud/
```

### Installing

To set up your database, create an empty database called sentimentdb, and put the db path in line 8 in the sentiment_declarative file.

```
Example path: 'postgresql+psycopg2://postgres@localhost:5432/sentimentdb'
```

To create the tables and their columns, run sentiment_declarative.py 

```
Enter your watson secret credentials to use the Watson alchemy api in line 11.
Enter your tweepy secret credentials and keys in lines 22-25. 
Run the command python sentiment_declaractive.py
```

To populate the sentimentdb database you just created, run sentiment_harvester.py

```
Run the command: python sentiment_harvester.py
```

To analyze the images and populate the 'contains_logo' column, run'CODandSiftBoolean.m'

```
Make sure your database is linked to matlab by using it's database linking tool before running this program in matlab. 
```

To extract any data or statistics, query the database 

```
Example query: SELECT COUNT(*) FROM tweet WHERE sentiment='positive';
```


## Authors

* **Kasia McLellan** - *Initial work* - [kawwsha](https://github.com/kawwsha)

* **Rachel Malloy** - *Initial work* - [rmalloy2](https://github.com/rmalloy2)

## Acknowledgments

* Thanks for a great semester Dr. Kim! 
