# Array DataStructure
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

# Creating a list to store these monthly expenses
arr = [2200,2350,2600,2130,2190]

#In Feb, how many dollars you spent extra compare to January?
extra = arr[1]-arr[0]
print "how many dollars you spent extra compare to January?",extra

#Find out your total expense in first quarter (first three months) of the year.
expenceFirstQuater = sum(arr[:3])
print "Find out your total expense in first quarter (first three months) " \
      "of the year: ",expenceFirstQuater

#Find out if you spent exactly 2000 dollars in any month
print "did i spent exctly 2000 :", 2000 in arr

# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
arr.append(1980)
print "June month just finished and your expense is 1980 dollar",arr

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
aprilMonthUpdate = arr[-2]-200
print "Latest Expense update: ",aprilMonthUpdate

#Size Insert, Remove, Append, Splice, Sort

programs = ["python", 'C', "Java", "C++", "HTML", "C#"]

#Length of the list
print "Length of List : ",len(programs)

# Add "CSS" at the end of the list
programs.append("CSS")
print 'Add "CSS" at the end of the list',programs

#Remove CSS from end and add it at index 3
programs.remove("CSS")
programs.insert(3,"CSS")
print "Remove CSS from end and add it at index 3",programs

#Remove "C" and "Java" and add "SQL"
print programs[1:3]
programs[1:3]= "C"
print 'Remove "C" and "Java" and add "C"',programs

# Sort the list in alphabetical order
print "Sorted Programs : ",programs.sort()