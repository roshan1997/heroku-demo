from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
from simple_salesforce import Salesforce

@sched.scheduled_job('cron', day_of_week='mon', hour=13)
def scheduled_job():
	print('Connecting to the Salesforce Org')
	sf = Salesforce(username='enter your username',password='enter your password',security_token='enter security token',domain='test')
	sf.ELTON__Equipment__c.create({'GEHC_Inventory_Org__c':'AUS','ELTONGEHC__Inventory_Org__c':'AUS'})
	print('The job is completed by creating record in demo inventory')

sched.start()
