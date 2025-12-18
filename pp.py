"""
Текстовая игра-новелла "Тайны Забытого Замка"
Разработана для демонстрации работы с коллекциями данных в Python
"""

import time

inventory = []  
opened_doors = set()
completed_tasks = set()  
player_stats = {} 
rooms = []  
room_coordinates = {}  
items = {}  
monsters = [] 
puzzles = {} 


def init_game():
    """Инициализация игрового мира"""
    global player_stats, rooms, room_coordinates, items, monsters, puzzles
    
    player_stats.update({
        'name': '',
        'health': 100,
        'strength': 10,
        'intelligence': 10,
        'level': 1
    })
    
    rooms = [
        ('Главный зал', 'Большой зал с высокими потолками'),
        ('Библиотека', 'Комната, полная старых книг'),
        ('Оружейная', 'Стены украшены старинным оружием'),
        ('Кухня', 'Заброшенная кухня с запахом плесени'),
        ('Тронный зал', 'Величественный зал с троном'),
        ('Подземелье', 'Темное и сырое подземелье'),
        ('Сокровищница', 'Комната, полная сокровищ'),
        ('Секретная комната', 'Скрытая от посторонних глаз')
    ]
    
    room_coordinates = {
        'Главный зал': (0, 0),
        'Библиотека': (1, 0),
        'Оружейная': (0, 1),
        'Кухня': (-1, 0),
        'Тронный зал': (0, -1),
        'Подземелье': (2, 2),
        'Сокровищница': (-2, -2),
        'Секретная комната': (3, 3)
    }
    
    items = {
        'золотой ключ': {'тип': 'ключ', 'сила': 5, 'комната': 'Библиотека'},
        'серебряный ключ': {'тип': 'ключ', 'сила': 3, 'комната': 'Оружейная'},
        'старый ключ': {'тип': 'ключ', 'сила': 1, 'комната': 'Кухня'},
        'меч': {'тип': 'оружие', 'урон': 15, 'комната': 'Оружейная'},
        'щит': {'тип': 'защита', 'броня': 10, 'комната': 'Главный зал'},
        'зелье здоровья': {'тип': 'зелье', 'восстановление': 30, 'комната': 'Подземелье'},
        'книга заклинаний': {'тип': 'артефакт', 'магия': 20, 'комната': 'Библиотека'},
        'сокровище': {'тип': 'цель', 'ценность': 100, 'комната': 'Сокровищница'}
    }
    
    monsters = [
        {'имя': 'Гоблин', 'здоровье': 50, 'урон': 10, 'комната': 'Оружейная', 'слабость': 'меч'},
        {'имя': 'Призрак', 'здоровье': 70, 'урон': 15, 'комната': 'Библиотека', 'слабость': 'книга заклинаний'},
        {'имя': 'Огр', 'здоровье': 100, 'урон': 20, 'комната': 'Тронный зал', 'слабость': 'зелье здоровья'},
        {'имя': 'Дракон', 'здоровье': 150, 'урон': 25, 'комната': 'Сокровищница', 'слабость': 'все ключи'}
    ]
    
    puzzles = {
        'Библиотека': {
            'вопрос': 'Что всегда идет, но никогда не приходит?',
            'ответ': 'время',
            'награда': 'золотой ключ'
        },
        'Оружейная': {
            'вопрос': 'Чем больше берешь, тем больше становиться. Что это?',
            'ответ': 'яма',
            'награда': 'серебряный ключ'
        },
        'Кухня': {
            'вопрос': 'Висит груша — нельзя скушать. Что это?',
            'ответ': 'лампочка',
            'награда': 'старый ключ'
        }
    }

