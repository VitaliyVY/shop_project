# Лабораторна робота №2

## Тема

**Розробка розширень агента: Slash Commands і Skills в Antigravity.**

## Мета роботи

Набути практичних навичок створення багаторазових Skills і slash-команд для агента Antigravity, навчитися задавати їх через frontmatter, запускати вручну та перевіряти автоматичний вибір Skill за змістом запиту.

## 1. Вихідна структура проєкту

Для виконання лабораторної роботи використано навчальний Python-проєкт системи керування інтернет-магазином.

Основні компоненти проєкту:

- `main.py` — точка запуску демонстраційної програми;
- `src/models.py` — моделі `Product`, `User`, `OrderItem`, `Order`;
- `src/products.py` — каталог товарів;
- `src/users.py` — реєстр користувачів;
- `src/orders.py` — створення замовлень і зміна залишків;
- `src/payments.py` — імітація оплати;
- `src/statistics.py` — статистичні розрахунки;
- `src/utils.py` — допоміжні функції;
- `tests/` — автоматизовані тести;
- `requirements.txt` — залежність `pytest`;
- `pytest.ini` — конфігурація запуску тестів.

Проєкт написаний мовою Python і використовує стандартну бібліотеку та pytest для тестування. Дані зберігаються в пам'яті, база даних не використовується.

(ВСТАВИТИ СКРІНШОТ 1: початкова структура проєкту в Antigravity або VS Code)

## 2. Створення Skills

Для Antigravity було створено три Skills у каталозі `.agents/skills/`:

```text
.agents/skills/code-planner/SKILL.md
.agents/skills/code-explainer/SKILL.md
.agents/skills/release-notes/SKILL.md
```

Кожен Skill має YAML frontmatter із полями `name` і `description`. Поле `description` описує призначення Skill і використовується агентом для автоматичного вибору відповідного інструмента.

(ВСТАВИТИ СКРІНШОТ 2: дерево каталогу `.agents/skills`)

### 2.1. Skill Code Planner

Файл: `.agents/skills/code-planner/SKILL.md`.

Code Planner призначений для read-only аналізу проєкту. Він:

- досліджує структуру репозиторію;
- визначає мову, фреймворки, бібліотеки та інструменти;
- аналізує основні source-файли;
- аналізує відповідні тести;
- визначає залежності між компонентами;
- визначає файли, які потенційно потрібно змінити;
- формує покроковий план реалізації.

Skill не повинен змінювати, створювати або видаляти файли.

### 2.2. Skill Code Explainer

Файл: `.agents/skills/code-explainer/SKILL.md`.

Code Explainer пояснює архітектуру, source-файли, залежності, потік даних і тестове покриття проєкту. Він також працює в read-only режимі.

### 2.3. Skill Release Notes

Файл: `.agents/skills/release-notes/SKILL.md`.

Release Notes аналізує `git status`, `git diff` і `git log`, після чого формує структурований звіт про зміни. Skill не виконує commit, stage, revert або редагування файлів.

## 3. Перевірка ручного запуску Code Planner

Для ручного запуску в Antigravity використано slash-команду:

```text
/code-planner Analyze this project's architecture and prepare a plan for adding a new feature.
```

Antigravity розпізнав команду `/code-planner`, прочитав відповідний `SKILL.md`, дослідив структуру проєкту, source-файли і тести, а потім сформував структурований план.

Оскільки конкретний функціонал у запиті не був заданий, агент запропонував як приклад функціонал скасування замовлення та відновлення залишків. Це була лише рекомендація в плані, фактичних змін у код не внесено.

(ВСТАВИТИ СКРІНШОТ 3: ручний запуск `/code-planner` і початок результату аналізу)

## 4. Перевірка автоматичного вибору Code Planner

Для перевірки автоматичного вибору Skill використано звичайний prompt без назви Skill:

```text
Analyze this project's architecture and prepare a detailed plan for adding a new feature. First inspect the project structure, main components, libraries, dependencies, and relevant tests. Do not modify the code.
```

