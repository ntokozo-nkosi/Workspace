from pynotifier import Notification
import simpleaudio as sa
import multiprocessing
import time

def notify():
    Notification(
    	title='Pomodoro Timer',
    	description='countdown over!! Take a break',
    	icon_path='/home/darthvader/Workspace/pomodoro_timer/tomato.png', # On Windows .ico is required, on Linux - .png
    	duration=20,                                   # Duration in seconds
    	urgency='normal'
    ).send()

def play_sound():
    wave_obj = sa.WaveObject.from_wave_file("/home/darthvader/Workspace/pomodoro_timer/beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def notification_processes():
    process1 = multiprocessing.Process(target=notify)
    process2 = multiprocessing.Process(target=play_sound)
    process1.start()
    process2.start()

def countdown(t):
    while t != 0:
        time.sleep(1)
        t -= 1
    return notification_processes()

t = int(input("How many minutes --> "))
countdown(t)
