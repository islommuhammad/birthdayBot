
import telebot
import db
from datetime import date

token = '5143006621:AAG_Vh1nkcWayAJZCoCHlVGbI_GxOkmVzyM'
bot = telebot.TeleBot(token)

sovga = u'\U0001F381'
star = u'\U0001F31F'
# iconlar uchun link   https://emojipedia.org

today = date.today()
day = today.strftime("%m-%d")
kun = today.strftime("%d-%m-%Y")
print (day)




def tupleTostr(tuple):
        res = ""
        for a in tuple:
          res += star+" "+str(a)+"\n\n"
        return res

name = db.mydb.cursor()
group = db.mydb.cursor()
name.execute("SELECT Guruh, Toliq_ismi FROM students WHERE Tugilgan_sana Like '%-"+day+"'") 

ism = [ x[1] for x in name.fetchall()]

#print(myresult)

nom = tupleTostr(ism)
print(nom)
#@bot.message_handler(commands=['start'])
#def send_message(message):
bot.send_photo(-1001521695040, photo=open('/var/www/html/birthdayBot/rasm.jpg', 'rb'),caption=
    "🎂 *Tug'ilgan kuningiz bilan!!!* \n Bugun "+kun+". Ushbu kunda TATU Samarqand filialining quyidagi talabalari o'z tavallud kunlarini nishonlashmoqda:\n\n"+nom+"Ushbu tug'ilgan kun sohiblarini jamoamiz nomidan muborakbod etamiz!!! 🎉🎉🎉\n\n ©️ Copyright: @telesto\_edu", parse_mode='Markdown')

#bot.infinity_polling(skip_pending = True)
