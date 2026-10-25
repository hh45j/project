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