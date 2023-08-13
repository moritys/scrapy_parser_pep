# Проект: Асинхронный парсер документов PEP на базе фреймворка Scrapy

## Технологии

**Языки программирования, библиотеки и модули:**

[![Python](https://camo.githubusercontent.com/379083b338a68bfd9bd32310ef6977b5fa873b08f25c152445fa935f96e8d4fe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e37253230253743253230332e38253230253743253230332e39253230253743253230332e3130253230253743253230332e31312d626c75653f6c6f676f3d707974686f6e)](https://www.python.org/)  [![csv](https://camo.githubusercontent.com/e4cdc39d2b4b463ec3d2e5b3e3aba91b06e59e7701781dd3e387e2bcdc6c7b3f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d6373762d3436343634363f6c6f676f3d707974686f6e)](https://docs.python.org/3/library/csv.html)  [![collections](https://camo.githubusercontent.com/1ed320671d95188c056db15dd744ad654a6cdc718b918688896e1ec4303a510d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d636f6c6c656374696f6e732d3436343634363f6c6f676f3d707974686f6e)](https://docs.python.org/3/library/collections.html)  [![datetime](https://camo.githubusercontent.com/488e81e39f6ba3fd429ea6ae13986930ef4022d044b20f2889eddb1138a2f93f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d6461746574696d652d3436343634363f6c6f676f3d707974686f6e)](https://docs.python.org/3/library/datetime.html)  [![pathlib](https://camo.githubusercontent.com/fd0a6454ee005dc73ea7f634b37d1d02a0f74034997f4b3893953abe96f2b0ec/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d706174686c69622d3436343634363f6c6f676f3d707974686f6e)](https://docs.python.org/3/library/pathlib.html)  [![typing](https://camo.githubusercontent.com/3c4d74331bd508f82b86be695faf9e4089c7033e8a169067bfdf9975970681b6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d747970696e672d3436343634363f6c6f676f3d507974686f6e)](https://docs.python.org/3/library/typing.html)

**Парсинг - асинхронный фреймворк и селекторы:**

[![Scrapy](https://camo.githubusercontent.com/e3637e48ab75ede9889b7478a3c4d70970cd8d86a61d4639f8686c44091fe1dc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d5363726170792d3436343634363f6c6f676f3d536372617079)](https://docs.scrapy.org/en/latest/)  [![CSS](https://camo.githubusercontent.com/4441d3e8a2b72db6bff2fd89f4086fd49aee4d006f19535b5b78c25bd5979d09/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d4353535f73656c6563746f72732d3436343634363f6c6f676f3d435353)](https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors)  [![XPath](https://camo.githubusercontent.com/5b61b5a89a2c585394e1ef466eb84eff753e073a7bf45df869cdb8865decb5c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d58506174685f73656c6563746f72732d3436343634363f6c6f676f3d5850617468)](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths)

## Описание работы

Парсер собирает ссылки на документы PEP со стартовой страницы по адресу  [https://peps.python.org/](https://peps.python.org/)  и переходит по каждой ссылке, чтобы получить актуальную информацию о каждом PEP документе. Парсер работает в асинхронном режиме, что существенно ускоряет выдачу результата парсинга. Далее парсер обрабатывает информацию и выводит ее в два  **.csv**-файла, уникальные названия которых имеют временную метку:

- В первый файл выводится список [номер, название, статус] всех PEP документов.
- Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе [статус, количество документов]. В последней строке этого файла выводится итоговая информация [Total, общее количество всех документов]. Файлы создаются в папке  **results**  в корне проекта.

## Установка и запуск

Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).

1. Клонируйте репозиторий с GitHub:

`git clone https://github.com/moritys/scrapy_parser_pep.git`

1. Создайте и активируйте виртуальное окружение:

`python -m venv venv && source venv/Scripts/activate`

1. Установите в виртуальное окружение все необходимые зависимости из файла  **requirements.txt**:

`python -m pip install --upgrade pip && pip install -r requirements.txt`

1. Запустите приложение:

`scrapy crawl pep`

### Автор

[Masha](https://github.com/moritys) 🐌
