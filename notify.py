import time
from plyer import notification
if __name__=="__main__":
	while True:
		notification.notify(
		title="Task Remaining!!",
		message="Machine Learning,Django,tkinter",
		timeout=2)
		time.sleep(3)