def main():
    #Take the input
    user_input = input("Text here: ")
    #Find the vowels and delete them
    #Create an empty string where to save the output
    tweet = []
    for i in user_input:
        if i in ["a","e","i","o","u"]:
            i = ""
        tweet.append(i)
    final_tweet = "".join(tweet)    
    print(final_tweet)

main()