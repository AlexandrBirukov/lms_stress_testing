# SITE = 'http://lms-dev.pakhomov.im'  # Тестовый сервер - фронт
# SITE_API = 'http://api.lms-dev.pakhomov.im'  # Тестовый сервер - API

SITE_API = 'https://api.lk.promrg.ru'  # Тестовый сервер - API

# --- Frontend ---
# PAGE_LOGIN_URL = f'{SITE}/authentication/login'  # Вход\авторизация
# PAGE_ADMIN_COURSES = f'{SITE}/admin/courses'  # Страница курсов для админа
# PAGE_CURATOR_USERS = f'{SITE}/curator/users'  # Страница пользователей для куратора

# --- Endpoints ---

# common endpoints
POST_TOKEN = '/api/v1/token/'  # Получение JWT
GET_USER_DATA = '/api/v1/user/user/'  # Данные пользователя
GET_UNREAD_MESSAGES = '/api/v1/chats/unread_message/'  # Список непрочитанных сообщений
GET_TIME = '/api/v1/time/'  # Список непрочитанных сообщений

# admin endpoints
GET_ADMIN_COURSES = '/api/v1/courses/course/'  # Список курсов для админа
GET_ADMIN_TAGS = '/api/v1/courses/tag/'  # Список тегов для админа
GET_ADMIN_USERS = '/api/v1/users/user/'  # Список пользователей для админа
GET_ADMIN_COMPANIES = '/api/v1/users/company/'  # Список компаний для админа
GET_ADMIN_MATERIALS = '/api/v1/courses/material/'  # Список материалов для админа
GET_ADMIN_TASKS = '/api/v1/courses/task/'  # Список заданий для админа
GET_ADMIN_TEST_PASSINGS = '/api/v1/courses/test_passing/'  # Список прохождений заданий для админа

# curator endpoints
GET_CURATOR_USERS = '/api/v1/curator/users/'  # Список пользователей для куратора

# client endpoints
GET_CLIENT_COURSE = '/api/v1/client/courses/course/'  # Курсы клиента
GET_CLIENT_TASK = '/api/v1/client/courses/task/'  # Задания материалов курсов клиента
GET_CLIENT_BOOKMARK = '/api/v1/client/courses/bookmark/'  # Закладки клиена для материалов
GET_CLIENT_MATERIAL = '/api/v1/client/courses/material/'  # Материалы курсов клиента (?course=306)
GET_CLIENT_MATERIAL_PASSING = '/api/v1/client/courses/material_passing/'  # Прохождение материалов клиентом
GET_CLIENT_TEST_PASSING = '/api/v1/client/courses/test_passing/'  # Прохождение тестов клиентом
GET_CLIENT_ACTIVITY = '/api/v1/client/users/activity/'  # Активность по дням клиента (?user=615&course_id=306)

# --- Роли пользователей ---
ADMIN = ('admin_role', 'admin_pas')  # Администратор
CLIENT = ('client_role', 'client_pas')  # Клиент
CURATOR = ('curator_role', 'curator_pas')  # Куратор
