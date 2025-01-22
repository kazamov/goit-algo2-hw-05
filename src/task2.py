import os.path as path
import json
import time
from HyperLogLog import HyperLogLog

def read_and_process_lines(file_path, callback):
    with open(file_path, 'rt') as file:
        for row in file:
            try:
                data = json.loads(row)
                callback(data['remote_addr'])
            except Exception as e:
                print(f"Unable to handle line: {row}")

def generate_set(file_path):
    ip_set = set()
    def add_to_set(ip):
        ip_set.add(ip)
    read_and_process_lines(file_path, add_to_set)
    return ip_set

def generate_hll(file_path):
    hll = HyperLogLog()
    def add_to_hll(ip):
        hll.add(ip)
    read_and_process_lines(file_path, add_to_hll)
    return hll

def run_task2():
    file_name = path.dirname(__file__) + '/lms-stage-access.log'

    start_exact = time.time()
    ip_set = generate_set(file_name)
    exact_count = '{0:.4f}'.format(len(ip_set))
    exact_time = time.time() - start_exact

    start_approx = time.time()
    hll = generate_hll(file_name)
    approx_count = '{0:.4f}'.format(hll.get_cardinality())
    approx_time = time.time() - start_approx

    print("Результати порівняння:")
    print("--------------------------------------------------------------------")
    print(f"{'Метод':<25}{'Унікальні елементи':<20}{'Час виконання (сек.)':<10}")
    print("--------------------------------------------------------------------")
    print(f"{'Точний підрахунок':<25}{exact_count:<20}{exact_time:<10.3f}")
    print(f"{'HyperLogLog':<25}{approx_count:<20}{approx_time:<10.3f}")

if __name__ == "__main__":
    run_task2()