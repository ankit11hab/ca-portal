from instagram_private_api import Client, ClientCompatPatch,ClientLoginError,errors
import random 

# user_name = 'fake27_28'
password = 'sid1234'

short_code = 'ChOgwVQLY4m'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
media_id = 0
for letter in short_code:
    media_id = (media_id*64) + alphabet.index(letter)

insta_id_list1 = ["fake27_28","digvijay.s5548","fake275_28"]
for id in insta_id_list1:
    api = Client(id,password)
    if not(api):
        insta_id_list1.remove(id)
        api=Client(id, password)
    else:
        print("working")
        break

results = api.media_likers_chrono(media_id)
# print(results['users'])
# for user in results['users']:
#     print(user['username'])