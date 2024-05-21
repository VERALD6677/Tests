import requests
import unittest

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://cloud-api.yandex.net/v1/disk'
        self.token = 'YOUR_YANDEX_DISK_API_TOKEN'
        self.folder_name = 'TestFolder'

    def test_create_folder_success(self):
        headers = {'Authorization': 'OAuth ' + self.token}
        params = {'path': '/' + self.folder_name}
        response = requests.put(self.base_url + '/resources', headers=headers, params=params)

        self.assertEqual(response.status_code, 201)  # Ожидаемый код ответа 201 (Created)
        # Проверяем, что папка появилась на Диске
        self.assertTrue(self.check_folder_exists())

    def test_create_folder_already_exists(self):
        # Создаем папку для проверки на повторное создание
        self.create_folder()

        headers = {'Authorization': 'OAuth ' + self.token}
        params = {'path': '/' + self.folder_name}
        response = requests.put(self.base_url + '/resources', headers=headers, params=params)

        self.assertEqual(response.status_code, 409)  # Ожидаемый код ответа 409 (Conflict)

    def test_create_folder_invalid_token(self):
        # Используем недействительный токен
        invalid_token = 'INVALID_TOKEN'
        headers = {'Authorization': 'OAuth ' + invalid_token}
        params = {'path': '/' + self.folder_name}
        response = requests.put(self.base_url + '/resources', headers=headers, params=params)

        self.assertEqual(response.status_code, 401)  # Ожидаемый код ответа 401 (Unauthorized)

    def check_folder_exists(self):
        # Проверяет, существует ли папка на Диске
        headers = {'Authorization': 'OAuth ' + self.token}
        params = {'path': '/' + self.folder_name}
        response = requests.get(self.base_url + '/resources', headers=headers, params=params)
        return response.status_code == 200

    def create_folder(self):
        # Создает папку для тестов
        headers = {'Authorization': 'OAuth ' + self.token}
        params = {'path': '/' + self.folder_name}
        response = requests.put(self.base_url + '/resources', headers=headers, params=params)

if __name__ == '__main__':
    unittest.main()
