from locust import TaskSet

import settings


def get_request(l, url, headers, message, data=None):
    """
    GET запрос с проверкой статуса ответа

    :param l: объект пользователя
    :param url: адрес запроса
    :param headers: заголовки запроса
    :param message: сообщение об ошибке
    :param data: данные запроса
    """
    with l.client.get(url, headers=headers, data=data, catch_response=True) as response:
        if response.status_code != 200:
            response.failure(message)


class AuthTaskSet(TaskSet):
    """
    Класс авторизации - общий для всех ролей пользователей
    """

    # USERNAME, PASSWORD = settings.ADMIN
    USERNAME = ''
    PASSWORD = ''
    ACCESS = ''
    REFRESH = ''
    USER_ID = ''

    def _get_header(self):
        return {'Authorization': f'Bearer {self.ACCESS}'}

    def on_start(self):
        # GET страница авторизации
        # with self.client.get(settings.PAGE_LOGIN_URL, catch_response=True) as response:
        #     if response.status_code != 200:
        #         response.failure('Страница авторизации не получена.')

        # POST получение JWT
        with self.client.post(
                settings.POST_TOKEN,
                {'username': self.USERNAME, 'password': self.PASSWORD},
                catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure('Токен авторизации не получен.')
            else:
                res = response.json()
                self.ACCESS = res['access']
                self.REFRESH = res['refresh']

        # Получение данных пользователя
        with self.client.get(settings.GET_USER_DATA, headers=self._get_header(), catch_response=True) as response:
            if response.status_code != 200:
                response.failure('Данные пользователя не получены.')
            else:
                data = response.json()
                self.USER_ID = data['id']
