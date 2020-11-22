user_seconds = int(input('Введите количество секунд: '))
hour = user_seconds // 3600
seconds = user_seconds % 60
minute = int(user_seconds - (hour * 3600) - seconds) // 60
print(f'Время {hour}:{minute}:{seconds}')