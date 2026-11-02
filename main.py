from models import Operator, OperatorLanguage, ProgrammingLanguage

def create_test_data():
    """Вернуть списки из 4 операторов, 3 языков и 5 связей."""
    languages = [
        ProgrammingLanguage(1, "Java"),
        ProgrammingLanguage(2, "Python"),
        ProgrammingLanguage(3, "C++"),
    ]
    operators = [
        Operator(1, "Оператор присваивания", 1, 2),
        Operator(2, "Арифметический оператор", 3, 2),
        Operator(3, "Логический оператор", 2, 3),
        Operator(4, "Арифметический сдвиг", 4, 1),
    ]
    operator_languages = [
        OperatorLanguage(1, 2),
        OperatorLanguage(3, 3),
        OperatorLanguage(4, 1),
        OperatorLanguage(2, 2),
        OperatorLanguage(2, 3),
    ]
    return operators, languages, operator_languages


def query_b1(operators, languages):
    """В1: операторы на кириллическую «А» и их языки (один ко многим)."""
    return [
        (operator.name, language.name)
        for operator in operators
        for language in languages
        if operator.language_id == language.id
        and operator.name.startswith("А")
    ]


def query_b2(operators, languages):
    """В2: минимальная сложность по языкам, по возрастанию минимума."""
    complexities_by_language = {
        language.id: [
            operator.complexity
            for operator in operators
            if operator.language_id == language.id
        ]
        for language in languages
    }
    minimums = [
        (language.name, min(complexities_by_language[language.id]))
        for language in languages
        if complexities_by_language[language.id]
    ]
    return sorted(minimums, key=lambda item: item[1])


def query_b3(operators, languages, operator_languages):
    """В3: все пары из связи «многие ко многим», по названию оператора."""
    pairs = [
        (operator.name, language.name)
        for link in operator_languages
        for operator in operators
        for language in languages
        if link.operator_id == operator.id and link.language_id == language.id
    ]
    return sorted(pairs, key=lambda item: item[0])

def main():
    operators, languages, operator_languages = create_test_data()
    print("В1. Операторы на кириллическую букву «А» (один ко многим):")
    for operator_name, language_name in query_b1(operators, languages):
        print(f"{operator_name} — {language_name}")

    print("\nВ2. Минимальная условная сложность в баллах (по возрастанию):")
    for language_name, complexity in query_b2(operators, languages):
        print(f"{language_name} — {complexity}")

    print("\nВ3. Все пары, по названию оператора (многие ко многим):")
    for operator_name, language_name in query_b3(
        operators, languages, operator_languages
    ):
        print(f"{operator_name} — {language_name}")

if __name__ == "__main__":
    main()
