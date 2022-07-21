from httpx import stream
from vosk import Model, KaldiRecognizer
import pyaudio
import sys, time

#need to pass absolute path
model=Model(r"C:\\Users\\Rgarud\\Desktop\\cloudstrats\\Speech_to_Speech_ofline\\vosk-model-small-en-us-0.15\\vosk-model-small-en-us-0.15")
recognizer=KaldiRecognizer(model,16000)

mic=pyaudio.PyAudio()
stream= mic.open(format=pyaudio.paInt16, channels=1,rate=16000,input=True,frames_per_buffer=8192)
stream.start_stream()

print("listning")
while True:
    data=stream.read(4096)
    # if len(data)==0:
    #     data=stream.read(4096)
    if recognizer.AcceptWaveform(data):
        
        text=recognizer.Result()
        
        if text[14:-3]=="Exit" or text[14:-3]=="exit":
            print("Dictation Stoped")
            break
        if text[14:-3]=="new line" or text[14:-3]=="New line":
            print(sep="\n")
            continue
        # if text[14:-3]=="":
        #     sys.stdout.flush()
        #     time.sleep(4)
            # print(text[14:-3])
        print(text[14:-3],end=" ")
