
from BloomFilter import BloomFilter

def check_password_uniqueness(bloom, passwords):
    results = {}
    for password in passwords:
        if bloom.contains(password):
            results[password] = "вже використаний"
        else:
            results[password] = "унікальний"
    return results

def run_task1():
    bloom = BloomFilter(size=1000, num_hashes=3)

    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Перевірка нових паролів
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    
    expected_results = {
        "password123": "вже використаний",
        "newpassword": "унікальний",
        "admin123": "вже використаний",
        "guest": "унікальний",
    }

    results = check_password_uniqueness(bloom, new_passwords_to_check)

    for password, status in results.items():
        assert status == expected_results[password]
        print(f"Пароль '{password}' - {status}.")

    print('\nТести пройдено успішно!')

if __name__ == "__main__":
    run_task1()