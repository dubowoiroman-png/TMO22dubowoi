#5 Вариант

def bill_per_person(bill, people):
    if people == 0:
        return "На ноль делить нельзя"
    return bill / people
assert bill_per_person(1500, 5) == 300.0
assert bill_per_person(150, 0) == "На ноль делить нельзя"
assert bill_per_person(1200, 20) == 60.0

#-----------------------------------------------------#

words = ["кот", "собака", "черепаха"]
result = sorted(words, key=lambda word: len(word))
print(result)
