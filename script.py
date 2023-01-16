import pyautogui
import requests
import schedule
import time

def job():
    url = "https://28fe-133-19-43-10.jp.ngrok.io/poll"
    response = requests.request("GET", url)
    cheer = response.json()['cheer']
    jeer = response.json()['jeer']
    print(f'{time.localtime().tm_year}/{time.localtime().tm_mon}/{time.localtime().tm_mday} {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}', ' - cheer - ', cheer, ' - jeer - ', jeer)
    
    if jeer > cheer:
         # S Key -> Monsters move faster x2
        pyautogui.moveTo(30, 30)
        pyautogui.click()
        pyautogui.press('S')
    else:
        # R Key -> Change all monsters to be eatable
        pyautogui.moveTo(30, 30)
        pyautogui.click()
        pyautogui.press('R')
   
schedule.every(30).seconds.do(job)

while 1:
    schedule.run_pending()
