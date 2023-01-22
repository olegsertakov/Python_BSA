'''
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
'''


import json

with open('text_7.json', 'w', encoding='utf-8') as test_fw:
    with open('text_7.txt', 'r', encoding='utf-8') as test_f:
        profit = {line.split()[0]: float(line.split()[2]) - float(line.split()[3]) for line in test_f}
        average_profit = {'Average_profit': round(sum([float(i) for i in profit.values() if float(i) > 0]) /
                          len([float(i) for i in profit.values() if float(i) > 0]))}
        result = [profit, average_profit]

    json.dump(result, test_fw)
