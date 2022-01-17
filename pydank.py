from time import sleep as wait
from requests import post as send

variables = {
    'header': {'authorization': input('Enter Your Token: ')},
    'url':  'https://discord.com/api/v9/channels/904975381977763904/messages?limit=50',
    'list_of_commands': [
        'daily',
        'beg',
        'use newplayer',
        'hunt',
        'fish',
        'dig',
        'use memebox',
        'use daily 2',
        'sell lifesaver max',
        'sell fishingpole max',
        'sell laptop max',
        'sell cellphone max',
        'sell huntingrifle max',
        'sell shovel max',
        'sell kno max',
        'sell'
        'se max',
        'gamble max',
        
    ]
}

def run(command, timex=0):
    payload = { 'content': f'{command}' }
    print(send(variables['url'],data=payload, headers=variables['header']))
    wait(timex)

def vote():
    run('pls vote')

def grind():
    for i in variables['list_of_commands']:
        run(f'pls {i}', 3)

def give():
    run('pls give max 919827389096292372')
