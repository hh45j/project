# StudyCards — генератор карточек для учёбы

Мини-скрипт на Python, который превращает конспекты в Markdown в набор
карточек для запоминания (вопрос → ответ) и экспортирует их в CSV для Anki.

## Документация

Вся документация проекта находится в Wiki:

**https://github.com/hh45j/project/wiki**

| Страница | Содержание |
|----------|------------|
| [Home](https://github.com/hh45j/project/wiki/Home) | Описание проекта и навигация |
| [Ideas](https://github.com/hh45j/project/wiki/Ideas) | Три идеи проекта |
| [Evaluation](https://github.com/hh45j/project/wiki/Evaluation) | Оценка идей тремя экспертами |
| [Concept](https://github.com/hh45j/project/wiki/Concept) | Концепция, устав, экономика |
| [Stakeholders](https://github.com/hh45j/project/wiki/Stakeholders) | Заинтересованные стороны |

## Суть проекта

- **Проблема:** создание карточек для запоминания вручную отнимает время.
- **Решение:** скрипт читает Markdown-конспект и автоматически делает карточки.
- **Результат:** готовый CSV для Anki + режим тренировки в терминале.

## Эксперты

- Эксперт 1 — expert_anna
- Эксперт 2 — expert_max

## Технологии

- Python 3 (стандартная библиотека)
- Markdown
- CSV / JSON

## Лицензия

MIT



## Структура репозитория

- `src/` — код скрипта (`studycards.py`)
- `content/` — примеры конспектов в Markdown
- `data/` — сгенерированные CSV/JSON для Anki
- `docs/` — дополнительная документация

## Как запустить

1. Установите Python 3.
2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/hh45j/project.git
   cd project
3. Запустите скрипт:

   ```bash
   python src/studycards.py
   ```

4. На выходе получите файл с карточками в `data/`.


## Roadmap

- v0.1 — MVP: парсинг Markdown и экспорт в CSV
- v0.2 — режим тренировки в терминале
- v0.3 — статистика ответов
- v1.0 — релиз

- 
## Авторы

- hh45j — идея и реализация


## Навигация

- [Wiki проекта](https://github.com/hh45j/project/wiki)
- [Структура репозитория](#структура-репозитория)
- [Как запустить](#как-запустить)