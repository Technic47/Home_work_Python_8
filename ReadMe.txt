Здравствуй читатель!

Интерфейс программы может быть не на 100% интуитивен, так как это ещё не переработанная версия.

В программе уже заложена тестовая база данных для проверки работы приложения.

Для выполнения базовых команд нужно сделать следующее:

Во-первых, выберите основную таблицу:
- правый верхний список для выбора и кнопка "Main Table select" вам в этом помогут.
Выбранная таблица помечается, как главная и все операции будут производиться с ней.

После выбора вы увидите содержимое таблицы.

Форма SELECT поможет вам отфильтровать вывод таблицы:
- в списке выберите ту колонку по которой будет произведена выборка и нажмите "Select column"
- в поле "Request" введите критерий поиска. Регистр имеет значение.
- вывод обновится автоматически.

Вы можете удалить какую-то строку из главной таблицы:
- в левом верхнем поле введите ваш запрос в виде "колонка критерий"
например: testcolumn1 line256.
Тут testcolumn1 - колонка по которой будет искаться значение, а line256 - значение в этой колонке.

Export json - выводит все таблицы в json формат и сохраняет из в папке "results".
Import json - создаёт таблицы из выбранного вами json файла.

Для работы в окне Merge вам необходимо:
- справа сверху в окне приложения выбрать вторую таблицу.
- нажать "2nd Table select".

Далее выберите в окне Merge "Cols for request". Это список колонок из 2‑х таблиц.
Можно выбрать несколько, одну или выбрать "*" для учёта всех колонок.
Обязательно выберите критерий выборки "Merging clause".
По желанию можно выбрать "INNER JOIN" как альтернативный "Method".
После нажимаем на "Merge". Вывод обновится автоматически.

***Для проверки работоспособности можно выбрать основной таблицу "albums",
второй "artists", а критерий выборки "ArtistsId"

Во вкладке "New Table" вы можете создать новую таблицу:
- Введите имя таблицы.
- для добавления колонок введите название колонки напротив "Add column",
выставите предпочтения такие как тип данных (TXT, INT...) и, по желанию,
установите флажки "PRIMARY KEY" и другие.
- нажмите "Add column" и повторите процедуру для добавления других колонок.
- нажмите "Create" для создания таблицы.

Во вкладке "Add to current" вы можете:
- добавить новую линию значений "Add line".
В поле "What to add" введите новые значения, разделяя их по колонкам, например:
"text1 text2 text3" или "text1, text2, text3". Разделитель не играет роли.
Нажмите "ADD" для добавления.

- добавить новую колонку "Add column".
Выставите предпочтения такие как тип данных (TXT, INT...) и, по желанию,
установите флажки "PRIMARY KEY" и другие.
Нажмите "ADD" для добавления.


Спасибо за ознакомления!