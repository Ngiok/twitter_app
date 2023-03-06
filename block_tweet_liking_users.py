import tweepy
import json

with open("C:\\Users\\valen\\Desktop\\twitter_app\\twitter_keys.txt", "r") as file:
    data = json.load(file)
    api_key = f"{data['api_key']}"
    api_secret = f"{data['api_secret']}"
    access_token = f"{data['access_token']}"
    access_token_secret = f"{data['access_token_secret']}"
    bearer_token = f"{data['bearer_token']}"
    client_id = f"{data['client_id']}"
    client_secret = f"{data['client_secret']}"

# Auth
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api =tweepy.API(auth,wait_on_rate_limit=True)
client = tweepy.Client(bearer_token)

tweet_id = ""
tweet = api.get_status(tweet_id)

api.create_block(screen_name=tweet._json["user"]["screen_name"]) #block who tweeted
users = client.get_liking_users(tweet_id)

likes_count = int(tweet._json["favorite_count"])
print("Likes count: ", likes_count, "\n")

verified_accounts = []
following_accounts = []
n=0
while(True):
    if users.meta["result_count"] == 0:
        break
    for x in users.data:
        user = api.get_user(screen_name=x)
        
        if user._json["verified"] != True and user._json["following"] != True:
            api.create_block(screen_name=x.username)
            print(x.username, "blocked")
            n=n+1
        else:    
            if user._json["verified"] == True:
                verified_accounts.append(x.username)
            
            if user._json["following"] ==  True:
                following_accounts.append(x.username)
            
    print("\nUsers remain:", likes_count-n, "\n")
    users = client.get_liking_users(tweet_id, pagination_token=users.meta["next_token"])

print("\n",n, " users blocked\n", sep="")

print("Verified accounts not blocked:\n", verified_accounts)
print("Following accounts not blocked:\n", following_accounts)
