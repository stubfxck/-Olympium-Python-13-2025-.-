import re

with open("nums.txt", "w", encoding="utf-8-sig") as nums:
    print("У тебя 10 монет, 15 — в банке, и 5.5 на карте.", file=nums)

with open("nums.txt", "r", encoding="utf-8-sig") as nums:
    nums = nums.read()
    pattern = r"\d+\.\d+|\d+"
    final = re.findall(pattern, nums)
    summary = 0
    for num in final:
        summary += float(num)
    print(f"Сумма: {summary}")

# Output: Сумма: 30.5