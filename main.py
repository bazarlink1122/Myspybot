import telebot
from kivy.app import App
from kivy.uix.label import Label

# Aapka API Token
TOKEN = '8675017242:AAFTFDKA_GzrII2qsiqratInvSq_4pfkArg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalam-o-Alaikum Saad Bhai! Aapka bot GitHub se ban kar tayyar ho chuka hai.")

class MainApp(App):
    def build(self):
        # Jab app mobile mein khulegi to ye nazar ayega
        return Label(text='Bot is Running Background...')

if __name__ == '__main__':
    # Bot ko background mein start karne ke liye
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    MainApp().run()
  
