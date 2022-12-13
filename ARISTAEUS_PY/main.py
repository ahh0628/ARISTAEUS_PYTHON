import time
import os
from discord_webhook import DiscordWebhook

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
    url1 = input('URL 1: ') #wip kk



# main function thingy
def start():
    print(' $$$$$$\  $$$$$$$\  $$$$$$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$$\ $$\   $$\  $$$$$$\ ')
    print('$$  __$$\ $$  __$$\ \_$$  _|$$  __$$\\__$$  __|$$  __$$\ $$  _____|$$ |  $$ |$$  __$$\ ')
    print('$$ /  $$ |$$ |  $$ |  $$ |  $$ /  \__|  $$ |   $$ /  $$ |$$ |      $$ |  $$ |$$ /  \__|')
    print('$$$$$$$$ |$$$$$$$  |  $$ |  \$$$$$$\    $$ |   $$$$$$$$ |$$$$$\    $$ |  $$ |\$$$$$$\ ')
    print('$$  __$$ |$$  __$$<   $$ |   \____$$\   $$ |   $$  __$$ |$$  __|   $$ |  $$ | \____$$\ ')
    print('$$ |  $$ |$$ |  $$ |  $$ |  $$\   $$ |  $$ |   $$ |  $$ |$$ |      $$ |  $$ |$$\   $$ |')
    print('$$ |  $$ |$$ |  $$ |$$$$$$\ \$$$$$$  |  $$ |   $$ |  $$ |$$$$$$$$\ \$$$$$$  |\$$$$$$  |')
    print('\__|  \__|\__|  \__|\______| \______/   \__|   \__|  \__|\________| \______/  \______/ ')

    # end of text art

    print('         1. Webhook Spammer')
    print('         2. Webhook Sender (in case you dont want to spam it')
    print('         3. Nuker preset (if ur lazy)')
    print('         4. Multiple hook spammer')

    result = input()
    match result:
        case '1':
            spammer()
        case '2':
            sender()
        case '3':
            nukerPreset()

start() #runs start
