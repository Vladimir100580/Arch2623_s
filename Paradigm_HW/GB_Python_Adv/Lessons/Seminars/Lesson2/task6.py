# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

RICH_LIMIT = 5000000
MAX_SUMM = 600
MIN_SUMM = 30
PERCENT_WITHDRAWAL = 1.5
PERCENT_ADD = 3
AMOUNT_REPLENISHED_SMALL = 50
PERCENTAGE_WEALTH_TAX = 10
OPERATIONS_COUNT = 3
count = 0
balance = 0


while True:
    print(f"Сумма на счету равна: {balance}")
    n = int(input("Введите (1-3): 1-пополнить, 2-снять, 3-выйти: "))
    if balance > RICH_LIMIT:
        balance *= 1 - PERCENTAGE_WEALTH_TAX / 100
    if n == 1:
        while True:
            s = int(input("Введите сумму пополнения: "))
            if s % AMOUNT_REPLENISHED_SMALL == 0:
                balance += s
                break
            else:
                print(f"!! Кратна {AMOUNT_REPLENISHED_SMALL}")
    if n == 2:
        while True:
            s = int(input("Сколько хотите снять: "))
            pr = max(min(s * PERCENT_WITHDRAWAL / 100, MAX_SUMM), MIN_SUMM)
            print(f"Сумма + процент: {s + pr}")
            if balance >= s + pr:
                balance -= s + pr
                break
    if n == 3:
        break
    if n == 1 or n == 2:
        count += 1
        if count % OPERATIONS_COUNT == 0:
            balance *= 1 + PERCENT_ADD / 100


