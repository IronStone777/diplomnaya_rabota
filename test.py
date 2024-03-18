import request


# Тест проверки создания заказа
def test_order_creation():
    creation_response = request.post_new_order()
    track_id = creation_response.json().get('track')
    if track_id is None:
        print("Ключ 'track' отсутствует в ответе")
        return
    response = request.get_orders_track(track_id)
    assert response.status_code == 200
    print(response.json())