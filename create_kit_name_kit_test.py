# # Нарек Доникян, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_get_track_order():  # Тест проверяющий, что статус кода равен 200 при запросе на получение заказа по треку заказа.
    sender_stand_request.get_track_order().status_code = 200
