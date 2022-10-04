from email import message
import requests
import json

def print_banner():
    banner = """
    ####################################################################################################################################
    #                                                                                                                                  #     
    #  B▄██████▄BBBBB▄████████BB▄█BB███▄▄▄▄BBBBBBB███BBBBBBBB▄████████B███BBBB█▄BBB▄████████BBBB▄█BBB▄█▄BBBB▄████████BBBB▄████████B    #
    #  ███BBBB███BBB███BBBB███B███BB███▀▀▀██▄B▀█████████▄BBB███BBBB███B███BBBB███B███BBBB███BBB███B▄███▀BBB███BBBB███BBB███BBBB███B    #
    #  ███BBBB███BBB███BBBB█▀BB███▌B███BBB███BBBB▀███▀▀██BBB███BBBB█▀BB███BBBB███B███BBBB█▀BBBB███▐██▀BBBBB███BBBB█▀BBBB███BBBB███B    #
    #  ███BBBB███BBB███BBBBBBBB███▌B███BBB███BBBBB███BBB▀BB▄███▄▄▄BBBBB███BBBB███B███BBBBBBBBB▄█████▀BBBBB▄███▄▄▄BBBBBB▄███▄▄▄▄██▀B    #
    #  ███BBBB███B▀███████████B███▌B███BBB███BBBBB███BBBBB▀▀███▀▀▀BBBBB███BBBB███B███BBBBBBBB▀▀█████▄BBBB▀▀███▀▀▀BBBBB▀▀███▀▀▀▀▀BBB    #
    #  ███BBBB███BBBBBBBBBB███B███BB███BBB███BBBBB███BBBBBBB███BBBBBBBB███BBBB███B███BBBB█▄BBBB███▐██▄BBBBB███BBBB█▄BB▀███████████B    #
    #  ███BBBB███BBBB▄█BBBB███B███BB███BBB███BBBBB███BBBBBBB███BBBBBBBB███BBBB███B███BBBB███BBB███B▀███▄BBB███BBBB███BBB███BBBB███B    #
    #  B▀██████▀BBB▄████████▀BB█▀BBBB▀█BBB█▀BBBBB▄████▀BBBBB███BBBBBBBB████████▀BB████████▀BBBB███BBB▀█▀BBB██████████BBB███BBBB███B    #
    #  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB▀BBBBBBBBBBBBBBBBBBBBBBBB███BBBB███B    #
    #                                                                                                                                  #
    #   insta killer                                                                                                                   #
    #   created by kartik   version 1.0                                                                                                #
    #   follow on twitter :- https://twitter.com/Kartik7877das                                                                         #
    ####################################################################################################################################
   """


print(print_banner)




insta_id = input("please insta id : ")

#here we are collecting masked email and phone no. 

Data = (f"email_or_username={insta_id}")

url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
header ={
        "Host": "www.instagram.com",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "X-CSRFToken": "RIu9PHWxCiO1JyOtYkwWARDUa9WqfmHk",
        "X-Instagram-AJAX": "8e9ff759d0a5",
        "X-IG-App-ID": "1217981644879628",
        "X-ASBD-ID": "198387",
        "X-IG-WWW-Claim": "0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "31",
        "Origin": "https://www.instagram.com",
        "Connection": "close",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
 }

response = requests.post(url,headers=header, data=Data )

print("\nprinting status code: ", response.status_code)

print(response.json()) 


# here we are collecting information of instagram profile

header2 = {
    "Host": "i.instagram.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "X-CSRFToken": "RIu9PHWxCiO1JyOtYkwWARDUa9WqfmHk",
    "X-Instagram-AJAX": "1006310789",
    "X-IG-App-ID": "936619743392459",
    "X-ASBD-ID": "198387",
    "X-IG-WWW-Claim": "0",
    "Origin": "https://www.instagram.com",
    "Alt-Used": "i.instagram.com",
    "Connection": "keep-alive",
    "Referer": "https://www.instagram.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
    }
url2 = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={insta_id}"

response2 = requests.get(url2 ,headers=header2 )

print("\nprinting status code: ", response2.status_code)

info = response2.json()

profile = info['data']['user']['profile_pic_url_hd']
bio = info['data']['user']['biography']
name =info['data']['user']['full_name']
follower = info['data']['user']['edge_followed_by']
following = info['data']['user']['edge_follow']
post = info['data']['user']['edge_owner_to_timeline_media']['count']
id = info['data']['user']['id']
privet = info['data']['user']['is_private']
business_email = info['data']['user']['business_email']


print(f"Name :{name}")
print(f"Bio : {bio}")
print(f"follower : {follower}")
print(f"following : {following}")
print(f"no. of post : {post}")
print(f"insta id : {id}")
print(f"privet : {privet}")
print(f"business_email : {business_email}")
print(profile)











