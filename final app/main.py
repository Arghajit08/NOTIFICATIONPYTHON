from kivy.app import App
from kivy.uix.screenmanager import Screen
from plyer import notification
from kivy.storage.jsonstore import JsonStore
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
	def build(self):
		return Toy()

MainApp().run()
