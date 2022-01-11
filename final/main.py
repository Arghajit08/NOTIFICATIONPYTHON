from kivy.app import App
from plyer import notification
import time
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
class Toy(Screen):
	def __init__(self,**kwargs):
		super(Toy,self).__init__(**kwargs)
		self.store=JsonStore('store.json')
		self.txt.text=self.store.get('Noted')['note_text']
	def save_notes(self):
		self.store.put('Noted',note_text=self.txt.text)
	def notification(self):
		while True:
			notification.notify(title='Task Left!!',message=self.txt.text)
			time.sleep(60*60)

class MainApp(App):
	title='Task Lobby'
	def build(self):
		return Toy()

MainApp().run()