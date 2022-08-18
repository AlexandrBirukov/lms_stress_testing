from locust import task

import settings
from .helpers import get_request, AuthTaskSet

"""
Дублирование запросов клиента:

/api/v1/user/user/ - x3
/api/v1/time/ - x2
/api/v1/client/courses/test_passing/ - x2
/api/v1/client/courses/material_passing/ - x2
/api/v1/client/courses/material/ - x2
"""


class ClientTaskSet(AuthTaskSet):
    USERNAME, PASSWORD = settings.CLIENT
    COURSE_ID = ''

    def on_start(self):
        super().on_start()

        # Получение курса клиента
        with self.client.get(settings.GET_CLIENT_COURSE, headers=self._get_header(), catch_response=True) as response:
            if response.status_code != 200:
                response.failure('Курсы клиента не получены.')
            else:
                for course in response.json():
                    if course['is_active']:
                        self.COURSE_ID = course['id']
                        break

    # @task(1)
    # def get_material_page(self):
    #     # Получение страницы материалов курса
    #     get_request(
    #         self, f'{settings.SITE}/courses/{self.COURSE_ID}/materials',
    #         self._get_header(),
    #         'Страница материалов курса не получена.'
    #     )

    @task(1)
    def api_tasks(self):
        # Получение заданий материалов курсов
        get_request(
            self, settings.GET_CLIENT_TASK,
            self._get_header(),
            'Список заданий материалов курсов не получен.'
        )

    @task(1)
    def api_bookmarks(self):
        # Получение закладок для материалов
        get_request(
            self, settings.GET_CLIENT_BOOKMARK,
            self._get_header(),
            'Список закладок для материалов не получен.'
        )

    @task(1)
    def api_materials(self):
        # Получение материалов курсов
        get_request(
            self, settings.GET_CLIENT_MATERIAL,
            self._get_header(),
            'Список материалов курсов не получен.',
            data={'course': self.COURSE_ID}
        )

    @task(1)
    def api_material_passing(self):
        # Получение прохождений материалов
        get_request(
            self, settings.GET_CLIENT_MATERIAL_PASSING,
            self._get_header(),
            'Список прохождений материалов не получен.'
        )

    @task(1)
    def api_test_passing(self):
        # Получение прохождений тестов
        get_request(
            self, settings.GET_CLIENT_TEST_PASSING,
            self._get_header(),
            'Список прохождений тестов не получен.'
        )

    @task(1)
    def api_activity(self):
        # Получение активности по дням клиента
        get_request(
            self, settings.GET_CLIENT_ACTIVITY,
            self._get_header(),
            'Список активности по дням не получен.',
            data={'course_id': self.COURSE_ID, 'user': self.USER_ID}
        )

    @task(1)
    def api_time(self):
        # Получение времени
        get_request(
            self, settings.GET_TIME,
            self._get_header(),
            'Время сервера не получено.'
        )
