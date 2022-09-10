from instagram_private_api import Client, ClientCompatPatch

user_name = 'fake27_28'
password = 'sid1234'

short_code = 'ChOgwVQLY4m'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
media_id = 0
for letter in short_code:
    media_id = (media_id*64) + alphabet.index(letter)

api = Client(user_name, password)
results = api.media_likers_chrono(media_id)
# print(results['users'])
for user in results['users']:
    print(user['username'])