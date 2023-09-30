# Татьяна Ведякина, 8-а когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request as sender


# Проверка ответа 200
def test_check_response():
    info_response = sender.get_info()
    assert info_response.status_code == 200
