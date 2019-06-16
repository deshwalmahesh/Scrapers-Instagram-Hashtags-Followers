# import xlsxwriter module 
import xlsxwriter


with open('tags.txt') as f:
    col1=f.read().splitlines()

with open('posts.txt') as f:
    col2=f.read().splitlines()

    

workbook = xlsxwriter.Workbook('output.xlsx') 

# By default worksheet names in the spreadsheet will be 
# Sheet1, Sheet2 etc., but we can also specify a name. 
worksheet = workbook.add_worksheet("My sheet") 

# Some data we want to write to the worksheet. 
scores=[]
for i in range(len(col1)):
    lis=[]
    lis.append(col1[i])
    lis.append(col2[i])
    scores.append(lis)
    

# Start from the first cell. Rows and 
# columns are zero indexed. 
row = 0
col = 0

# Iterate over the data and write it out row by row. 
for name, score in (scores): 
	worksheet.write(row, col, name) 
	worksheet.write(row, col + 1, score) 
	row += 1

workbook.close() 
