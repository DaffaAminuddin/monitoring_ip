import telepot
from read_unseen_email import ip
from read_unseen_email import date
from read_unseen_email import status

token = '5468371812:AAEyRk91E3o45DYpRLatgzHezYr_kVYJZm0'
receiver_id = 5235674608

bot = telepot.Bot(token)

bot.sendMessage(receiver_id, ip + "sedang" + status + date)


