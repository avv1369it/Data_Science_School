import joblib
import numpy as np
import random
from flask import Flask, render_template_string, request

# Загружаем модель LightFM
model = joblib.load("/usr/src/app/static/model/model_LightFM_final.joblib")

# Список URL-адресов для изображений товаров
item_images = [
    "/static/images/image_1.jpg",
    "/static/images/image_2.jpg",
    "/static/images/image_3.jpg",
    "/static/images/image_4.jpg",
    "/static/images/image_5.jpg",
    "/static/images/image_6.jpg",
    "/static/images/image_7.jpg",
    "/static/images/image_8.jpg",
    "/static/images/image_9.jpg",
    "/static/images/image_10.jpg",
]

# Функция для получения рекомендаций
def get_recommendations(user_id):
    try:
        scores = model.predict(user_ids=user_id, item_ids=np.arange(model.item_embeddings.shape[0]))
        top_indices = np.argsort(-scores)[:3]  # Получить индексы элементов с наивысшими оценками
        return top_indices
    except ValueError as e:
        print(f"Ошибка: {e}")
        return []

app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_id = int(request.form.get('user_id'))
        
        # Получаем рекомендации для указанного пользователя
        recommendations = list(get_recommendations(user_id))
        
        if len(recommendations) > 0:
            random_images = random.sample(item_images, len(recommendations))
            return render_template_string('''
                <h2>Для пользователя с ID: {{ user_id }} рекомендованы следующие товары:</h2>
                <div style="display: flex;">
                    {% for index, item, image in recommendations %}
                        <div style="margin-right: 50px;">
                            <p>Товар ID: {{ item }}</p>
                            <img src="{{ image }}" width="500">
                        </div>
                    {% endfor %}
                </div>
            ''', user_id=user_id, recommendations=zip(range(1, 4), recommendations, random_images))
        else:
            return f"Пользователь с ID: {user_id} не найден или для него нет рекомендаций."
    
    # Если GET-запрос, рендерим форму ввода userID
    return render_template_string('''
        <form method="post">
            <label for="user_id">Введите UserID:</label><br>
            <input type="number" id="user_id" name="user_id"><br><br>
            <input type="submit" value="Получить рекомендации">
        </form>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)