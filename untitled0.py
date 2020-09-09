#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 12:15:00 2020

@author: andiapriana
"""

# List of hashtags that we're interested in
keywords = ['machinelearning', 'ML', 'deeplearning', 
            '#artificialintelligence', '#NLP', 'computervision', 'AI', 
            'tensorflow', 'pytorch', "sklearn", "pandas", "plotly", 
            "spacy", "fastai", 'datascience', 'dataanalysis']

# Lets run one iteration to understand how to implement this library
tweets = get_tweets("#machinelearning", pages = 5)
tweets_df = pd.DataFrame()

# Lets print the keys and values obtained
for tweet in tweets:
  print('Keys:', list(tweet.keys()), '\n')
  break

# Running the code for one keyword and extracting the relevant data
for tweet in tweets:
  _ = pd.DataFrame({'text' : [tweet['text']],
                    'isRetweet' : tweet['isRetweet'],
                    'replies' : tweet['replies'],
                    'retweets' : tweet['retweets'],
                    'likes' : tweet['likes']
                    })
  tweets_df = tweets_df.append(_, ignore_index = True)
tweets_df.head()

# We'll measure the time it takes to complete this process sequentially
%%time
all_tweets_df = pd.DataFrame()
for word in tqdm(keywords):
  tweets = get_tweets(word, pages = 100)
  try:
    for tweet in tweets:    
      _ = pd.DataFrame({'hashtag' : word, 
                        'text' : [tweet['text']],
                        'isRetweet' : tweet['isRetweet'],
                        'replies' : tweet['replies'],
                        'retweets' : tweet['retweets'],
                        'likes' : tweet['likes']
                      })
      all_tweets_df = all_tweets_df.append(_, ignore_index = True)
  except Exception as e: 
    print(word, ':', e)
    continue

# We'll create a function to fetch the tweets and store it for us
def fetch_tweets(word):
  tweet_df = pd.DataFrame()
  tweets = get_tweets(word, pages=100)
  try:
    for tweet in tweets:    
      _ = pd.DataFrame({'hashtag' : word, 
                        'text' : [tweet['text']],
                        'isRetweet' : tweet['isRetweet'],
                        'replies' : tweet['replies'],
                        'retweets' : tweet['retweets'],
                        'likes' : tweet['likes']
                      })
      tweet_df = tweet_df.append(_, ignore_index = True)
  except Exception as e: 
    print(word, ':', e)
  return tweet_df

# We'll run this in parallel with 4 subprocesses to compare the times
%%time
with Pool(4) as p:
    records = p.map(fetch_tweets, keywords)