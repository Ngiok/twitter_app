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

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api =tweepy.API(auth,wait_on_rate_limit=True)

n = 0

blocked_users = tweepy.Cursor(api.get_blocked_ids).items()
print("Total users blocked:", sum(1 for _ in blocked_users))

