from locust import task

import settings
from .helpers import get_request, AuthTaskSet

"""
Дублирование запросов админа:

/api/v1/user/user/ - x3
/api/v1/courses/course/ - x3
/api/v1/user/user/ - x2
/api/v1/users/company/ - x2

"""


class AdminTaskSet(AuthTaskSet):
    USERNAME, PASSWORD = settings.ADMIN

    # @task(1)
    # def get_courses_page(self):
    #     # Получение страницы курсов
    #     get_request(
    #         self, settings.PAGE_ADMIN_COURSES,
    #         self._get_header(),
    #         'Страница курсов не получена.'
    #     )

    @task(1)
    def api_courses(self):
        # Получение списка курсов
        get_request(
            self, settings.GET_ADMIN_COURSES,
            self._get_header(),
            'Список курсов не получен.'
        )

    @task(1)
    def api_tags(self):
        # Получение списка тегов
        get_request(
            self, settings.GET_ADMIN_TAGS,
            self._get_header(),
            'Список тегов не получен.'
        )

    @task(1)
    def api_users(self):
        # Получение списка пользователей
        get_request(
            self, settings.GET_ADMIN_USERS,
            self._get_header(),
            'Список пользователей не получен.'
        )

    @task(1)
    def api_companies(self):
        # Получение списка компаний
        get_request(
            self, settings.GET_ADMIN_COMPANIES,
            self._get_header(),
            'Список компаний не получен.'
        )

    @task(1)
    def api_materials(self):
        # Получение списка матриалов
        get_request(
            self, settings.GET_ADMIN_MATERIALS,
            self._get_header(),
            'Список материалов не получен.'
        )

    @task(1)
    def api_tasks(self):
        # Получение списка заданий
        get_request(
            self, settings.GET_ADMIN_TASKS,
            self._get_header(),
            'Список заданий не получен.'
        )

    @task(1)
    def api_test_passings(self):
        # Получение списка прохождений заданий
        get_request(
            self, settings.GET_ADMIN_TEST_PASSINGS,
            self._get_header(),
            'Список прохождений заданий не получен.'
        )

    @task(3)
    def api_unread_messages(self):
        # Получение списка непрочитанных сообщений
        get_request(
            self, settings.GET_UNREAD_MESSAGES,
            self._get_header(),
            'Список непрочитанных сообщений не получен.'
        )
