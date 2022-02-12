import telebot
import requests
from bs4 import BeautifulSoup

url = 'https://стопкоронавирус.рф/information/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('div', class_='cv-section__content')

quote = quotes[1].find('cv-spread-overview')

'''string = str(quote)'''

i = 0

some = soup.find_all(string="стопкоронавирус")
print(soup.prettify())

regions = []
stats = []
'''
while i < len(string):
    region_start = string.find('code',i)+7
    region = string[region_start:region_start+6:1]

    regions.append(region)

    sick_incr_start = string.find('sick_incr',i)+11
    sick_incr = string[sick_incr_start:sick_incr_start+5:1]

    healed_incr_start = string.find('healed_incr',i)+13
    healed_incr = string[healed_incr_start:healed_incr_start+5:1]

    died_incr_start = string.find('died_incr',i)+11
    died_incr = string[died_incr_start:died_incr_start+2:1]

    stats.append([sick_incr,healed_incr,died_incr])
 
    i = died_incr_start+10

print(regions)'''
'''
answer = 'В Москве за последние сутки:\nЗаболело: ' + sick_incr + '\nВыздоровело: ' + healed_incr + '\nУмерло: '  + died_incr
answer += '\n\n Данные взяты с сайта Стопкоронавирус.рф'

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "/covid":
        bot.send_message(message.from_user.id, answer)

bot.polling(none_stop=True, interval=0)

print('region: ' + region)
print('sick incr: ' + sick_incr)
print('healed incr: ' + healed_incr)
print('died incr: ' + died_incr)

'''