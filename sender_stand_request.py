# Татьяна Ведякина, 8-а когорта - Финальный проект. Инженер по тестированию плюс

import configuration as conf
import data as dt
import requests


# Создание нового заказа
def create_new_order():
    return requests.post(conf.URL_SERVICE + conf.CREATE_ORDER_PATH)


#  Получение номера трека
def save_track_number():
    new_order = create_new_order()
    return new_order.json()['track']


# Запрос информации о заказе по треку
def get_info():
    track = save_track_number()
    params_track = {"t": track}
    return requests.get(conf.URL_SERVICE + conf.GET_ORDER_PATH, params=params_track)
