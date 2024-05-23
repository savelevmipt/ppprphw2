import requests
import time

def write_stat():
    try:
        response = requests.get('http://web-service/statistics')

        if response.status_code == 200:
            time_requests_count = response.json()['time_requests_count']

            with open('statistics.txt', 'a') as f:
                f.write(f'{time_requests_count}\n')

        else:
            print(f'Ошибка при запросе: {response.status_code}')
    except Exception as e:
        print(f'Ошибка: {e}')


while True:
    write_stat()
    time.sleep(5)