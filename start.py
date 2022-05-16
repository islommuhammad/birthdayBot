import mysql.connector
import telebot
from datetime import date

token = '5143006621:AAG_Vh1nkcWayAJZCoCHlVGbI_GxOkmVzyM'
bot = telebot.TeleBot(token)

sovga = u'\U0001F381'
star = u'\U0001F31F'

today = date.today()
day = today.strftime("%m-%d")
kun = today.strftime("%d-%m-%Y")
print (day)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="talabalar"
)


def tupleTostr(tuple):
        res = ""
        for a in tuple:
          res += star+" "+str(a)+"\n\n"
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
      "🎂*Tug'ilgan kuningiz bilan!!!* \n Bugun "+kun+". Ushbu kunda TATU Samarqand filialining quyidagi talabalari o'z tavallud kunlarini nishonlashmoqda:\n\n"+nom+"Ushbu tug'ilgan kun sohiblarini jamoamiz nomidan muborakbod etamiz!!! 🎉🎉🎉", parse_mode='Markdown')

bot.infinity_polling(skip_pending = True)