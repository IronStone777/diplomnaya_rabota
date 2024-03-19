import request

# Кондратьев Артем, 14-я когорта - Финальный проект. Инженер по тестированию плюс
# Тест проверки создания заказа
def test_order_creation():
    creation_response = request.post_new_order()
    track_id = creation_response.json().get('track')
    response = request.get_orders_track(track_id)
    assert response.status_code == 200, f"Expected status_code {200}, but got {response.status_code}"
    print("Тест пройден")
