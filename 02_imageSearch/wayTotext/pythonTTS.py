#from textToSpeech import *
from tkinter import *

from gtts import gTTS
import playsound
from tkinter import filedialog 

import speech_recognition as sr

global count
count = 1

# GUI, 타이틀, 화면 크기, 창 크기 고정
tk = Tk()
tk.title("Python TTS")
tk.geometry("420x240")
tk.resizable(width=False, height=False)

#텍스트 -> 보이스 함수
#save를 연속해서 같은 이름으로 하면 오류 나서 한번 실행 중일 때는 번호를 붙임.
def speak(text ,lang="ko", speed=False):
    global count
    tts = gTTS(text=text, lang=lang , slow=speed)
    saveMp3="./tts"+str(count)+".mp3"
    #saveWav="./tts"+str(count)+".wav"
    
    tts.save(saveMp3) #tts.mp3로 저장
    #tts.save(saveWav) #tts.mp3로 저장
    playsound.playsound(saveMp3) #말하기
    count = count+1

#보이스 -> 텍스트 (wav파일 경로, 언어 선택한 라디오버튼 값)
def voice2text(soundfile, translate):
    filename = soundfile
    
    # initialize the recognizer
    r = sr.Recognizer()

    #load voice by Korean
#   import librosa
#   sample_wav, rate = librosa.core.load(filename)
    korean_audio = sr.AudioFile(filename)
    
    if(translate == 0):
        Lang = 'en-US'
    elif(translate == 1):
        Lang = 'ko-KR'
    else:
        #경고창
        tk.showerror('언어 선택', '언어를 선택하지 않으셨습니다.')
        return  
    
    # open the file
    with korean_audio as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        try:
            #한국어로
            audio_text = r.recognize_google(audio_data,language=Lang)
            #audio_text = r.recognize_google(audio_data)
            print("음성 인식 결과 : %s" % audio_text)
            
        except:
            audio_text = "인식에 실패했습니다."
            print(audio_text)
        
        return audio_text
    # Result : 안녕하세요 이것은 테스트 코스입니다
    
#voiceTotext("./tempVoice/tts1.wav")

#확인 버튼 : 텍스트 -> 보이스 함수 실행
def confirm():
    print(input_text.get())
    text_data = input_text.get()
    tts.configure(text=text_data)
    speak(text_data,"en")

#파일 탐색기 오픈 후 경로를 전역 변수에 저장.    
def TTS_dir():
    tk.filename = filedialog.askopenfilename(initialdir='./', title='음성 파일 선택', filetypes=(
    ('wav files', '*.wav'),('all file', '*.*')))
    label_tts2.config(text= tk.filename)
    global voice_text
    voice_text = tk.filename
    
#위에서 저장된 전역 변수로 보이스 -> 텍스트 변환
def TTS_start():
    
    tts_result.config(text="음성 인식 결과 : "+ voice2text(voice_text,radioValue.get()))


# 1 텍스트 to 보이스
label = Label(tk,text='텍스트를 음성으로 출력합니다.')
label.grid(row=1,column=0,pady=10,columnspan=3)

#버튼
button = Button(tk, text="확인", command=confirm)
button.grid(row=2,column=0,padx=10)

#입력창
input_text = Entry(tk, width=50)
input_text.grid(row=2,column=1, columnspan=3)

#입력창 내용 출력
tts = Label(tk,text='음성 변환 내용')
tts.grid(row=3,column=2)

# 2 보이스 to 텍스트
label_tts1 = Label(tk,text='wav 파일의 음성을 텍스트로 출력합니다.')
label_tts1.grid(row=5,column=0,padx=10,columnspan=3)

button_tts2 = Button(tk, text="파일", command=TTS_dir)
button_tts2.grid(row=6,column=0,pady=10)
label_tts2 = Label(tk,text='파일 경로')
label_tts2.grid(row=6,column=1,columnspan=3)

#언어 선택용 라디오 버튼
radioValue = IntVar() 

# variable 값을 공유하는 버튼끼리 그룹(group)이 됩니다.
radio_button1 = Radiobutton(tk,text='English', variable=radioValue, value=0)
radio_button2 = Radiobutton(tk,text='Korean', variable=radioValue, value=1)

#라디오 버튼 배치
radio_button1.grid(column=1, row=7)
radio_button2.grid(column=2, row=7)

#결과 출력
button_tts3 = Button(tk, text="변환", command=TTS_start)
button_tts3.grid(row=7,column=0)
tts_result = Label(tk,text='음성 내용')
tts_result.grid(row=8,column=0,columnspan=3)


tk.mainloop()