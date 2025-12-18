import json
import csv
import os

def task_1_block_5():
    with open('animals.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Животное', 'Среда обитания'])
        writer.writerow(['Медведь', 'Лес'])
        writer.writerow(['Дельфин', 'Океан'])
        writer.writerow(['Верблюд', 'Пустыня'])
    
    animals_list = []
    with open('animals.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            animals_list.append(row)
    
    with open('zoo.json', 'w', encoding='utf-8') as file:
        json.dump(animals_list, file, ensure_ascii=False, indent=4)
    
    print("Задача 5 из блока 1 выполнена")

def task_2_block_2():
    test_data = [
        ['Имя', 'Возраст', 'Город', 'Должность'],
        ['Иван', '28', 'Москва', 'Разработчик'],
        ['Мария', '35', 'Санкт-Петербург', 'Менеджер'],
        ['Алексей', '42', 'Москва', 'Дизайнер'],
        ['Ольга', '31', 'Казань', 'Разработчик'],
        ['Дмитрий', '29', 'Москва', 'Менеджер']
    ]
    
    with open('csv_file.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(test_data)
    
    salary_map = {
        'Разработчик': 120000,
        'Менеджер': 100000,
        'Дизайнер': 90000
    }
    
    rows = []
    with open('csv_file.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        headers.append('Зарплата')
        rows.append(headers)
        
        for row in reader:
            if len(row) >= 4:
                position = row[3]
                salary = salary_map.get(position, 0)
                row.append(str(salary))
                rows.append(row)
    
    with open('employees_with_salary.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Задача 2 из блока 2 выполнена")

def convert_csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        data = []
        with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)
        
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f"CSV {csv_path} -> JSON {json_path}")
    
    except FileNotFoundError:
        print(f"Файл {csv_path} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

def convert_json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        if not data:
            print("JSON файл пуст")
            return
        
        headers = list(data[0].keys())
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"JSON {json_path} -> CSV {csv_path}")
    
    except FileNotFoundError:
        print(f"Файл {json_path} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    print("=" * 50)
    print("5 ВАРИАНТ")
    print("=" * 50)
    
    task_1_block_5()
    print()
    
    task_2_block_2()
    print()
    
    print("Преобразования:")
    print("-" * 40)
    
    convert_csv_to_json('animals.csv', 'animals_converted.json')
    convert_json_to_csv('zoo.json', 'zoo_converted.csv')
    convert_csv_to_json('employees_with_salary.csv', 'employees.json')
    
    print("\n" + "=" * 50)
    print("СОЗДАННЫЕ ФАЙЛЫ:")
    print("=" * 50)
    
    files = [
        'animals.csv', 'zoo.json', 'csv_file.csv',
        'employees_with_salary.csv', 'animals_converted.json',
        'zoo_converted.csv', 'employees.json'
    ]
    
    for file in files:
        if os.path.exists(file):
            print(f"{file} - {os.path.getsize(file)} байт")
        else:
            print(f"{file} - не найден")

if __name__ == "__main__":
    main()