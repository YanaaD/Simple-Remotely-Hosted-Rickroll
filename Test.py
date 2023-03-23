from playsound import playsound
import time
import requests
from threading import Thread

url = "https://audio.jukehost.co.uk/Mesu6I9rcTVL49r6Nsk5ZNb5PEjEGnPB"
response = requests.get(url)
with open("totallynotsuspicious.wav", "wb") as file:
 file.write(response.content)  

def playingmusic():
  playsound ("totallynotsuspicious.wav")

def do_thethingy():
  print ("Never gonna give you up")
  time.sleep(2.5)

  print ("Never gonna let you down")
  time.sleep(2.2)

  print ("Never gonna run around and desert you")
  time.sleep(3.9)

  print ("Never gonna make you cry")
  time.sleep(2.4)

  print ("Never gonna say goodbye")
  time.sleep(2.1)

  print ("Never gonna tell a lie")
  time.sleep(2.4)

  print ("And hurt you") 
  time.sleep(2)

t1 = Thread(target=playingmusic)
t1.start()

t2 = Thread (target=do_thethingy) 
t2.start()