Antigravity автоматично визначив, що запит відповідає `description` Skill `code-planner`, і виконав аналіз проєкту без явної slash-команди.

Це демонструє різницю між двома способами запуску:

- slash-команду запускає користувач явно;
- Skill може бути автоматично вибраний агентом за змістом запиту та полем `description`.

(ВСТАВИТИ СКРІНШОТ 4: автоматичний запуск Code Planner без згадки назви Skill)

## 5. Перевірка Code Explainer

### 5.1. Ручний запуск

```text
/code-explainer Explain this project's architecture, modules, dependencies, data flow, and tests. Do not modify the code.
```

У результаті Antigravity описав:

- мову Python і середовище виконання;
- основні модулі `src/`;
- залежності між `models.py` та сервісними модулями;
- потік створення користувача, товару та замовлення;
- наявні 11 тестів;
- прогалини тестового покриття.

(ВСТАВИТИ СКРІНШОТ 5: ручний запуск `/code-explainer` та фрагмент результату)

### 5.2. Автоматичний запуск

Для автоматичної активації використано prompt без назви Skill:

```text
Explain this project's architecture, source files, dependencies, data flow, and test coverage. Do not modify the code.
```

Запит відповідає опису `code-explainer`, тому Antigravity автоматично застосував цей Skill і сформував пояснення проєкту.

(ВСТАВИТИ СКРІНШОТ 6: автоматичний запуск Code Explainer без `/code-explainer`)

## 6. Перевірка slash-команди Release Notes

Для ручного запуску використано:

```text
/release-notes
```

Skill виконав аналіз Git-репозиторію за допомогою:

- `git status`;
- `git log`;
- `git diff`.

Також було запущено тестовий набір pytest. У результаті сформовано звіт із розділами `Highlights`, `Changes`, `Fixes`, `Validation` і `Notes`.

(ВСТАВИТИ СКРІНШОТ 7: запуск `/release-notes` і сформований звіт)

## 7. Перевірка тестів проєкту

Для перевірки працездатності Python-проєкту виконано команду:

```powershell
pytest -q
```

Очікуваний і зафіксований результат:

```text
11 passed
```

Тести перевіряють:

- створення замовлень і зміну залишків;
- розрахунок знижки;
- оплату замовлення;
- роботу каталогу товарів;
- статистичні функції;
- створення та пошук користувачів.

(ВСТАВИТИ СКРІНШОТ 8: команда `pytest -q` і результат `11 passed`)

## 8. Перевірка відсутності змін у програмному коді

Після запуску read-only Skills перевірено стан Git:

```powershell
git status --short
```

Skills аналізували проєкт, але не реалізовували функціонал і не змінювали Python-файли.

(ВСТАВИТИ СКРІНШОТ 9: результат `git status --short` після тестування)

## 9. Результати роботи

У результаті лабораторної роботи:

1. Створено Skill `code-planner` для аналізу архітектури та підготовки плану.
2. Створено Skill `code-explainer` для пояснення архітектури та коду.
3. Створено Skill `release-notes` для генерації release notes з Git-історії.
4. Перевірено ручний запуск Skills через slash-команди.
5. Перевірено автоматичний вибір Skills за змістом звичайного prompt.
6. Перевірено роботу тестів проєкту: 11 тестів пройшли успішно.
7. Перевірено read-only поведінку Skills.

## Висновок

Під час лабораторної роботи було створено та протестовано розширення агента Antigravity у вигляді Skills і slash-команд. Ручний запуск виконується користувачем за допомогою команд `/code-planner`, `/code-explainer` і `/release-notes`. Автоматичний режим працює за змістом prompt: агент порівнює запит із полем `description` та вибирає відповідний Skill.

Створені Skills виконують аналіз і формування звітів у read-only режимі, тому вони не змінюють програмний код. Результати тестування підтвердили працездатність Skills і стабільність навчального Python-проєкту.
