#!/usr/bin/env python3
import states

from helpers import show_room
from items import figa, coin, canister, matches, fire_extinguisher, newspaper, door
from commands import *


if __name__ == '__main__':
    # init game
    context = {
        'state': states.PLAY,
        'backpack': {
            'items': [],
            'max': 2,
        },
        'world': {},
        'room': {},
        'commands': [
            cmd_about,
            cmd_inventory,
            cmd_drop,
            cmd_take,
            cmd_examine,
            cmd_quit,
            cmd_look_around,
            cmd_use,
            cmd_commands
        ]
    }

    context['backpack']['items'].append(figa)
    context['backpack']['items'].append(coin)

    context['room'] = {
        'name': 'dungeon',
        'description': 'Nachádzaš sa v tmavej zatuchnutej miestnosti. Na kamenných stenách sa nenachádza žiadne okno, '
                       'čo dáva tušiť, že si niekoľko metrov pod zemou. Žeby košický hrad? Aj to je možné, ti '
                       'prebleslo hlavou.',
        'items': [
            canister,
            matches,
            fire_extinguisher,
            newspaper,
            door
        ],
        'exits': []
    }

    # banner
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print("                       and his Great Escape                        ")
    print()

    # rendering the dark room
    show_room(context['room'])

    # main loop
    while context['state'] == states.PLAY:
        # normalizing string
        line = input('> ').lower().strip()

        # empty input
        if line == '':
            continue

        command, param = parse(line, context)
        if command is None:
            print('Taký príkaz nepoznám.')
        else:
            callback = command['exec']
            callback(context, param)

        # check game win

    # game credits
    print('(c)2021 by Dárius Lindvai')
