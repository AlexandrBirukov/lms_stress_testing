from locust import HttpUser, between

from app.admin_role import AdminTaskSet
from app.curator_role import CuratorTaskSet
from app.client_role import ClientTaskSet


class MyUser(HttpUser):
    wait_time = between(1, 3)

    tasks = [
        # AdminTaskSet,  # Сейчас запускаем только пользователей с ролью администратора
        # CuratorTaskSet,  # Сейчас запускаем только пользователей с ролью куратор
        ClientTaskSet,  # Сейчас запускаем только пользователей с ролью клиент
    ]
