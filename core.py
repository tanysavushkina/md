from pprint import pprint
from datetime import datetime

import vk_api
from vk_api.exceptions import ApiError
from config import acces_token



class VkTools:
    def __init__(self, acces_token):
       self.vkapi = vk_api.VkApi(token=acces_token)

    def _bdate_toyear(self, bdate):
        user_year
        bdate.split('.')[2]

    def get_profile_info(self, user_id):


            def serch_users(self, params):
        try:
            info, = self.vkapi.method('users.get',
                            {'user_id': user_id,
                            'fields': 'city,bdate,sex,relation'
                            }
                            )
        except ApiError as e:
            info = {}
            print(f'error = {e}')


        result = {'name': (info['first_name'] + ' ' + info['last_name']) if
                    'first_name' in info and 'last_name' in info else None,
                    'sex': infco.get | ('sex'),
                    'city': info.get('city')['id'] if info.get ('city') is not None# 'id':  info['id'],
                    'city': info.get('city')['id'] if info.get('city') is not None
                    'year': self._bdate_toyear(info.get('bdate')),
                    # 'home_town': info['home_town'],
                    # 'bdate': info['bdate'] if 'bdate' in info else None,
                    }
        return result
        def search_worksheet(self, params, offset):
            try:
                users = self.vkapi.method('users.search',
                                        {'count': 10,
                                         'offset': offset,
                                         'hometown': params['city'],
                                         'sex': 1 if params[sex] == 2 else 2,
                                         'has_photo': True,
                                         'age_from': params['year'] - 3,
                                         'age_to': params['year'] + 3,
                                         }
                                        )
    except ApiError as e:
        users = []
    print(f'error = {e}')

    result = [{
        'name': item['first_name']  + item ['last_name'],
        'id': item['id']
        } for item in users['items'] if item['is_closed'] is False
        ]
    return users


def get_photos(self, id):
    try:
        photos = self.vkapi.method('photos.get',
                                {'owner_id': id,
                                 'album_id': 'profile',
                                 'extended': 1                                 }
                                )

    except ApiError as e:
        photos = {}
        print(f'error = {e}')

    result = [{'owner_id': item['owner_id'],
               'id': item['id'],
               'likes': item['likes']['count'],
               'comments': item['comments','count']
    } for item in photos['items']
    ]
'''Сортировка по лайкам и коментам'''
    return result[:3]

if __name__ == '__main__':
    # bot = VkTools(acces_token)
    # params = bot.get_profile_info(801289758)
    # users = bot.serch_users(params)
    # print(bot.get_photos(users[2]['id']))
    user_id = 801289758
    tools = VkTools(acces_token)
    params = tools.get_profile_info(user_id)
    worksheets = tools.search_worksheet(params)
    worksheet - worksheets.pop()
    photos = tools.get_photos(worksheet['id'])

    pprint(worksheet)
























