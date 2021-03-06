# Исправляем успеваемость в электронном дневника e-diary

Для использования скрипта необходимо установить [**e-diary**](https://github.com/devmanorg/e-diary).

### Подготовка к работе
Cкопируйте файл `scripts.py` в корень с проектом **e-diary**.

Для запуска скрипта войдите в интерактивный режим с помощью команды:
```shell
python3 manage.py shell
```

Содержимое `scripts.py` вставьте в интерактивный режим.

### Что можно делать с помощью scripts.py
С помощью скрипта можно:
1. Исправлять удовлетворительные и неудовлетворительные оценки на пять. Функция: **fix_marks**.
2. Удалять замечания. Функция: **remove_chastisements**.
3. Присваивать грамоты. Функция: **create_commendation**.

### Как пользоваться?

Вместо 'ИМЯ' подставьте Фамилию и Имя ученика, например, 'Фролов Иван'.

Вместо 'Предмет' подставьте нужный предмет, например, 'Математика'.

1. Для начала необходимо найти нужного ученика, для этого выполните:

```shell
child = get_child('ИМЯ')
```

2. Для исправления всех оценок ниже 4 баллов необходимо ввести в интерактивном режиме:

```shell
fix_marks(child)
```

3. Для удаления всех замечаний ученика необходимо выполнить следующую команду:
```shell
remove_chastisements(child)
```
4. Для присвоения похвалы необходимо указать `child` и Предмет. Похвала будет добавлена к последнему уроку по указанному предмету. Текст похвалы выбирается случайным образом.

```shell
create_commendation(child,'ПРЕДМЕТ')
```

Исправленные данные можно увидеть через web-интерфейс. Для этого запустите проект **e-diary**:
```shell
python3 manage.py runserver
```
Далее в брайзере наберите [http://127.0.0.1:8080](http://127.0.0.1:8080).
Найдите требуемого ученика и проверьте исправления.
