date = input()

reversed_date = date.split('/')
reversed_date.reverse()
reversed_date = '/'.join(reversed_date)

print(reversed_date)
