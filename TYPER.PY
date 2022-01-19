def text():
	import speech_recognition as sr
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listening")
		r.pause_threshold = 2
		audio = r.listen(source, timeout=4, phrase_time_limit=7)
	try:
		print("recognizing..")
		txtx = r.recognize_google(audio, language='en-in')
		print(f"you said {txtx}")
	except Exception as e:
		print(e)
		return " "
	txtx = txtx.lower()
	return txtx

def write():
	import pyautogui
	outext = text()
	for a in outext:
		pyautogui.press(a)

while True:
	write()