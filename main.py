from src.masks import get_mask_account, get_mask_card_number

user_card_number = input("Введите номер карты : ")
print(get_mask_card_number(user_card_number))


user_account_number = input("Введите номер счёта : ")
print(get_mask_account(user_account_number))
