import csv

with open('your_file.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)

result = []
for i in range(0, len(rows), 4):
    row = rows[i]
    new_row = row[:1] + [''] * 3
    for j in range(4):
        if j < len(rows[i:i+4]) and rows[i+j][0] == 'Câu':
            new_row[1 + j] = rows[i+j][1:]
        else:
            new_row[1 + j] = row[1 + j]
    result.append(new_row)

with open('new_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
