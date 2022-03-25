
from faker import Faker

app = 'Advantage Shopping Cart'
fake = Faker(locale='en_CA')
adv_shop_cart_url = 'https://advantageonlineshopping.com/#/'
my_account_url = 'https://advantageonlineshopping.com/#/myAccount'
old_username = fake.user_name()
new_username = old_username[0:14]
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
city = fake.city()
country = fake.country()
address = fake.street_address()
phone = fake.phone_number()
province = fake.province_abbr()
postal_code = fake.postcode()