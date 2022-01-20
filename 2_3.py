message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for ind, val in enumerate(message):
    if val.isdigit():
        message[ind] = f'"{int(val):02}"'
    elif val[1:].isdigit():
        message[ind] = f'"{val[0]}{int(val[1:]):02}"'

print(" ".join(message))
