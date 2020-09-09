#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:06:46 2020

@author: andiapriana
"""

from twitter_scraper import get_tweets
import pandas as pd

# Cari berdasarkan hastag
tweets = get_tweets("#Mulan", pages = 10)
tweets_df = pd.DataFrame()

#Running the code for one keyword and extracting data
for tweet in tweets:
    _= pd.DataFrame({'text' : [tweet['text']],
                     'isRetweet' : tweet['isRetweet'],
                     'replies' : tweet['replies'],
                     'retweets': tweet['retweets'],
                     'likes' : tweet['likes']
                     })
    tweets_df = tweets_df.append(_, ignore_index = True)
    
tweets_df.to_csv (r'/Users/andiapriana/Documents/PROJECT/data.csv',
                  index= False, header=True)