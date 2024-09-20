## Задание

Разработайте простой API для управления списком задач. Используйте Django и Django REST Framework.

## Требования

1. Создайте Django проект и приложение tasks.
2. Реализуйте модель Task с полями:
   - title (строка, до 100 символов)
   - description (текст, необязательное поле)
   - completed (булево значение, по умолчанию False)
3. Реализуйте сериализатор для модели Task.
4. Реализуйте CRUD операции для Task через RESTful API:
   - Получение списка задач (GET)
   - Создание новой задачи (POST)
   - Обновление задачи (PUT/PATCH)
   - Удаление задачи (DELETE)
5. Напишите тесты для API с использованием Django тестов и Django REST Framework тестового клиента.

## Эндпоинты API: 

- Получение списка задач (GET): 
```
api/task/
```
- Создание новой задачи (POST): 
```
/api/tasks/
```
- Обновление задачи (PUT): 
```
/api/tasks/<id>/
```
- Частичное обновление задачи (PATCH): 
```
api/tasks/<id>/
```
- Удаление задачи (DELETE): 
```
/api/tasks/<id>/
```

## Запуск тестов

**Для запуска тестов выполните следующую команду**:
```
python manage.py test
```


    
