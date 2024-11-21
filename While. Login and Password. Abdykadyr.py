import time
login = "112233"
password = "445566"
max_attempts = 3
attempts = 0
while True:
    written_login = input("Enter login: ")
    written_password = input("Enter password: ")
    if written_login == login and written_password == password:
        print("Welcome!")
        break
    else:
        print("Not correct login or password. Please, try again.")
        attempts += 1
    if attempts == max_attempts:
        print("Attempts are over. Please, wait 5 seconds")
        time.sleep(5)
        attempts = 0
        break
