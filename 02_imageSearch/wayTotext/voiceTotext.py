import speech_recognition as sr


def voice2text(soundfile):
    filename = soundfile

    # initialize the recognizer
    r = sr.Recognizer()

    #load voice by Korean
    import librosa
    sample_wav, rate = librosa.core.load(filename)
    korean_audio = sr.AudioFile(filename)

    # open the file
    with korean_audio as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        try:
            #한국어로
            #audio_text = r.recognize_google(audio_data,language='ko-KR')
            audio_text = r.recognize_google(audio_data)
            print("음성 인식 결과 : %s" % audio_text)
        except:
            print("인식에 실패했습니다.")
    # Result : 안녕하세요 이것은 테스트 코스입니다
    
voice2text("./tempVoice/tts1.wav")

