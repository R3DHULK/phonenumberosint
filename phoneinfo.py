import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
logo = '''
  _  _      _ _   _       ___     _     _   
 | || |_  _| | |_( )___  / _ \ __(_)_ _| |_ 
 | __ | || | | / //(_-< | (_) (_-< | ' \  _|
 |_||_|\_,_|_|_\_\ /__/  \___//__/_|_||_\__|
            created by R3DHULK                         

'''
print(logo)
number = input("Enter Victim's Phone Number : ")
phone_number = phonenumbers.parse(number)

print (geocoder.country_name_for_number(phone_number,'en'))
# print (geocoder.description_for_number,(phone_number,'en'))
# print (geocoder.description_for_valid_number,(phone_number,'en'))

print(carrier.name_for_number(phone_number,'en'))
# print(carrier.name_for_valid_number(phone_number,'en'))
