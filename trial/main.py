from kivy.app import App
from kivmob import KivMob, TestIds
from kivy.uix.screenmanager import Screen
from plyer import notification
from kivy.storage.jsonstore import JsonStore
from kivy.uix.label import Label
import time
class Toy(Screen):
	def __init__(self,**kwargs):
		super(Toy,self).__init__(**kwargs)
		self.store=JsonStore('store.json')
		try:
			self.txt.text=self.store.get('Noted')['note_text']
		except KeyError:
			pass
	def save_notes(self):
		self.store.put('Noted',note_text=self.txt.text)
	def notifications(self):
		while True:
			notification.notify(title='Task Left!!',message=self.txt.text)
			time.sleep(60*60)

class MainApp(App):
	ads=KivMob('ca-app-pub-8942943599421136~1773917991')
	def build(self):
		self.ads.new_banner('ca-app-pub-8942943599421136/5247286818',top_pos=True)
		self.ads.request_banner()
		self.ads.show_banner()	
		return Toy()

MainApp().run()
