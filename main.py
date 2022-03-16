import schedule
import time
import os
import pandas as pd
import pyautogui as pyAu
from datetime import datetime
import pyperclip
import winsound

ScheduleFile = (r'')  # Your CSV File Path
# Your Zoom Path
ZoomLocation = ('')
DelayTime = 5  # Delay Between Step

DataFrame = pd.read_csv(ScheduleFile, sep=',')


def JobParting(Date):
    Jobs = DataFrame.loc[DataFrame['Day'] == Date]
    Jobs.reset_index(drop=True, inplace=True)
    Jobs.sort_values('Time')
    return Jobs


def AvailableJobs(Jobs):
    if len(Jobs) == 0:
        return False
    else:
        return True


def DoneNoti(Jobs, index, State):
    if State:
        print(Jobs.loc[index, 'Class']+' done')
        winsound.PlaySound(r'C:\Windows\Media\Windows Background.wav',
                           winsound.SND_FILENAME | winsound.SND_NOWAIT)


def job(Jobs, index):
    os.startfile(ZoomLocation)
    time.sleep(DelayTime)
    x, y = pyAu.locateCenterOnScreen(r'\JoinButton.png')
    pyAu.click(x, y)
    time.sleep(DelayTime)
    pyAu.write(str(Jobs.loc[index, 'RoomID']))
    pyAu.press('tab', presses=2)
    pyAu.hotkey('ctrl', 'a')
    pyperclip.copy(str(Jobs.loc[index, 'ParticipantName']))
    pyAu.hotkey("ctrl", "v")
    pyAu.press('enter')
    time.sleep(DelayTime)
    pyAu.write(str(Jobs.loc[index, 'RoomPassword']))
    pyAu.press('enter')
    DoneNoti(Jobs, index, True)


def JobCall(Jobs, index, day):
    if day == 'Monday':
        schedule.every().monday.at(
            str(Jobs.loc[index, 'Time'])).do(job, Jobs, index)
    elif day == 'Tuesday':
        schedule.every().tuesday.at(
            str(Jobs.loc[index, 'Time'])).do(job, Jobs, index)
    elif day == 'Wednesday':
        schedule.every().wednesday.at(
            str(Jobs.loc[index, 'Time'])).do(job, Jobs, index)
    elif day == 'Thurday':
        schedule.every().thursday.at(
            str(Jobs.loc[index, 'Time'])).do(job, Jobs, index)
    elif day == 'Friday':
        schedule.every().friday.at(
            str(Jobs.loc[index, 'Time'])).do(job, Jobs, index)
    elif day == 'Saturday':
        schedule.every().saturday.at(
            str(Jobs.loc[index, 'Time'])).do(job, Jobs, index)
    else:
        schedule.every().sunday.at(
            str(Jobs.loc[index, 'Time'])).do(job, Jobs, index)


num = 0
Today = datetime.now().strftime('%A')
TodayJobs = JobParting(Today)
if AvailableJobs(Jobs=TodayJobs):
    while num < len(TodayJobs):
        JobCall(Jobs=TodayJobs, index=num, day=Today)
        num += 1
else:
    print('Not thing to do today. Quiting Now...')
    quit()


while 1:
    schedule.run_pending()
    time.sleep(1)
