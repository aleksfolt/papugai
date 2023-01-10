import os, webbrowser, sys, requests, subprocess, pyttsx3, datetime, wikipedia
from datetime import datetime
import keyboard
import pyautogui
from pynput.keyboard import Key,Controller
keyboard = Controller()
import time
wait = time.sleep
from time import sleep

#345678
engine = pyttsx3.init()
engine.setProperty('rate', 180)

wikipedia.set_lang('ru')

def speaker(text):
    '''2345678'''
    engine.say(text)
    engine.runAndWait()


def browser():
    webbrowser.open('https://www.youtube.com', new=2)


def game():
    try:
        subprocess.Popen('"C:\GOG Games\Road 96\Road 96.exe"')
    except:
        speaker('Путь к файлу не найден, проверьте, правильный ли он')


def explorer():
    try:
        subprocess.Popen('explorer.exe')
    except:
        speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    # Эта команда отключает ПК под управлением Windows

    os.system('shutdown \s')
    print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
    try:
        params = {'q': 'haifa', 'units': 'metric', 'lang': 'ru', 'appid': 'db9cfb630c4abb144cf1f537a9e67bc2'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    sys.exit()


def funny_cats():
    webbrowser.open('https://www.google.com/search?q=funny+cat&sxsrf=AJOqlzWAezTryyh2_xKaU-iuCG6oaszy6Q:1673096225520&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjMxMmRwbX8AhUxS_EDHZ0qDDkQ_AUoAXoECAIQAw&biw=1536&bih=746&dpr=1.25', new=2)


def funny_dog():
    webbrowser.open('https://www.google.com/search?q=funny+dog&sxsrf=AJOqlzX3kxmS02pmmqUgrqdnV02523LVyQ:1673096384727&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjx477dwbX8AhWDQvEDHWDiBrMQ_AUoAXoECAEQAw&biw=1536&bih=746&dpr=1.25', new=2)


def music():
    webbrowser.open('https://mp3uk.net/pesen-2020/14227-fem-love-1000-7-skachat.html')


def telegram():
    try:
        subprocess.Popen(r'C:\Users\AleksFOLT\AppData\Roaming\Telegram Desktop\Telegram.exe')
    except:
        speaker('Путь к файлу не найден, проверьте, правильный ли он')


def news():
    webbrowser.open('https://nikk.agency/?gclid=Cj0KCQiAzeSdBhC4ARIsACj36uHK9QFbMN7rs68fKXwuBQ78LsNPxK04nyAFa3yvVKBcL0u3Ee_CVx8aAnDjEALw_wcB')


def calculator():
    subprocess.Popen()


def volumeup():
    for i in range(10):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
    sleep(2)


def volumedown():
    for i in range(10):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
    sleep(2)


def alt_f4():
    pyautogui.hotkey('alt', 'f4')


def svernut():
    pyautogui.hotkey('win', 'm')


def time():
    current_datetime = datetime.now()
    speaker(current_datetime.hour)
    speaker(current_datetime.minute)
    sleep(0.5)


def wikipedia():
    python_page = wikipedia.page(engine.say)

def chrome_kill():
    import os
    os.system("taskkill /f /im chrome.exe")


def passive():
    pass