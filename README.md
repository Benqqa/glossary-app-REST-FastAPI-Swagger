# Glossary API

API для управления глоссарием терминов, построенное с использованием FastAPI.

## Функциональность

- Получение списка всех терминов
- Получение информации о конкретном термине
- Добавление нового термина
- Обновление существующего термина
- Удаление термина

## Технологии

- FastAPI
- SQLAlchemy
- SQLite
- Docker
- Pydantic

## Запуск проекта

### Локальный запуск

1. Установите Python 3.9+
2. Создайте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```
5. Запустите приложение:

```bash
uvicorn app.main:app --reload
```

### Запуск через Docker

```bash
docker-compose up --build
```

## API Документация

После запуска приложения документация доступна по адресу:

- Swagger UI: http://localhost:8000/docs

## Примеры использования

### Создание термина
```bash
curl -X 'POST' \
'http://localhost:8000/terms/' \
-H 'Content-Type: application/json' \
-d '{
"word": "test",
"definition": "test"
}'
```

### Получение термина
```bash
curl -X 'GET' \
'http://localhost:8000/terms/test'
```
