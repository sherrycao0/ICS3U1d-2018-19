# 2_1_if_statements.py




def squirrel_play(temp, is_summer):
    if is_summer:
        if temp >= 60 and temp <=100:
            return True
    elif temp >= 60 and temp <=90:
        return True
    else:
        return False

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(70, True))





