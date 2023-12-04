import configuration
import requests
import data


def post_new_order():  # Функция создания заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.user_body,
                         headers=data.headers)


def get_track():  # Функция получения трекера заказа
    return post_new_order().json()["track"]


t = get_track()   # Сохранили трекер в t


def get_track_order():  # Функция создание набора
    return requests.get(configuration.URL_SERVICE + configuration.PRODUCTS_ORDER_TRACK_PATH + "?t=" + str(t))
