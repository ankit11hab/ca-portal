from instagram_private_api import Client, ClientCompatPatch,ClientLoginError,errors
import random 

# user_name = 'fake27_28'
password = 'sid1234'
api = -1
short_code = 'ChOgwVQLY4m'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
media_id = 0
for letter in short_code:
    media_id = (media_id*64) + alphabet.index(letter)

# insta_id_list1 = ["digvijay.s5548", "fake27_28","fake275_28"]
insta_id_list1 = [
    {
        "username": "1alfikhan48@gmail.com",
        "password": "Qwerty@9760"
    },
    {
        "username": "rahuldua9760@gmail.com",
        "password": "Qwerty@9760"
    },
    {
        "username": "fake27_28",
        "password": "sid1234"
    }
]
for account in insta_id_list1:
    try:
        api = Client(account['username'],account['password'])
    except:
        print("Error")
    if api!=-1:
        break
if api!=-1:
    results = api.media_likers_chrono(media_id)
    # print(results['users'])
    for user in results['users']:
        print(user['username'])