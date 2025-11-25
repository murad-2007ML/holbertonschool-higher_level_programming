#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
# Mənfi ədədlər üçün son rəqəmin işarəsini düzəldirik
# Əgər ədəd mənfidirsə VƏ qalıq sıfır deyilsə, 10 çıxarırıq.
if last_digit > 0 and number < 0:
    last_digit -= 10
if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"
else:
    # Bu şərt (6-dan kiçik və 0-a bərabər olmayan) bütün digər ehtimalları əhatə edir:
    # 1-dən 5-ə qədər müsbət rəqəmlər və -1-dən -9-a qədər mənfi rəqəmlər.
    result = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {result}")
~                                                                                                                                                                                                                                        
~                                                        
