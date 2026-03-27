# Проект интернет-магазина

## Описание проекта

Проект представляет собой реализацию объектно-ориентированной модели  
для управления товарами и категориями. Включает в себя классы  
для работы с продуктами, категориями и утилитами для обработки  
данных из JSON.

E-commerce  — электронная торговля, или электронная коммерция.  
На данном этапе работы мы не будем реализовывать систему платежей,  
однако подготовим всё для того, чтобы у нас появилось ядро для  
интернет-магазина. В дальнейшем для этого ядра возможно будет  
реализовать любой интерфейс — от сайта до телеграм-бота.

## 1. Функциональность

### Веб-страницы


### Сервисы
Основные сущности и инициализации объектов.
Созданы классы ```Product``` и ```Category```
Для классов описаны необходимые атрибуты.
Для класса Category добавлены два атрибута класса:  
- **количество категорий ```category_count```**  
- **количество товаров ```product_count```**  
- Атрибуты класса заполняются автоматически при  
инициализации нового объекта.  
- Созданы два класса наследников класса ```Product```:  
«Смартфон» ```Smartphone``` и «Трава газонная» ```LawnGrass```.
- Класс ```Smartphone``` расширен атрибутами: производительность ```efficiency```,   
модель ```model```, объем встроенной памяти ```memory```, цвет ```color```.
- Класс ```LawnGrass``` расширен атрибутами: страна-производитель ```country```,  
срок прорастания ```germination_period```, цвет ``color``.
- в проекте используются **магические методы** ```__str__``` и ```__add__```
- применяются приватные методы, геттеры и сеттеры к ним.
- Создан абстрактный базовый класс, который является родительским для класса ```Product```
- Классы ```Smartphone``` и ```LawnGrass``` остаются наследниками класса ```Product```
- В проекте реализованы классы-миксины и настроены цепочки последовательной инициации классов  
и правильного множественного наследования.


## 2. Технологии

- **Python 3.11+** - основной язык программирования
- **Pandas** - обработка данных и Excel-файлов
- **Pytest** - тестирование
- **Logging** - логирование
- **NumPy** - математические операции
- **OpenPyXL** - работа с Excel файлами

---

## 3. Установка и запуск

### 3.1. Клонирование репозитория
```bash
git clone https://github.com/LeeParker1603/OOP.git
cd OOP
```

### 3.2. Создание виртуального окружения

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3.3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3.4. Подготовка данных
**Поместите файл ```products.json``` в папку ```data/```.**

```
{
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  }
```

### 3.6. Запуск приложения

```bash
python main.py
```

## 4. Структура проекта

```
OOP/
├── src/
│   ├── __init__.py
│   ├── utils.py          # Загрузка данных JSON
│   ├── category.py       # Класс Category
│   ├── product.py        # Класс Products
├── tests/
│   ├── test_category.py  # Тесты для Category
│   ├── test_product.py   # Тесты для Products
│   ├── test_utils.py     # Тесты для утилит
│   └── conftest.py       # Общие фикстуры для тестов
├── data/                 # Папка для данных
│   └── products.json     # JSON-файл
├── main.py               # Точка входа
├── requirements.txt      # Зависимости
├── pytest.ini            # Настройки pytest
├── .coveragerc           # Настройки покрытия кода
└── README.md             # Документация
```

## 5. Запуск тестов и проверка покрытия

### 5.1. Запуск всех тестов

```bash
pytest tests/ -v
```

### 5.2. Запуск конкретного теста

```bash
pytest tests/test_services.py::test_cashback_rounding -v
```

### 5.3. Проект покрыт модульными (unit) тестами на 96%

```
Name                Stmts   Miss  Cover
---------------------------------------
src\__init__.py         0      0   100%
src\category.py        28      0   100%
src\lawn_grass.py       7      0   100%
src\product.py         52      2    96%
src\smartphone.py       8      0   100%
src\utils.py           24      2    92%
---------------------------------------
TOTAL                 119      4    97%




```

### 5.4. Проверка покрытия кода

```bash
# Базовый отчет
pytest tests/ --cov=src --cov-report=term

# Подробный отчет с пропущенными строками
pytest tests/ --cov=src --cov-report=term-missing

# HTML отчет
pytest tests/ --cov=src --cov-report=html
# Откройте htmlcov/index.html в браузере

# С проверкой минимального покрытия (80%)
```

## 6. Примеры использования


## 7. Примеры JSON-ответов


## 8. Зависимости (requirements.txt)
```txt
# Основные зависимости
black==26.3.1
click==8.3.1
colorama==0.4.6
coverage==7.13.5
flake8==7.3.0
iniconfig==2.3.0
isort==8.0.1
librt==0.8.1
mccabe==0.7.0
mypy==1.19.1
mypy_extensions==1.1.0
packaging==26.0
pathspec==1.0.4
platformdirs==4.9.4
pluggy==1.6.0
pycodestyle==2.14.0
pyflakes==3.4.0
Pygments==2.19.2
pytest==9.0.2
pytest-cov==7.0.0
pytokens==0.4.1
typing_extensions==4.15.0
```

## 13. Автор
Студент: Evgenia Gorobets - Beginner Python developer  
Курс: Python-разработчик  
Дата: march 2026  
Контакты: [leeparker1603@gmail.com](mailto:leeparker1603@gmail.com)
