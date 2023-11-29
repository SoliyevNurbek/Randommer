from card import Card
from finance import Finance
from misc import Misc
from name import Name
from phone import Phone
from social_number import SocialNumber
from text import Text
token = '0e4404c428d149a18f042a3f250fd746'

card = Card()
# print(card.get_card_types(api_key=token))

finan=Finance()
# print(finan.get_crypto_address_types(token))
# print(finan.get_crypto_address('Argoneum',token))
# print(finan.get_crypto_address('mpWTeDVpsPrJvY9Rd7kghdhzSepuurSmNL',token))
# print(finan.get_countries(token))
# print(finan.get_iban_by_country_code('AD',token))

mis=Misc()
# print(mis.get_cultures(token))
# print(mis.get_random_address(token,55,'en_ZA'))

nam=Name()
# print(nam.get_name(token,'fullname',55))
# print(nam.get_name_suggestions(token,'Nurbek'))
# print(nam.get_name_cultures(token))

cell=Phone()
# print(cell.generate(token,'uz',20))
# print(cell.get_IMEI(token,15))
# print(cell.is_valid(token,'+998 61 298 87 83','uz'))
# print(cell.get_countries(token))

soc_num=SocialNumber()
# print(soc_num.get_SocialNumber(token))

tx=Text()
print(tx.generate_LoremIpsum(token,'normal','words',50))










