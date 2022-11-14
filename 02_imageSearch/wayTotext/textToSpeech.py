from gtts import gTTS
import playsound


global count
count = 1

def speak(text ,lang="ko", speed=False):
    global count
    tts = gTTS(text=text, lang=lang , slow=speed)
    saveMp3="./tempVoice/tts"+str(count)+".mp3"
    saveWav="./tempVoice/tts"+str(count)+".wav"

    
    tts.save(saveMp3) #tts.mp3로 저장
    tts.save(saveWav) #tts.mp3로 저장
    playsound.playsound(saveMp3) #말하기
    count = count+1
    #return saveMp3

#speak("Fang Joker","en")