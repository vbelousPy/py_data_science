

try:
    2/0
except (ValueError, KeyError, ZeroDivisionError) as e:
    print("error")
