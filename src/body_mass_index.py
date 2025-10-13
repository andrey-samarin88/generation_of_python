weight, height = float(input()), float(input())

index = weight / height ** 2

if index < 18.5:
    print('Недостаточная масса')
elif 18.5 <= index <= 25.0:
    print('Оптимальная масса')
elif index > 25.0:
    print('Избыточная масса')