def print_with_delay(text, delay=0.03):
    """Вывод текста с задержкой для эффекта печатания"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def show_status():
    """Показать статус игрока"""
    print_with_delay("\n" + "="*50)
    print_with_delay(f"Игрок: {player_stats['name']}")
    print_with_delay(f"Здоровье: {player_stats['health']}/100")
    print_with_delay(f"Уровень: {player_stats['level']}")
    print_with_delay(f"Инвентарь: {', '.join(inventory) if inventory else 'пустой'}")
    print_with_delay(f"Открытые двери: {len(opened_doors)}")
    print_with_delay(f"Выполненные задачи: {len(completed_tasks)}")
    print_with_delay("="*50)

def explore_room(room_name):
    """Исследовать комнату"""
    print_with_delay(f"\nВы находитесь в: {room_name}")
    
    found_items = []
    for item_name, item_data in items.items():
        if item_data.get('комната') == room_name and item_name not in inventory:
            found_items.append(item_name)
    
    if found_items:
        print_with_delay(f"Вы нашли: {', '.join(found_items)}")
        choice = input("Взять предметы? (да/нет): ").lower()
        if choice == 'да':
            for item in found_items:
                inventory.append(item) 
                print_with_delay(f"Вы взяли: {item}")
    
    for monster in monsters:
        if monster['комната'] == room_name:
            print_with_delay(f"\nОсторожно! В комнате {monster['имя']}!")
            return monster
    
    if room_name in puzzles and room_name not in completed_tasks:
        print_with_delay("\nВы обнаружили загадку!")
        return 'puzzle'
    
    return None

def solve_puzzle(room_name):
    """Решить загадку в комнате"""
    puzzle = puzzles[room_name]
    print_with_delay(f"\nЗагадка: {puzzle['вопрос']}")
    
    answer = input("Ваш ответ: ").lower().strip()
    
    if answer == puzzle['ответ']:
        print_with_delay("Правильно! Загадка разгадана!")
        if puzzle['награда'] not in inventory:
            inventory.append(puzzle['награда'])
            print_with_delay(f"Вы получили: {puzzle['награда']}")
        completed_tasks.add(room_name) 
        return True
    else:
        print_with_delay("Неправильно! Попробуйте еще раз позже.")
        return False

def fight_monster(monster):
    """Сразиться с монстром"""
    print_with_delay(f"\nВы встретили {monster['имя']}!")
    print_with_delay(f"Здоровье монстра: {monster['здоровье']}")
    
    while monster['здоровье'] > 0 and player_stats['health'] > 0:
        print_with_delay("\n1. Атаковать")
        print_with_delay("2. Использовать предмет")
        print_with_delay("3. Попытаться убежать")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            damage = player_stats['strength']
            monster['здоровье'] -= damage
            print_with_delay(f"Вы нанесли {damage} урона!")
            
            if monster['здоровье'] > 0:
                player_stats['health'] -= monster['урон']
                print_with_delay(f"{monster['имя']} нанес вам {monster['урон']} урона!")
        
        elif choice == '2':
            if inventory:
                print_with_delay(f"Ваш инвентарь: {inventory}")
                item = input("Выберите предмет для использования: ")
                
                if item in inventory:
                    if monster['слабость'] in item or monster['слабость'] == 'все ключи' and 'ключ' in items.get(item, {}).get('тип', ''):
                        monster['здоровье'] = 0
                        print_with_delay(f"Вы использовали {item}! Это слабость монстра!")
                    else:
                        print_with_delay("Этот предмет не эффективен против этого монстра.")
                else:
                    print_with_delay("У вас нет такого предмета!")
            else:
                print_with_delay("Ваш инвентарь пуст!")
        
        elif choice == '3':
            print_with_delay("Вы сбежали из боя!")
            return False
        
        if monster['здоровье'] > 0:
            print_with_delay(f"Здоровье монстра: {monster['здоровье']}")
        print_with_delay(f"Ваше здоровье: {player_stats['health']}")
    
    if monster['здоровье'] <= 0:
        print_with_delay(f"\nВы победили {monster['имя']}!")
        completed_tasks.add(f"победить_{monster['имя'].lower()}")
        player_stats['level'] += 1
        return True
    else:
        print_with_delay("\nВы проиграли...")
        return False

def use_item():
    """Использовать предмет из инвентаря"""
    if not inventory:
        print_with_delay("Ваш инвентарь пуст!")
        return
    
    print_with_delay(f"Ваш инвентарь: {inventory}")
    item = input("Выберите предмет для использования: ")
    
    if item in inventory:
        item_type = items.get(item, {}).get('тип', '')
        
        if item_type == 'зелье':
            heal_amount = items[item].get('восстановление', 0)
            player_stats['health'] = min(100, player_stats['health'] + heal_amount)
            print_with_delay(f"Вы использовали {item}. Здоровье восстановлено на {heal_amount}!")
            inventory.remove(item)  
        
        elif item_type == 'ключ':
            print_with_delay(f"Ключи в инвентаре: {[i for i in inventory if 'ключ' in i]}")
            if len([i for i in inventory if 'ключ' in i]) >= 3:
                print_with_delay("У вас есть все три ключа! Вы можете открыть главную дверь!")
                opened_doors.add('главная дверь') 
            else:
                print_with_delay("Этот ключ может пригодиться позже.")
        
        else:
            print_with_delay(f"Вы осматриваете {item}, но сейчас его нельзя использовать.")
    else:
        print_with_delay("У вас нет такого предмета!")


def level_1():
    """Первый уровень: Исследование замка и поиск ключей"""
    print_with_delay("\n" + "="*50)
    print_with_delay("УРОВЕНЬ 1: ИССЛЕДОВАНИЕ ЗАМКА")
    print_with_delay("="*50)
    print_with_delay("\nВы очнулись в главном зале древнего замка.")
    print_with_delay("Вокруг тишина и пыль веков.")
    print_with_delay("Ваша цель: найти 3 ключа, спрятанных в разных комнатах.")
    
    rooms_to_explore = ['Главный зал', 'Библиотека', 'Оружейная', 'Кухня']
    current_room_index = 0
    
    while len([i for i in inventory if 'ключ' in i]) < 3:
        current_room = rooms_to_explore[current_room_index]
        print_with_delay(f"\nТекущая комната: {current_room}")
        
        encounter = explore_room(current_room)
        
        if encounter == 'puzzle':
            solve_puzzle(current_room)
        
        elif isinstance(encounter, dict):  
            print_with_delay("Чтобы продолжить, нужно разобраться с монстром!")
            if not fight_monster(encounter):
                print_with_delay("Вы отступили назад...")
                current_room_index = max(0, current_room_index - 1)
                continue
        
        print_with_delay("\nКуда дальше?")
        for i, room in enumerate(rooms_to_explore):
            if room != current_room:
                print_with_delay(f"{i+1}. {room}")
        
        print_with_delay("0. Показать статус")
        print_with_delay("9. Использовать предмет")
        
        try:
            choice = int(input("Выберите комнату для перехода: "))
            
            if choice == 0:
                show_status()
                continue
            elif choice == 9:
                use_item()
                continue
            elif 1 <= choice <= len(rooms_to_explore):
                current_room_index = choice - 1
            else:
                print_with_delay("Неверный выбор!")
        
        except ValueError:
            print_with_delay("Введите число!")
    
    print_with_delay("\nПоздравляем! Вы нашли все 3 ключа!")
    print_with_delay("Теперь вы можете открыть главную дверь и перейти на следующий уровень!")
    return True

def level_2():
    """Второй уровень: Битва с драконом"""
    print_with_delay("\n" + "="*50)
    print_with_delay("УРОВЕНЬ 2: СХВАТКА С ДРАКОНОМ")
    print_with_delay("="*50)
    print_with_delay("\nВы открыли главную дверь и попали в сокровищницу.")
    print_with_delay("Но здесь вас ждет страшный страж - Дракон!")
    print_with_delay("Чтобы победить его, вам понадобятся все ваши навыки и предметы.")
    
    dragon = next((m for m in monsters if m['имя'] == 'Дракон'), None)
    
    if dragon:
        print_with_delay("\nПеред вами могучий Дракон, охраняющий сокровища!")
        print_with_delay("Его слабость - магическая сила всех собранных ключей.")
        
        if fight_monster(dragon):
            print_with_delay("\nУРА! Вы победили Дракона!")
            print_with_delay("Перед вами открываются несметные сокровища!")
            
            if 'сокровище' in items and 'сокровище' not in inventory:
                inventory.append('сокровище')
                print_with_delay("Вы нашли главное сокровище замка!")
            
            return True
        else:
            return False
    
    return False


def main():
    """Главная функция игры"""
    print_with_delay("="*60)
    print_with_delay("      ТАЙНЫ ЗАБЫТОГО ЗАМКА")
    print_with_delay("          Текстовая игра-новелла")
    print_with_delay("="*60)
    
    init_game()
    
    player_stats['name'] = input("\nВведите имя вашего персонажа: ")
    
    print_with_delay(f"\nДобро пожаловать, {player_stats['name']}!")
    print_with_delay("Вы заблудились в древнем заброшенном замке.")
    print_with_delay("Чтобы выбраться, вам нужно пройти два уровня испытаний.")
    print_with_delay("Удачи!\n")
    
    if level_1():
        print_with_delay("\n" + "="*50)
        print_with_delay("УРОВЕНЬ 1 ПРОЙДЕН!")
        print_with_delay("="*50)
        
        if level_2():
            print_with_delay("\n" + "="*50)
            print_with_delay("   ПОБЕДА! ВЫ ПРОШЛИ ИГРУ!")
            print_with_delay("="*50)
            print_with_delay(f"\nИтоговый счет:")
            print_with_delay(f"Игрок: {player_stats['name']}")
            print_with_delay(f"Уровень: {player_stats['level']}")
            print_with_delay(f"Предметов собрано: {len(inventory)}")
            print_with_delay(f"Задач выполнено: {len(completed_tasks)}")
            print_with_delay(f"Дверей открыто: {len(opened_doors)}")
            print_with_delay("\nСпасибо за игру!")
        else:
            print_with_delay("\nК сожалению, дракон оказался сильнее...")
            print_with_delay("Игра окончена.")
    else:
        print_with_delay("\nВы не смогли найти все ключи...")
        print_with_delay("Игра окончена.")
    
    print_with_delay("\n" + "="*50)
    print_with_delay("ФИНАЛЬНАЯ СТАТИСТИКА:")
    print_with_delay("="*50)
    show_status()


if __name__ == "__main__":
    main()