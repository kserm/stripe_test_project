# Тестовое задание Stripe API + Django.
##### автор: Ермачков Константин
____________________________________________
## **Адрес проекта.**
### [kserm.pythonanywhere.com](http://kserm.pythonanywhere.com/)

### Учетная запись администратора:
- username: admin_user1
- password: adpass123 

____________________________________________
## **Описание.**
Пример реализации оплаты товаров с использованием Stripe API в Django проекте.
Реализована модель Item, содержащая поля name (название товара), description 
(описание товара) и price (цена). На главной странице выводятся все имеющиеся 
товары, при переходе на страницу конкретного товара можно нажать кнопку "Buy"
и перейти на страницу оплаты или вернуться на главную страницу.
Для добавления нового товара необходимо отправить POST запрос на адрес:

`<project_url>/api/item/`

следующего содержания:
```
{
	"name": "Test",
	"description": "Test",
	"price": 1000
}
```

Аутентификация не требуется.

## **Используемые технологии.**
- Python 3.11
- Django 4.1
- SQLite
- DRF
- Docker

## **Шаблон наполнения env-файла.**
``` 
STRIPE_PUBLIC_KEY=pk_test_******
STRIPE_SECRET_KEY=sk_test_******
```

## **Описание команд для запуска проекта локально.**
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:kserm/stripe_test_project.git
```

```
cd stripe_test_project/stripe_project
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Создайте в рабочей директории файл с переменными окружения `.env`.
(Содержимое файла см. в разделе "Шаблон наполнения env-файла")

*(Опционально) выполните загрузку тестовых данных:*
```
python3 manage.py loaddata fixtures.json
```

Запустить проект:

```
python3 manage.py runserver
```

### **Создание суперпользователя**
Для создания superuser выполните команду:
```
python3 manage.py createsuperuser
```


## **Описание команд для запуска приложения в контейнере.**
*(Опционально) Создайте директорию и перейдите в нее:*
```
mkdir stripe_test_project
cd stripe_test_project 
```
Создайте в рабочей директории файл с переменными окружения `.env`.
(Содержимое файла см. в разделе "Шаблон наполнения env-файла")

После заполнения файла .env выполните команду:
```
docker run --env-file .env -it -p 80:80 kserm27/stripe-test-project
```

После успешного выполнения команды проект доступен по адресу:

`http://localhost/`