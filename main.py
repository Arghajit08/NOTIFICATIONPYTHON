
##DEVELOP MOBILE KIVY APP

from kivy.app import App
from kivy.lang import Builder
from plyer import notification
import time
KV = """

Button:
	text:"Alert"
	size_hint: .2,.1
	pos_hint:{"center_x":.5,"center_y":.5}
	on_release:app.notification()

"""
class Main(App):
	def build(self):
		return Builder.load_string(KV)
	def notification(self):
			notification.notify(
				title="Task Remaining!!",
				app_icon="logo.png",
				message="Machine Learning,Django,tkinter",
				timeout=2,)
	
Main().run()
