import random
import os
import time

STATS_DIR = "game_stats"
STATS_FILE = os.path.join(STATS_DIR, "statistics.txt")

def init_stats():
    if not os.path.exists(STATS_DIR):
        os.makedirs(STATS_DIR)
    if not os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            f.write("Статистика игр в крестики-нолики\n")
            f.write("="*50 + "\n")

def save_game_result(result, players, field_size):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(STATS_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\nДата: {timestamp}\n")
        f.write(f"Размер поля: {field_size}x{field_size}\n")
        f.write(f"Игроки: {players}\n")
        f.write(f"Результат: {result}\n")
        f.write("-"*30 + "\n")

def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_board(board):
    size = len(board)
    print("\n  " + " ".join(str(i) for i in range(size)))
    for i in range(size):
        print(f"{i} " + "|".join(board[i]))
        if i < size - 1:
            print("  " + "-"*(size*2-1))

def check_win(board, player):
    size = len(board)
    
    for i in range(size):
        if all(board[i][j] == player for j in range(size)):
            return True
        if all(board[j][i] == player for j in range(size)):
            return True
    
    if all(board[i][i] == player for i in range(size)):
        return True
    if all(board[i][size-1-i] == player for i in range(size)):
        return True
    
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_valid_move(board, player):
    size = len(board)
    while True:
        try:
            move = input(f"Игрок {player}, введите строку и столбец (например: 1 2): ").split()
            if len(move) != 2:
                print("Введите два числа через пробел!")
                continue
                
            row, col = int(move[0]), int(move[1])
            
            if row < 0 or row >= size or col < 0 or col >= size:
                print(f"Координаты должны быть от 0 до {size-1}!")
                continue
                
            if board[row][col] != ' ':
                print("Эта клетка уже занята!")
                continue
                
            return row, col
        except ValueError:
            print("Введите числа корректно!")
        except Exception:
            print("Ошибка ввода!")

def bot_move(board, player):
    size = len(board)
    empty_cells = [(i, j) for i in range(size) for j in range(size) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else (0, 0)

def play_game(field_size, game_mode):
    board = create_board(field_size)
    players = ['X', 'O']
    current_player_idx = random.randint(0, 1)
    
    print(f"\nНачинаем игру на поле {field_size}x{field_size}!")
    print(f"Первым ходит: {players[current_player_idx]}")
    
    while True:
        print_board(board)
        current_player = players[current_player_idx]
        
        if game_mode == 'robot' and current_player == 'O':
            print("\nХод бота...")
            time.sleep(1)
            row, col = bot_move(board, current_player)
        else:
            row, col = get_valid_move(board, current_player)
        
        board[row][col] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            result = f"Победил {current_player}!"
            print(result)
            
            if game_mode == 'robot':
                players_str = "Человек (X) vs Бот (O)"
            else:
                players_str = "Человек (X) vs Человек (O)"
            
            save_game_result(result, players_str, field_size)
            return current_player
        
        if check_draw(board):
            print_board(board)
            result = "Ничья!"
            print(result)
            
            if game_mode == 'robot':
                players_str = "Человек (X) vs Бот (O)"
            else:
                players_str = "Человек (X) vs Человек (O)"
            
            save_game_result(result, players_str, field_size)
            return 'draw'
        
        current_player_idx = (current_player_idx + 1) % 2

def main():
    init_stats()
    
    while True:
        print("\n" + "="*50)
        print("КРЕСТИКИ-НОЛИКИ")
        print("="*50)
        
        try:
            field_size = int(input("Введите размер игрового поля (например, 3): "))
            if field_size < 3:
                print("Минимальный размер поля - 3!")
                continue
                
            print("\nВыберите режим игры:")
            print("1. Два игрока")
            print("2. Против бота")
            mode_choice = input("Ваш выбор (1 или 2): ")
            
            if mode_choice == '1':
                game_mode = 'human'
            elif mode_choice == '2':
                game_mode = 'robot'
            else:
                print("Неверный выбор, играем с человеком")
                game_mode = 'human'
            
            play_game(field_size, game_mode)
            
            print("\n" + "="*30)
            restart = input("Хотите сыграть еще раз? (да/нет): ").lower()
            if restart != 'да':
                print("Спасибо за игру! Статистика сохранена в папке game_stats")
                break
                
        except ValueError:
            print("Ошибка! Введите число для размера поля.")
        except KeyboardInterrupt:
            print("\n\nИгра прервана.")
            break
        except Exception:
            print("Произошла ошибка!")

if __name__ == "__main__":
    main()