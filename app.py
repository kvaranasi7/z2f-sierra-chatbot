#import files
from flask import Flask, render_template, request
import functools
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
trainer2.train(["Hey girl", "Hello friend", "Sup dude"])
trainer2.train(["Who created you?", "The BEST Summit Group"])
#link_text = functools.partial(hyperlink_format.format)
#etotals = link_text(link='https://w3-03.ibm.com/hr/us/etotals/welcome.wss', text = 'etotals')
#'<a href="https://w3-03.ibm.com/hr/us/etotals/welcome.wss"></a>')
trainer2.train(["How do I report overtime?", 'Let me direct you to ETotals. Here is where you will schedule overtime. Please click the "eTotals" link above.'])
#trainer2.train(["How do I report overtime?", "Let me direct you to ETotals. Here is where you will schedule overtime." + <a href="https://w3-03.ibm.com/hr/us/etotals/welcome.wss"></a>])
trainer2.train(["Karthik", '<a href="https://w3-03.ibm.com/hr/us/etotals/welcome.wss"></a>'])
trainer2.train(["How do I schedule time off?","First, let you manager know. Certain managers will then have you update your PTO in Workday."])

trainer2.train(["How much PTO do I have?", "What month did you start?", "July", "Okay great, it looks like you have 6 1/2 days of paid time off. You also have 2 personal choice holidays."])
trainer2.train(["How much PTO do I have?", "What month did you start?", "June", "Okay great, it looks like you have 7 1/2 days of paid time off. You also have 3 personal choice holidays."])
trainer2.train(["How much PTO do I have?", "What month did you start?", "January", "Okay great, it looks like you have 14 days of paid time off. You also have 5 personal choice holidays."])
trainer2.train(["How much PTO do I have?", "What month did you start?", "March", "Okay great, it looks like you have 11 1/2 days of paid time off. You also have 4 personal choice holidays."])
trainer2.train(["How much PTO do I have?", "What month did you start?", "August", "Okay great, it looks like you have 5 days of paid time off. You also have 2 personal choice holidays."])
trainer2.train(["How much PTO do I have?", "What month did you start?", "October", "Okay great, it looks like you have 2 1/2 days of paid time off. You also have 2 personal choice holidays."])


trainer2.train(["Where can I find case studies on IBM and the airline industry?", "To learn more about IBM's partnership with airlines visit this link: https://www.ibm.com/industries/travel-transportation/airline"])
trainer2.train(["Where can I learn more about Predictive Maintenance and Optimization?", "To learn more about Predictive Maintenance and Optimization visit this link: https://www.ibm.com/products/ibm-maximo-asset-performance-management/predictive-maintenance-insights"])
trainer2.train(["Where can I find the new hire checklist?", "Great question, welcome to IBM! The new hire checklist can be found here: https://w3.ibm.com/w3publisher/new-hire-community/usa"])
trainer2.train(["Where can I find the GDPR required training?", "GDPR training can be found at: https://yourlearning.ibm.com/#activity/EL01-00000919"])
trainer2.train(["What is my facilitators email?", "Let me check on that. What Summit stream are you in?", "Stream 4B", "Your facilitator is Patsy Horgan, her email is horgan@us.ibm.com."])
trainer2.train(["When do we kick off NTW?", "Great question. Let me check! What stream are you?", "Stream 4B", "It looks like you will kick off NTW on Monday, November 18"])
trainer2.train(["When do we kick off CDE?", "Great question. Let me check! What stream are you?", "Stream 4B", "It looks like you will kick off CDE on Monday, December 9"])
trainer2.train(["When do we kick off LCS?", "Great question. Let me check! What stream are you?", "Stream 4B", "It looks like you will kick off LCS  on Monday, July 30"])
trainer2.train(["When do we kick off BYP?", "Great question. Let me check! What stream are you?", "Stream 4B", "It looks like you will kick off NTW on Monday, September 16"])
trainer2.train(["When do we kick off BTC?", "Great question. Let me check! What stream are you?", "Stream 4B", "It looks like you will kick off NTW on Monday, October 7"])
trainer2.train(["When do we kick off DUV?", "Great question. Let me check! What stream are you?", "Stream 4B", "It looks like you will kick off NTW on Monday, October 28"])


