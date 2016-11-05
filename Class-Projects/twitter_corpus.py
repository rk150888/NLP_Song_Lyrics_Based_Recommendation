# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:09:48 2016

@author: Admin
"""
import nltk

from nltk.corpus import twitter_samples
twitter_samples.fileids()

"""Accessing json file of positive tweets"""
positive=nltk.corpus.twitter_samples.raw("positive_tweets.json")
positive.__str__()

postwts=nltk.word_tokenize(positive)

"""Length of all the positive tweets"""
len(set(postwts))


from nltk.corpus import twitter_samples
twitter_samples.fileids()

"""Accessing json file of negative tweets"""
tweet= twitter_samples.raw("negative_tweets.json")
tweet.__str__()

tokens= nltk.word_tokenize(tweet)

"""Length of all the negative tweets"""
len(set(tokens))
