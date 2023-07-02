import pywhatkit
import datetime
import time
import sys
import pyautogui
# Number "+918768073772"
def send_whatsapp_reminder():
    currentTime = datetime.datetime.now()
    deadline = datetime.datetime(currentTime.year, currentTime.month, currentTime.day, 3, 15, 0)  # Set the deadline time

    if currentTime >= deadline:
        print("Current Time = ",currentTime)
        print("deadline = ",deadline)
        return  # If the current time has passed the deadline, no need to send a reminder

    time_left = deadline - currentTime
    hours_left = time_left.seconds // 3600
    minutes_left = ((time_left.seconds // 60) % 60)+1
    # minutes_left += minutes_left
    reminder_set_at = "The reminder is set for 03:15 in the morning"
    if hours_left != 0:
        reminder_message = f"{reminder_set_at}\nAutomated Reminder: {hours_left} hours and {minutes_left} minutes left until the Call."
    elif minutes_left != 0:
        reminder_message = f"{reminder_set_at}\nAutomated Reminder: {minutes_left} minutes left until the Call."
    else:
        reminder_message = f"It's time for Call."

    # Replace the phone number and message with your own
    pywhatkit.sendwhatmsg_instantly(
        phone_no = "+918768073772",
        message = reminder_message
    )

while True:
    send_whatsapp_reminder()
    time.sleep(15)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(58)  # Wait for 58 seconds before sending the next reminder
    # sys.exit("Task completed. Closing the program.")  # Exit the program when the deadline has passed
