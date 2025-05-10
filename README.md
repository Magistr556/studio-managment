# 🎛️ Studio Managment

**Управляйте бронированием студий легко и быстро.**  
Записывайтесь по календарю, отслеживайте историю аренды и управляйте профилем в одно нажатие.

---

## Возможности

- Удобная аренда через календарь
- Отслеживание истории аренд
- Персональный профиль пользователя

---

## Установка и запуск

Скопируйте репозиторий:

```bash
git clone https://github.com/Magistr556/studio-managment
```

Запуск:
```bash
python manage.py runserver
```
---

## Бейджи
![Tests](https://github.com/Magistr556/studio-managment/actions/workflows/tests.yml/badge.svg)
![Build](https://github.com/Magistr556/studio-managment/actions/workflows/build.yml/badge.svg)
![Deploy](https://github.com/Magistr556/studio-managment/actions/workflows/deploy.yml/badge.svg)

### Настроенные Workflow:

| Workflow     | Назначение                                                                                                           | Событие запуска                                 |
| ------------ | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `tests.yml`  | Автоматически запускает тесты Django с помощью `pytest`, чтобы убедиться, что изменения не сломали функциональность. | При каждом push и pull request в ветку `master` |
| `build.yml`  | Проверяет структуру проекта, применяет миграции, собирает статику и выполняет базовую сборку проекта.                | При каждом push и pull request в ветку `master` |
| `deploy.yml` | Выполняет автоматический деплой на [Render](https://render.com) по HTTP-запросу через Deploy Hook.                   | При push в ветку `master`                       |


