import csv

month_counter = 0
profit=[]
month=[]
change_up = 0
change_down = 0

gain_current = 0
gain_prior = 0
gainsum = 0
max = 0
min = 0
x = 0

#Read in the budget CSV File
with open('budget_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None) # This line skips reading the Header Row
    for row in readCSV:
        profit.append(row[1])
        month.append(row[0])
        month_counter = month_counter + 1

#Scan for largest gain and loss month-on-month

for i in range (1, len(profit)):
 
    # Look for greatest delta postive and negative month-on-month profit changes
    if int(profit[i]) - int(profit[i-1]) > change_up:
        change_up = (int(profit[i])-int(profit[i-1]))
        change_up_month = month[i]
    elif int(profit [i]) - int(profit[i-1]) < change_down:
        change_down = (int(profit[i])-int(profit[i-1]))
        change_down_month = month[i]

x = len(profit)

for i in range (x):
    gainsum = gainsum + int(profit[i])
    if int(profit[i]) > max:
        max = int(profit[i])
    elif int(profit[i]) < min:
        min = int(profit[i])
average  = gainsum / x

print ("Number of months tracked are: ", month_counter)
print ("Sum of profits are: ", gainsum)
print ("Average of profits are: ", average )
print ("Largest monthly GAIN in profits are: ", change_up)
print ("Largest monthly GAIN month was: ", change_up_month)
print ("Largest monthly LOSS in profits are: ", change_down)
print ("Largest monthly LOSS month was: ", change_down_month)