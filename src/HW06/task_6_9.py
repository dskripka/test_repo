# Создать список поездов. Структура словаря: номер поезда,
#пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.[02-7.3-ML02]
#Примечание: данное задание подразумевает самостоятельное изучение принципов работы со временем в Python(библиотека datetime)

from datetime import datetime, date, time, timedelta

spisok = [
{
        'number': '1',
        'from': 'Minsk',
        'to': 'Vilnus',
        'departure': datetime(2019, 4, 2, 8, 30),
        'arrival': datetime(2019, 4, 2, 11, 10),
},
{
        'number': '2',
        'from': 'Minsk',
        'to': 'Moscow',
        'departure': datetime(2019, 4, 2, 23, 55),
        'arrival': datetime(2019, 4, 3, 7, 45),
},
{
        'number': '3',
        'from': 'Minsk',
        'to': 'Brest',
        'departure': datetime(2019, 4, 3, 6, 30),
        'arrival': datetime(2019, 4, 3, 10, 5),
  },
{
        'number': '4',
        'from': 'Minsk',
        'to': 'Grodno',
        'departure': datetime(2019, 4, 3, 6, 30),
        'arrival': datetime(2019, 4, 3, 10, 20),
},
]

trains = []
compare_time = (timedelta(hours=7, minutes=20))
for time in spisok:
    travel_time = time['arrival'] - time['departure']
    if travel_time > compare_time:
        print(time['number'])
        print(time['from'])
        print(time['to'])
        print(time['departure'])
        print(time['arrival'])
        print(travel_time)

