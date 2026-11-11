from dataclasses import dataclass


@dataclass
class Card:
    """Одна карточка: вопрос и ответ."""
    question: str
    answer: str


def _add_card(cards, question, answer_lines):
    """Добавляет карточку, если есть вопрос и непустой ответ."""
    answer = "\n".join(answer_lines).strip()
    if question and answer:
        cards.append(Card(question, answer))


def parse_markdown(text):
    """Разбирает конспект: заголовок '## ' = вопрос, текст под ним = ответ."""
    cards = []
    question = None
    answer_lines = []
    for line in text.splitlines():
        if line.startswith("## "):
            _add_card(cards, question, answer_lines)
            question = line[3:].strip()
            answer_lines = []
        elif question is not None:
            answer_lines.append(line)
    _add_card(cards, question, answer_lines)
    return cards


def remove_duplicates(cards):
    """Убирает карточки с повторяющимся вопросом.

    Возвращает пару: список без повторов и число пропущенных карточек.
    """
    seen = set()
    unique = []
    for card in cards:
        key = card.question.strip().lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(card)
    return unique, len(cards) - len(unique)


def report_skipped(skipped):
    """Выводит сообщение о числе пропущенных карточек."""
    print(f"Пропущено: {skipped}")