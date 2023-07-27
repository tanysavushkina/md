# импорты
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import comunity_token, acces_token
from core import VkTools

class VKSearch:
    relations = {
        1: 'не женат/не замужем',
        2: 'есть друг/есть подруга',
        3: 'помолвлен/помолвлена',
        4: 'женат/замужем',
        5: 'в активном поиске',
        6: 'влюблён/влюблена'
    }
    regex = {
        'минимальный  возраст': 'lower_age_limit',
        'максимальный возраст': 'higher_age_limit',
        'город': 'city',
        'семейное положение': 'marital_status'
    }

    def get_search_data(self, user_id: int):
           result = db_api.get_params(user_id)
        if result:
            self.write_msg(user_id, 'Поиск...')
            self.search_for_users(user_id)
            return result
        else:
            text = 'Проверьте введенные параметры'
            self.write_msg(user_id, text)

    """Данный метод провеит  заполнение всех полей поискового
            запроса."""
    def check(self, data_to_check: list) -> bool:

        check_data = True
        for key in self.regex.keys():
            choice = False
            for data in data_to_check:
                choice = bool(re.search(key, data))
            check_data = choice
        return check_data


class BotInterface():

    def __init__(self,comunity_token, acces_token):
        self.vk = vk_api.VkApi(token=comunity_token)
        self.longpoll = VkLongPoll(self.vk)
        self.vk_tools = vkTools(acces_token)
        # self.interface = vk_api.VkApi(token=comunity_token)
        # self.api = VkTools(acces_token)
        self.params = {}
        self.worksheets = []
        self.offset = 0

    def message_send(self, user_id, message, attachment=None):
        self.interface.method('messages.send',
                                {'user_id': user_id,
                                'message': message,
                                'attachment': attachment,
                                'random_id': get_random_id()
                                }
                                )

    def event_handler(self):
        # longpoll = VkLongPoll(self.interface)
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text.lower() == 'привет':
                    '''Логика для получения данных о пользователях'''
                    self.params = self.vk_tools.get_profile_info(event.user_id)
                    self.message_send(event.user_id, f'Приветствую! {self.params['name]}')
                elif event.text.lower() == 'поиск':
        for user in users:
        user_info = get_user_info(user['id'])
            if user_info:
                message = f"{user_info.get('first_name', '')} {user_info.get('last_name', '')}\n"
                message += f"Дата рождения: {user_info.get('bdate', '')}\n"
                message += f"Город: {user_info.get('city', {}).get('title', '')}\n"
                    for photo_link in photos:
                        message += f"Фото: [{photo_link}]({photo_link})\n"
                        message += f"Ссылка на профиль: https://vk.com/id{user['id']}"
                        save_search_results(create_connection(), user_id, user['id'],
                        user_info.get('first_name', ''), user_info.get('last_name', ''),
                        user_info.get('bdate', ''), user_info.get('city', {}).get('title', ''))
            else:
                    write_msg(user_id, "Для использования данной команды вам необходимо заполнить профиль")
            else:
                    write_msg(user_id, "Я вас не понимаю. Введите корректную команду")

                    '''Логика для поиска анкет'''
                    self.message_send(event.user_id, 'Начнем!')
                    if self.worksheets:
                        worksheet = self.worksheets.pop()
                        photos = get.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:
                            photo_string += f'photo{photo["owner_id"]}-photo["id"],'
                            ''' photo{owner_id}_{id} '''
                    else:
                        self.worksheets = self.vk_tools.search_worksheet (self.params, self.offset)
                        worksheet = self.worksheets.pop()
                        photos = get.vk_tools.get_photos(worksheet['id'])
                        photo_string = ''
                        for photo in photos:
                            photo_string += f'photo{photo["owner_id"]}-photo["id"],'
                        self.offset +=10
                    self.photo(user_id, 'Фото с максимальными лайками')
                    self.message_send(event.user_id, f'имя: {worksheet["name"]} ссылка: vk.com/{worksheet["id"]}',
                    attachment=photo_string
                    )
                elif event.text.lower() == 'покa':
                    self.message_send(event.user_id, 'До скорой встречи!
                else:
                self.message_send(event.user_id, 'Команда не опознана!')
                # command = event.text.lower()

                # if command == 'привет':
                #     self.params = self.api.get_profile_info(event.user_id)
                #     self.message_send(event.user_id, f'здравствуй {self.params["name"]}')
                # elif command == 'поиск':
                #     users = self.api.serch_users(self.params)
                #     user = users.pop()
                    #здесь логика дял проверки бд
                    photos_user = self.api.get_photos(user['id'])                  
                    
                    attachment = ''
                    for num, photo in enumerate(photos_user):
                        attachment += f'photo{photo["owner_id"]}_{photo["id"]}'
                        if num == 2:
                            break
                    self.message_send(event.user_id,
                                      f'Встречайте {user["name"]}',
                                      attachment=attachment
                                      ) 
                    #здесь логика для добавленяи в бд
                elif command == 'пока':
                    self.message_send(event.user_id, 'пока')
                else:
                    self.message_send(event.user_id, 'команда не опознана')



if __name__ == '__main__':
    bot_interface = BotInterface(comunity_token, acces_token)
    bot_interface.event_handler()

            