trainer2.train(["I am sick, where do I report this?", "You can report this in Workday. Do you need the link?", "Yes", 'Please click the "Workday" link above.'])
trainer2.train(["How much overtime do I get per GSS mission?", "Great question. It tends to vary, I would follow-up with your Summit Manager and ask him or her directly."])
trainer2.train(["Do I have any assignments due this week?", "It looks like may have something due this week. Would you like the link to the DLG?", "Yes", "https://gss-dashboard.w3bmix.ibm.com/home"])
trainer2.train(["How many calls are in this mission?", "Let me check into that, which module are you on?", "Demonstrate Unique Value", "There are two calls and one presentation in this mission."])
trainer2.train(["When do I finish GSS?", "Let me check on that. When did you start GSS?", "July 23", "Congrats on your new role! It looks like you are completing GSS January 10."])

trainer2.train(["How do I access the GSS Dashboard?", 'At the link labeled "DLG" above you will find the GSS Digial Learning Guide'])
trainer2.train(["I want to sign up for benefits, where do I go?", "Great idea! You would need to register through Fidelity, the link is listed above!"])
trainer2.train(["How do I access BluePages to update my role and contact information?", "BluePages can be accessed through w3 and the link is listed above!"])
trainer2.train(["Where can I find the required sexual harrasment training?", "That can be found through YourLearning, however, here is the link directly to it: https://yourlearning.ibm.com/#activity/EL01-00000554"])
trainer2.train(["How do I get business cards?", "You will have to get them through Bond. Here is the link: https://w3-01.ibm.com/procurement/buyondemand/common/enUS/index.html"])
trainer2.train(["Where can I find the employee checklist for first 30 days?", "The employee checklist can be access here: https://w3.ibm.com/hr/web/us/recruitment/joiningibm/"])
trainer2.train(["Where can I learn more about the employee stock purchase plan?", "Information on employee stock purchase plan can be found through: https://w3.ibm.com/hr/web/compensation/espp/"])
trainer2.train(["How can I access Zero to Foundations?", "I can redirect you, here is the link: https://w3.ibm.com/w3publisher/ibm-summit-program-zero-to-foundation"])
trainer2.train(["How do I set up my mobile phone?", "Everything you will need to know can be found through: https://apps.na.collabserv.com/communities/service/html/communityview?communityUuid=06b2242c-0b3b-405d-87bf-9d36aee89fe8"])
trainer2.train(["How do I acces YourLearning?", "The link to YourLearning is listed above!"])
trainer2.train(["What is YourLearning?", "YourLearning is a repository of modules and trainings to further develop your skillset in areas of your interest. You can also gain badges through this."])
trainer2.train(["How do I earn badges?", "Badges can be earned through completing modules within YourLearning. You can collect any badge you desire that is offered."])
trainer2.train(["I am having trouble setting up WebEx, how do I set it up?", "I am sorry to hear about the trouble. Here is a link that will guide you through: https://w3.ibm.com/help/#/article/setup_webex_acct/webex_setup_ov?requestedTopicId=webex_setup_ov"])
trainer2.train(["Where can I download Slack?", "Slack can be downloaded at this link: https://w3.ibm.com/help/#/article/slack_install/install?requestedTopicId=install"])
trainer2.train(["Where can I find discounts for IBMers?", "IBM offers it's employees a lot of great discounts. To see what is offered please click the IBM benefits link above!"])
trainer2.train(["What is IBM Money Smart?", "IBM MoneySmart is a financial program to help you make the right decisions financially. To learn more please go to: https://w3.ibm.com/hr/web/us/benefits/moneysmart/"])
trainer2.train(["How do I access Journey to Cloud training?", "Journey to Cloud can be found here : https://bundles.yourlearning.ibm.com/ibm/jtc-sales-enablement/#"])
trainer2.train(["Where can I find the GSS DLG?", "The link to the GSS DLG is listed above as DLG!"])
trainer2.train(["When does IBM match my 401k contributions?", " IBM will generally match your 401k contributions after 1 year of employment. "])
trainer2.train(["How much does IBM match? ", " IBM matches 1% of your pay no matter what. In addition, IBM will match at a rate of 100% the first 5% of your contributions. In essence, as long as you are contributing 5% of your pay to your 401k in either a Roth, Traditional, or mixed account you are reaching the full match. When you combine the 1% plus the potential 5% together, IBM’s maximum match is 6%. "])
trainer2.train(["When does IBM pay its matching contributions?", " IBM pays its contributions once a year on the December 31st or the last business day of the year if the 31st is not a business day. To receive your match you must be an employee as of December 15th of the year in question. "])
trainer2.train(["What is a Roth 401k?", "The Roth 401k option allows you to pay taxes now on the money that you contribute to your 401k, but you will never pay any taxes again on the contributed money or on any investment gains or dividends on the money in your Roth account."])
trainer2.train(["What is a traditional 401k?", " The traditional 401k options allows you to defer pay taxes on your contributions. This means that you pay no taxes today on any contributions, but you will pay taxes on the contributed amount as well as on the investment gains and dividends paid."])
trainer2.train(["What is the after tax option?", " In addition to the Roth or Traditional 401k options, you may elect to contribute up to 10% of your salary to the after tax option. Contributed dollars will not be taxed, but any investment gains and dividends will be taxed as in a traditional 401k (at earned income rates)."])
trainer2.train(["Can I change my contributions?", " Yes, you may change your contributions to your 401k as often as you like. However it may take a pay period or two for those changes to take effect."])
trainer2.train(["Can I contribute to both the Roth and Traditional options at the same time?", " Yes you can. However total contributions from yourself (not counting IBM’s matches) cannot exceed the annual limit. In 2019 this limit was $19,000. "])
trainer2.train(["What is the maximum that I can contribute to my 401k? ", "In 2019 the maximum is $19,000."])
trainer2.train(["Do I have to enroll in a 401k?", "You do not, although if you take no action after a month or two to decline to participate, IBM will automatically enroll you."])
trainer2.train(["What happens to my money if I leave IBM?", " Your money is 100% yours. You can leave it in IBM’s 401k account, or roll the money into your new employer’s 401k or IRA accounts."])
trainer2.train(["How do I change my contributions?", "Go to the Fidelity NetBenefits page and login. Once logged in, click menu and click “Retirement Savings” under IBM. On the next screen you will see a summary of your 401k. Click “contributions” on the left-hand side of the screen. Then click on “contribution amount”. You will then be directed to a screen where you can edit your contributions. Be sure to click the “Change Contribution Amount” button near the bottom of the screen if you want to save any changes."])
trainer2.train(["Where Do I book my flight?", "Listed above is the Travel link. Please click that and login and you will be able to book your flight."])
trainer2.train(["How early should I book my flight?", "It is reccomended that you book your flight at least three weeks in advance."])
trainer2.train(["Where do I make an expense report?", "Click on the link labeled Travel above and login and click on the Expense tab and create a report."])
trainer2.train(["Can I book a flight with a red marker?", "No, that flight is out of policy an cannot be booked unless you have received prior approval."])
trainer2.train(["Do I get a per diem for my trip?", "Was dinner provided?", "Yes", "Was breakfast provided", "Yes", "Unfortunately, you do not get per diem for this trip since your meals were included."])
trainer2.train(["Do I get a per diem for my trip?", "Was dinner provided?", "Yes", "Was breakfast provided", "No", "You  do get a small per diem for this trip since your breakfast costs were not included."])
trainer2.train(["Do I get a per diem for my trip?", "Was dinner provided?", "No", "Was breakfast provided", "Yes", "You  do get  per diem for this trip since your dinner costs were not included."])
trainer2.train(["Do I get a per diem for my trip?", "Was dinner provided?", "No", "Was breakfast provided", "No", "You  do get  per diem for this trip since your meals were not provided."])
trainer2.train(["What do I put in the business purpose section of an expense report?", "Required Summit Training"])
trainer2.train(["What do I do if a transaction hasn’t posted to my account yet for an expense report?", "Wait a few more business days to fill out the report until the transaction posts."])

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()


