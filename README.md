Group Project
# NLP_Song_Lyrics_Based_Recommendation
Recommendation system based on music lyrics sentiment analysis.

# LyricsBasedSongRecommendation.py
# Explanation of code, assumptions and process flow in project:

Each Lyrics in training data has three features : Lyrics,Name,Sentiment
Training data songs have been classified into three sentiments:positive, negative, not defined.

Training :
1) Created a function to identify lyrics and sentiments from training data
2) Removed stop word from lyrics
3) Created a bag of words of all lyrics
4) Found frequency distribution of all words
5) Applied features to filtered corpus and used Naive-Bayes algorithm to train the classifier on training data

Testing :
1) Applied classifier on testing data to find sentiments of song based on lyrics.
2) Calculated accuracy of the model.

Used model to identify sentiment of a string in lyrics for verification purposes

# Recommendation :
Recommendation based on basis of last five songs chosen by the user to listen(User_Last_5_Songs.txt)
1)Identified sentiments of the songs in user history.
2)Calculated the majority sentiment
3)Recommended a randomly selected song of same sentiment to user.


References: Github repositories
            Stack Overflow
            Google



# Class Assignments :
Class Assignment 1: Project2_Group7.py
1)Remove Stopwords
2)Write words along with the key term in the list.
Working on writing the resultant dictionary in the output file.

Class Assignment 2: twitter_corpus.py

