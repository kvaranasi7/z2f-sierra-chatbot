#import files
from flask import Flask, render_template, request
import functools
import xlrd
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#from chatterbot.storage import SQLStorageAdapter
app = Flask(__name__)

bot = ChatBot("Karthik")
trainer1 = ChatterBotCorpusTrainer(bot)
#set_trainer(ListTrainer)
trainer2 = ListTrainer(bot)
#bot.set_trainer(ChatterBotCorpusTrainer)
#trainer1.train("chatterbot.corpus.english")
loc = ("finalz2f.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0) 
print (sheet.nrows)
print (sheet.ncols)
print (sheet.cell_value(1,3))
#prints questions
for i in range(1,65):
	
	if sheet.cell_value(i,6) != '':
		trainer2.train([sheet.cell_value(i,1), sheet.cell_value(i,2), sheet.cell_value(i,3),sheet.cell_value(i,4),sheet.cell_value(i,5),sheet.cell_value(i,6)])
	elif sheet.cell_value(i,4) != '':
		trainer2.train([sheet.cell_value(i,1), sheet.cell_value(i,2), sheet.cell_value(i,3),sheet.cell_value(i,4)])
	else:
		trainer2.train([sheet.cell_value(i,1), sheet.cell_value(i,2)])

	

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()


