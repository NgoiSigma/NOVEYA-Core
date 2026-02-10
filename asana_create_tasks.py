"""
Script to create strategic tasks in Asana using the Personal Access Token (PAT).

This script reads a predefined list of tasks (names and detailed descriptions)
and creates each task under a specified project. Each task's description
includes the Nebi‑Ula cycle (Initiation/Thesis, Conflict/Antithesis, Synthesis,
Test and Stop‑Condition) along with a meta‑tag `#NebiUla_Init` that triggers
downstream automation.

Instructions:
1. Install the `requests` package if it is not already available.
2. Replace `ASANA_PAT` with your Personal Access Token.
3. Replace `PROJECT_GID` with the gid of your Asana project.
4. Run the script with `python asana_create_tasks.py`.

Note: This script does not attempt to handle pagination or existing tasks;
running it multiple times will create duplicate tasks. Use with care.
"""

import json
import requests


# TODO: Insert your Asana PAT here
ASANA_PAT = "YOUR_ASANA_PAT"

# TODO: Insert your project gid here
PROJECT_GID = "YOUR_PROJECT_GID"


def build_tasks():
    """Return a list of dictionaries representing the tasks to be created."""
    tasks = []

    # 01 Governance
    tasks.append({
        "name": "[01] GOVERNANCE: Создание устава \"Цифровой Общины\" (DAO-структура)",
        "notes": (
            "#NebiUla_Init\n"
            "Initiation (Thesis): Система пока лишена формализованного устава; управление происходит стихийно.\n"
            "Conflict (Antithesis): Отсутствие \"руля-языка\" приводит к дрейфу и усиливает борьбу между централизацией и распределением.\n"
            "Synthesis: Разработать гибкий устав DAO, где малые корректировки (руль-язык) задают курс всему проекту.\n"
            "Test: Провести моделирование и голосование, чтобы убедиться, что небольшие изменения действительно управляют динамикой.\n"
            "Stop-Condition: Устав принят, конфликты снижены, управление работает плавно."
        )
    })

    # 02 Energy
    tasks.append({
        "name": "[02] ENERGY: Карта точек магнитного резонанса и децентрализованной генерации",
        "notes": (
            "#NebiUla_Init\n"
            "Initiation (Thesis): Энергосистема зависит от внешних сетей, локальная генерация не развита.\n"
            "Conflict (Antithesis): Дефицит генерации при росте потребления; неизвестны подходящие места для микрогенераторов.\n"
            "Synthesis: Создать карту магнитных резонансных точек и план распределения мощности по принципу \"клин журавлей\".\n"
            "Test: Запустить пилотные кластеры генерации, наблюдая их стабильность.\n"
            "Stop-Condition: Карта опубликована, пилотные узлы обеспечивают часть потребностей."
        )
    })

    # 03 Ecology
    tasks.append({
        "name": "[03] ECOLOGY: Протокол биологической нормализации (очистка лимана/рек)",
        "notes": (
            "#NebiUla_Init\n"
            "Initiation (Thesis): Воды лимана и рек загрязнены, экосистемы деградируют.\n"
            "Conflict (Antithesis): Восстановление сталкивается с экономическими интересами и отсутствием единой методики.\n"
            "Synthesis: Разработать протокол очистки с биофильтрами и \"свойствами клевера\" для регенерации.\n"
            "Test: Провести тестовые мероприятия на небольшом участке и измерить показатели.\n"
            "Stop-Condition: Качество воды стабильно улучшается, протокол принят как стандарт."
        )
    })

    # 04 Science
    tasks.append({
        "name": "[04] SCIENCE: Программа обучения операторов ФДЛ",
        "notes": (
            "#NebiUla_Init\n"
            "Initiation (Thesis): Операторы не владеют формально-диалектической логикой.\n"
            "Conflict (Antithesis): Отсутствие структуры обучения приводит к разрозненности знаний.\n"
            "Synthesis: Организовать обучение по принципу \"клин журавлей\": участники поддерживают друг друга, чередуя роли ведущего и ведомых.\n"
            "Test: Запустить пилотный курс и наблюдать, как формируется коллективный ритм.\n"
            "Stop-Condition: Программа сертифицирована и внедрена, выпускники демонстрируют синхронизацию мышления."
        )
    })

    # 05 Economy
    tasks.append({
        "name": "[05] ECONOMY: Токенизация локальных ресурсов (Экономика Дарения/Обмена)",
        "notes": (
            "#NebiUla_Init\n"
            "Initiation (Thesis): Локальная экономика ориентируется на внешние валюты; общинные ресурсы не учитываются.\n"
            "Conflict (Antithesis): Введение токена сталкивается с вопросами доверия и законодательства.\n"
            "Synthesis: Создать токен, отражающий труд и ресурсы, управляемый DAO.\n"
            "Test: Запустить пилотный оборот токена в небольшой группе участников и оценить его влияние.\n"
            "Stop-Condition: Токен принят сообществом, оборот устойчив и поддерживает обмен."
        )
    })

    # 06 Security
    tasks.append({
        "name": "[06] SECURITY: Кибер-щит на базе протокола Proton",
        "notes": (
            "#NebiUla_Init\n"
            "Initiation (Thesis): Данные проекта уязвимы; отсутствует единый стандарт защиты.\n"
            "Conflict (Antithesis): Усиление защиты может усложнить сотрудничество и коммуникацию.\n"
            "Synthesis: Внедрить Proton‑VPN и шифрованную почту, распределив ответственность за безопасность по принципу \"клин журавлей\".\n"
            "Test: Провести тестовую рассылку и обмен документов через защищённые каналы.\n"
            "Stop-Condition: Все коммуникации перешли на зашифрованные каналы, безопасность повышена."
        )
    })

    # 07 Culture
    tasks.append({
        "name": "[07] CULTURE: \"Собор Двунадесятых Тезисов\" (Этическая конституция проекта)",
        "notes": (
            "#NebiUla_Init\n"
            "Initiation (Thesis): Община не имеет единого этического каркаса; между участниками существуют меридианные разрывы.\n"
            "Conflict (Antithesis): Попытка создать общий кодекс может усилить разногласия.\n"
            "Synthesis: Сформировать двенадцать тезисов, устраняющих дискретность меридианов и соединяющих разные группы.\n"
            "Test: Организовать встречи для разработки тезисов и оценить, насколько они объединяют участников.\n"
            "Stop-Condition: Тезисы приняты большинством и используются во всех секторах как этический ориентир."
        )
    })

    # 08 Urban
    tasks.append({
        "name": "[08] URBAN: План застройки \"Живого Города\" (Биомеханические кластеры)",
        "notes": (
            "#NebiUla_Init\n"
            "Initiation (Thesis): Городская инфраструктура устарела и фрагментирована.\n"
            "Conflict (Antithesis): Гармоничная застройка сталкивается с бюрократией и различными интересами.\n"
            "Synthesis: Разработать мастер‑план биомеханических кластеров: как в \"клине журавлей\", каждый кластер поддерживает следующий.\n"
            "Test: Построить прототип кластера и оценить влияние на транспорт, энергию и экологию.\n"
            "Stop-Condition: Концепция одобрена и масштабируется по всему городу."
        )
    })

    return tasks


def create_tasks(tasks):
    """Send POST requests to Asana to create each task."""
    url = "https://app.asana.com/api/1.0/tasks"
    headers = {
        "Authorization": f"Bearer {ASANA_PAT}",
        "Content-Type": "application/json",
    }
    for task in tasks:
        payload = {
            "data": {
                "name": task["name"],
                "notes": task["notes"],
                "projects": [PROJECT_GID],
            }
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(task["name"], response.status_code)
        try:
            data = response.json()
            print("Response:", data)
        except Exception:
            print("Response text:", response.text)


if __name__ == "__main__":
    if ASANA_PAT == "YOUR_ASANA_PAT" or PROJECT_GID == "YOUR_PROJECT_GID":
        raise SystemExit(
            "Please replace ASANA_PAT and PROJECT_GID with your actual token and project gid before running the script."
        )
    tasks = build_tasks()
    create_tasks(tasks)