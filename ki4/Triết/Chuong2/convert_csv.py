import pandas as pd
import csv
import openpyxl
# # Load the Excel file into a Pandas DataFrame
# df = pd.read_excel('book_example.xlsx')

# # Save the DataFrame to a CSV file
# df.to_csv('output_file.csv', index=False)

with open("finalc2.csv", 'w',encoding='utf-8-sig') as csvfinal:
    data_final= csv.writer(csvfinal)
    with open('chuong2csv.csv', 'r',encoding='utf-8-sig') as csvfile:
        datareader = csv.reader(csvfile)
        for i,row in enumerate(datareader):
            if row[0].startswith("Câu"):
                lst = []
                lst.append(row[0])
                for j in range(4):
                    try:
                        st = next(datareader)[0]
                        print(st)
                        lst.append(st)
                    except StopIteration:
                        break
                data_final.writerow(lst)
        # print(*lst)
        # print(*row)
df = pd.read_csv('finalc2.csv')

# Write the DataFrame to an Excel file
df.to_excel('finalc2.xlsx', index=False)