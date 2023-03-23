# Simple-Remotely-Hosted-Rickroll
In this quick tutorial you will learn to make a simple 16 second Rickroll that plays music and prints text simultaneously using the playsound, requests and threading modules in Python! 

**Step 1:** The first thing we need to do is to import all necessary modules:

```python
from playsound import playsound
import time
import requests
from threading import Thread
```

**Step 2:** Then we will use the requests module to download our audio file and give it a name:
 
```python
url = "YOUR_LINK_HERE"
response = requests.get(url)
with open("totallynotsuspicious.wav", "wb") as file:
 file.write(response.content)  
```
**(this works for **.mp3** and **.wav** files)*

*Note that you can add your own direct URL link or simply use the one already provided in the original script (Test.py file)*

If you choose to create your own direct link to an audio file of your choosing i suggest you check out this great tutorial by **Moutard3** : https://gist.github.com/Moutard3/b925b090ab1d6d20a5d20f054bae7bca 

**Step 3:** 
 We will create a function that plays our previously created audio file and one that prints the song lyrics with the appropriate pauses between each line:

```python
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
  ```
   
 **Step 4:**
 And finally we will create and call our threads:

```python
t1 = Thread(target=playingmusic)
t1.start()

t2 = Thread (target=do_thethingy) 
t2.start()
```

### And we're done! You can go ahead and test it out!
Of course you can use this script and edit it to play and **do literally whatever you want.** 



