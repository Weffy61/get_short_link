#Генератор коротких ссылок

Скрипт для генериации коротких ссылок с сервиса [bitly.com](https://bitly.com), а также проверки их на переходы.  
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2)

##Установка
`git clone https://github.com/Weffy61/get_short_link`

##Установка зависимостей
Переход в директорию с исполняемым файлом и установка  
`cd get_short_link`  
`pip install -r requirements.txt`
##Настройка  
Зарегистрируйтесь на [bitly.com](https://bitly.com).  
Перейдите по [ссылке](https://app.bitly.com/settings/api/) или перейдите вручную `Settings > API`  
Нажмите на кнопку `Generate token` и скопируйте полученный токен  
Создайте в папке `config` файл `.env`. Откройте его для редактирования любым текстовым редактором.  
`TOKEN = 'вставить скопированный токен'`  
## Запуск  

`python main.py`  

Вставьте ссылку для получение bitly ссылки.  
Вставьте bitly ссылку, без указания протокола(HTTP, HTTPS), для получения колличества переходов по ней.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.