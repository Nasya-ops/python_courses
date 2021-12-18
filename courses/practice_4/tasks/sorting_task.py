from collections import defaultdict

WAGER_TYPES = {
    'LOTTO_WAGER': 'Lucky Numbers',
    'WAGER': 'Sports',
    'LIVE_WAGER': 'Live Sports',
    'BETGAMES_WAGER': 'Betgames',
    'EVOLUTION_WAGER': 'Evolution Games',
    'EZUGI_WAGER': 'Ezugi Games',
    'PRAGMATIC_WAGER': 'Pragmatic Play Games'
}

PURCHASE_SETTINGS_ORDER = [
    'LOTTO_WAGER',
    'WAGER',
    'LIVE_WAGER',
    'BETGAMES_WAGER',
    'EVOLUTION_WAGER',
    'EZUGI_WAGER',
    'PRAGMATIC_WAGER'
]

purchase_settings = [
    {
        'wagerType': 'PRAGMATIC_WAGER',
        'minTotalOdds': '',
        'wageredPercent': '15',
        'sameEventAllowed': True
    },
    {
        'wagerType': 'BETGAMES_WAGER',
        'minTotalOdds': '2',
        'wageredPercent': '100',
        'sameEventAllowed': True
    },
    {
        'wagerType': 'LIVE_WAGER',
        'minTotalOdds': '3',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
    {
        'wagerType': 'LOTTO_WAGER',
        'minTotalOdds': '4',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
    {
        'wagerType': 'WAGER',
        'minTotalOdds': '',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
]


def dict_to_result(purch_settings):
    my_dict = defaultdict(list)

    for i in purch_settings:
        for k, v in i.items():
            my_dict[k].append(v)
    list_1 = list(my_dict.get('wagerType'))

    list_2 = []

    for i in reversed(list_1):
        for k in WAGER_TYPES:
            if i == k:
                list_2.append(WAGER_TYPES[k])
    list_2[0], list_2[1] = list_2[1], list_2[0]
    return list_2


print(dict_to_result(purchase_settings))
result = [
    'Lucky Numbers',
    'Sports',
    'Live Sports',
    'Betgames',
    'Pragmatic Play Games'
]
