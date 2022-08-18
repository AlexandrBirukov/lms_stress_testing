from locust import task

import settings
from .helpers import get_request, AuthTaskSet

"""
Дублирование запросов куратора:

/api/v1/user/user/ - x2
/api/v1/curator/users/ - x2

"""


class CuratorTaskSet(AuthTaskSet):
    USERNAME, PASSWORD = settings.CURATOR

    # @task(1)
    # def get_users_page(self):
    #     # Получение страницы курируемых пользователей
    #     get_request(
    #         self, settings.PAGE_CURATOR_USERS,
    #         self._get_header(),
    #         'Страница пользователей не получена.'
    #     )

    @task(1)
    def api_users(self):
        # Получение списка пользователей
        get_request(
            self, settings.GET_CURATOR_USERS,
            self._get_header(),
            'Список пользователей не получен.'
        )
