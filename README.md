# _ycebnaua_praktika1

Работаем

Структура проекта:

```
.
|- res/
|- config.json
|- main.py
|- plot.py
|- PyQt_app.ui
|- requirements.txt
|- Res_rc.py
```

Инструкции для запуска проекта

```bash
pip install -r requirements.txt

python main.py
```

Тестовый сервер можно запустить через [Mockoon](https://mockoon.com/)

В нём нужно открыть файл `openapi_mock.json`

Инструкция по сборке финального исполняемого файла:

```bash
pip install pyinstaller

pyinstaller --onefile main.py
```

После окончания сборки в папке dist появится один исполняемый файл, который можно скопировать на другой компьютер и запустить его там без установки питона и требуемых библиотек
