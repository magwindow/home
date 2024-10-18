import os
import django
import json
from goods.models import Categories

# Установка переменной окружения, чтобы Django знал, где искать настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '../app.settings.py')

# Инициализация Django
django.setup()

# Получаем все категории
categories = Categories.objects.all()

# Собираем данные для экспорта
data = []
for category in categories:
    data.append({
        "model": "goods.categories",
        "pk": category.pk,
        "fields": {
            "name": category.name,
            "slug": category.slug
        }
    })

# Записываем данные в JSON файл с кодировкой utf-8
with open('fixtures/goods/cats.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)





