import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def start(update, context):
    update.message.reply_text("Please enter your group:")
def my_code(update, context):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(executable_path=r'D:\Python Projects\blackout bot\chromedriver.exe', options=options)
    driver.get('https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule')

    timeSchedule = []
    elements = driver.find_elements(By.CLASS_NAME, "fc-event-container")
    for element in elements:
        timeSchedule.append(element.text)
    driver.quit()
    newSchedule = [string.replace("\n", " ") for string in timeSchedule]
    new_list = [item for sublist in [i.split() for i in newSchedule] for item in sublist]
    Group = update.message.text
    if (Group in new_list):
        occurrences_of_Group = [i for i, x in enumerate(new_list) if x == Group]

        for i in occurrences_of_Group:
            update.message.reply_text("from <b>"+new_list[i - 2] + "</b> to <b>"+ new_list[i - 1]+"</b>",parse_mode=telegram.ParseMode.HTML)

    else:
        update.message.reply_text("please enter a valid Group (Case Sensitive)")


    pass
updater = Updater("5841110404:AAGEi6liSGEzAmB4rPgIwv0QwrGUUaHgdLI", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, my_code))
updater.start_polling()
updater.idle()