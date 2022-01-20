message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for ind, val in enumerate(message):
    sigin_1 = '"'
    sigin_2 = ''
    if val.isdigit():
        message[ind] = f'{sigin_1}{int(val):02}{sigin_1}'
    if val.count('+'):
        val = val.replace('+', '')
        sigin_2 = '+'
        message[ind] = f'{sigin_1}{sigin_2}{int(val):02}{sigin_1}'
    elif val.count('-'):
        val = val.replace('-', '')
        sigin_2 = '-'
        message[ind] = f'{sigin_1}{sigin_2}{int(val):02}{sigin_1}'
print(" ".join(message))
