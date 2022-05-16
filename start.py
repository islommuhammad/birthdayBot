import mysql.connector
import telebot
from datetime import date

token = '5143006621:AAG_Vh1nkcWayAJZCoCHlVGbI_GxOkmVzyM'
bot = telebot.TeleBot(token)

today = date.today()
day = today.strftime("%m-%d")
print (day)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="talabalar"
)


def tupleTostr(tuple):
        res = " "
        for a in tuple:
          res += str(a)+",\n"
        return res

name = mydb.cursor()
group = mydb.cursor()
name.execute("SELECT Guruh, Toliq_ismi FROM students WHERE Tugilgan_sana Like '%-"+day+"'") 

ism = [ x[1] for x in name.fetchall()]

#print(myresult)

nom = tupleTostr(ism)
print(nom)
@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_photo(-321996347, photo=open('rasm.jpg', 'rb'),caption=
      "\nQuyidagi talabalar bugun tugulgan kunlarini nishonlamoqda: \n "+nom)

bot.infinity_polling(skip_pending = True)