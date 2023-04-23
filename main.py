import telebot
import requests
import time

token = "5976173936:AAGyFYdhSZDipQLIIWNaz5258fzNPUaNhWs"
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == "private":
        test = 'Add me to your group'
        bot.send_message(message.chat.id, test,parse_mode="Markdown")

@bot.message_handler(commands=['test'])
def test(message):
    if message.chat.type == "private":
        pass
    
    
    # give or take score with sticker and calling up,down functions:
@bot.message_handler(content_types=['sticker'])
def sticker(message):
    if message.chat.type == "supergroup":
        sticker_id = message.sticker.file_unique_id
        upstickerid = 'AgADwg4AAvn3KFI'
        downstickerid = 'AgADXQ8AAkw-KVI'
        if sticker_id == upstickerid:
            up(message)
        elif sticker_id == downstickerid:
            down(message)
        else:
            pass
    
score = {}

def up(message):
    if message.reply_to_message != None:
        username = str(message.reply_to_message.from_user.username)
        id = message.reply_to_message.from_user.id
        if username in score:
            score[str(username)]+=10
        else:
            score[username]=10
        text = f'* 10 score lost for @{username}.  ur score is {score[username]}'
        bot.send_message(message.chat.id, text)
        return score
    else:
        bot.send_message(message.chat.id, "ریپلای نکردی که یهود")

def down(message):
    if message.reply_to_message != None:
        username = str(message.reply_to_message.from_user.username)
        id = message.reply_to_message.from_user.id
        if username in score:
            score[str(username)]-=10
        else:
            score[username]= -10
        text = f'* 10 score is lost for @{username}.  ur score is {score[username]}'
        bot.send_message(message.chat.id, text)
        return score
    else:
        bot.send_message(message.chat.id, "ریپلای نکردی که یهود")

@bot.message_handler(commands=['scores'])
def table(message):
    if message.chat.type == "supergroup":
        names = list(score.keys())
        ss = list(score.values())
        
        text = ''
        for i in range(len(names)):
            text += f'- @{names[i]} : {ss[i]}\n'
            # text.append([{names[i]:int(ss[i])}])  #bug dare
            # text.sort()
            # text = str(text)
        if text == "":
            text = 'هنوز چیزی ثبت نشده'
            bot.send_message(message.chat.id, text)
        else:
            bot.send_message(message.chat.id, text)
        



while True:
    bot.polling()
    time.sleep(20)
    bot.stop_polling