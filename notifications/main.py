from kivy.app import App
from plyer import notification
import time
class Toy(App):
	while True:
		notification.notify(title='Task Left!!',app_icon="/home/arghajit/Desktop/notifications/icon.ico",message='Machine Learning,BOT studies,tkinter')
		time.sleep(60*60)
Toy().run()
