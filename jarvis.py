import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def Speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		Speak("Good Morning !")
	elif hour >= 12 and hour < 18:
		Speak ("Good Afternoon !")
	else:
		Speak("Good Evening !")
	Speak("I am alexa sir, Please tell me how may i help you")

def takeCommand():
	#it takes microphone input from the user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source :
		print("Listening.....")
		r.pause_threshold = 1
		audio = r. listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio,language = 'en-in')
		print(f"user said :{query}")
	except Exception as e:
		print(e)
		print("say that again Please....")
		return "None"
	return query						
if __name__ == '__main__':
		#Speak("Hello")	
		wishMe()
		if 1:
			query = takeCommand().lower()
		#logic for executing tasks based on query
			if 'wikipedia' in query:
				Speak('Searching wikipedia........')
				query = query.replace("wikipedia","")
				results = wikipedia.summary(query,sentences = 2)
				Speak("Accoring to wikipedia")
				print(results)
				Speak(results)
			elif 'open youtube' in query:
				webbrowser.open('youtube.com')
			elif 'open google' in query:
				webbrowser.open('google.com')	
			elif 'play music' in query:
				music_dir ='C:\\Users\\HP\\OneDrive\\Desktop\\music_dir' 		
				songs = os.listdir(music_dir)
				print(songs)
				Speak(songs)
				os.startfile(os.path.join(music_dir,songs[0]))
			elif 'time' in query:
				strTime=datetime.datetime.now().strftime("%H:%M:%S")
				Speak(f"Sir,the time is {strTime}")	
			elif 'sublime' in query:
				codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"	
				os.startfile(codePath)