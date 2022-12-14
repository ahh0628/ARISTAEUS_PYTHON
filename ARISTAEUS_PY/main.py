import time
import os
from discord_webhook import DiscordWebhook #hello imports my old friend

def spammer():
    hookurl = input('URL:')
    message = input('Message:')
    webhook = DiscordWebhook(url=hookurl, content=message)
    result = input('Start spam? y/n')
    match result:
        case 'y':
            while True:
                response = webhook.execute()
                time.sleep(0.5)
        case 'n':
            os.system('cls')
            start()


def sender():
    hookurl = input('URL:')
    message = input('Message:')
    webhook = DiscordWebhook(url=hookurl, content=message)
    result = input('Start sender? y/n')
    match result:
        case 'y':
            response = webhook.execute()
            print('Sent!')
            time.sleep(2)
            start()
        case 'n':
            start()

def nukerPreset():
    hookurl = input('URL:')
    message = input('Message:')
    webhook = DiscordWebhook(url=hookurl, content=message)
    result= input('Start preset? y/n')
    match result:
        case 'y':
            for i in range(25):
                response = webhook.execute()
                #time.sleep(0.3) turns out the library does auto
                #anti rate limiting so i dont need the sleep
                #absolutely poggers
                #actually nvm it just skips this after it rate limits and just deletes the webhook but fuck you stop reading my comments u nigor
            os.system('curl -X DELETE ' + hookurl)
            print('Webhook Deleted, preset finished!')
            time.sleep(2)
            os.system('cls')
            start()
        case 'n':
            os.system('cls')
            start()


def multiHookSpammer():
    url1 = input('URL 1: ')
    msg1 = input('Message 1: ')
    print('URL 1 set to ' + url1 + '\n Message Set to ' + msg1)
    url2 = input('URL 2: ')
    msg2 = input('Message 2: ')
    print('URL 2 set to ' + url2 + '\n Message Set to ' + msg2)
    url3 = input('URL 3: ')
    msg3 = input('Message 3: ')
    print('URL 3 set to ' + url3 + '\n Message Set to ' + msg3)
    url4 = input('URL 4: ')
    msg4 = input('Message 4: ')
    print('URL 4 set to ' + url4 + '\n Message Set to ' + msg4)
    url5 = input('URL 5: ')
    msg5 = input('Message 5: ')
    print('URL 5 set to ' + url5 + '\n Message Set to ' + msg5)
    webhookurls = [url1, url2, url3, url4, url5]
    webhook1 = DiscordWebhook(url=url1, content=msg1)
    webhook2 = DiscordWebhook(url=url2, content=msg2)
    webhook3 = DiscordWebhook(url=url3, content=msg3)
    webhook4 = DiscordWebhook(url=url4, content=msg4)
    webhook5 = DiscordWebhook(url=url5, content=msg5)
    yorn = input('Start hooks? y/n')
    match yorn:
        case 'y':
            while True:           
                    response1 = webhook1.execute()
                    response2 = webhook2.execute()     
                    response3 = webhook3.execute()
                    response4 = webhook4.execute()
                    response5 = webhook5.execute()
        case 'n':
            time.sleep(1)
            os.system('cls')
            start()


def deleter():
    toDelete = input('URL: ')
    os.system('curl -X DELETE ' + toDelete)
    print('Deleted!')
    time.sleep(2)
    start()


def scheduler():
    schedule = input('URL: ')
    message = input('Message: ')
    time = input(int('Delay per send: '))
    webhook = DiscordWebhook(url=schedule, content=message)
    result = input('Start scheduler? y/n ')
    match result:
        case 'y':
            while True:
                response = webhook.execute()
                time.sleep(time)
        case _:
            time.sleep(1)
            start()

# main function thingy
def start():
    os.system('cls')
    os.system('color 6')
    print('$$$$$$\  $$$$$$$\  $$$$$$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$$\ $$\   $$\  $$$$$$\ ')
    print('$$  __$$\ $$  __$$\ \_$$  _|$$  __$$\\__$$  __|$$  __$$\ $$  _____|$$ |  $$ |$$  __$$\ ')
    print('$$ /  $$ |$$ |  $$ |  $$ |  $$ /  \__|  $$ |   $$ /  $$ |$$ |      $$ |  $$ |$$ /  \__|')
    print('$$$$$$$$ |$$$$$$$  |  $$ |  \$$$$$$\    $$ |   $$$$$$$$ |$$$$$\    $$ |  $$ |\$$$$$$\ ')
    print('$$  __$$ |$$  __$$<   $$ |   \____$$\   $$ |   $$  __$$ |$$  __|   $$ |  $$ | \____$$\ ')
    print('$$ |  $$ |$$ |  $$ |  $$ |  $$\   $$ |  $$ |   $$ |  $$ |$$ |      $$ |  $$ |$$\   $$ |')
    print('$$ |  $$ |$$ |  $$ |$$$$$$\ \$$$$$$  |  $$ |   $$ |  $$ |$$$$$$$$\ \$$$$$$  |\$$$$$$  |')
    print('\__|  \__|\__|  \__|\______| \______/   \__|   \__|  \__|\________| \______/  \______/           but in python  \n\n made by ahh#0628 \n\n')

    
    print('         1. Webhook Spammer')
    print('         2. Webhook Sender (in case you dont want to spam it')
    print('         3. Webhook Nuker Preset')
    print('         4. Multiple Webhook Spammer')
    print('         5. Webhook Deleter')
    print('         6. Webhook Scheduler')

    result = input()
    match result:
        case '1':
            spammer()
        case '2':
            sender()
        case '3':
            nukerPreset()
        case '4':
            multiHookSpammer()
        case '5':
            deleter()
        case '6':
            scheduler()
        case _:
            print("You're funny.")
            time.sleep(1)
            start()

start() #runs start
