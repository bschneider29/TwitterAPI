from textblob import TextBlob #Must upload TextBlob first / pip install textblob
import tweepy #Must upload tweepy first / pip install tweepy
import matplotlib.pyplot as plt
def tweet():
    
    consumer_key = '' #API connection hash

    consumer_secret= '' #Specifc hash to my (or a user) account

    access_token='' #Access hash

    access_secret='' #Connective hash

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Grant authorization from my account to spyder 

    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth) #Store authorization access code


    

    search_value = input("Enter Your Keyword or Twitter Handle: ") #Enter a keyword or a twitter handle
    str(search_value) #Search input
    tweets = api.search(search_value) #Search Twitter via API
    for tweet in tweets:
 
        print (tweet.text) #Print the tweets
        analysis = TextBlob(tweet.text) #Provides sentiment analysis via TextBlob
        y = analysis.subjectivity #Y value for graph
        x = analysis.polarity #X value for graph
        print(analysis.sentiment) #Print the sentiment under each tweet
        if analysis.polarity > 0 and analysis.subjectivity >= 0: #My metric is 0>POSITIVE based on polarity 'emotion'
            print("POSITIVE")
        elif analysis.polarity == 0 and analysis.subjectivity >= 0: #My metric is 0==NEUTRAL 'emotion' based on polarity
            print("NEUTRAL")     
        else:
            print("NEGATIVE") #My metric is 0<=NEGATIVE based on polarity 'emotion'
        plt.figure(figsize=(6, 4)) #Graphs each senitmental analysis
        plt.grid(True) # grid
        plt.xlabel('x-axis')      #Label               
        plt.ylabel('y-values')
        plt.scatter(x,y) # Plotting 
        plt.show 
#Use Python Console for GUI graphs in exec file form
def main():
    tweet() 

    
if __name__ == "__main__": main() 

#I did this project because my main interest is data science in social media 
