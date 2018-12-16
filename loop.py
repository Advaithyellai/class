import pyttsx3
engine = pyttsx3.init()
engine.say("Hello this is me talking")
engine.setProperty('rate',120)  #120 words per minute
engine.setProperty('volume',0.9) 
engine.runAndWait()
while (a < 10):
	a = a + 1
	print("hello", a)
print(2<2)
print(2>3)
print(2<=12)
print(34>=25)
print(1==871)
print(5!=5)
print("b" < "a")