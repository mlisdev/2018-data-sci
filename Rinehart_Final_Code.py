#Stephanie Rinehart 
#IST 652 
#Final Project: Best States for MLS Grads 

#import required modules 
import statistics as stats

#open CSV file and call "libinfo" 
libinfo = open('2016library.csv', 'r')


#set columns as variables for easy retrieval 
STATE_COLUMN = 0
UNDUPLICATED_POPULATION_COLUMN = 10
MLIS_LIBRARIANS_COLUMN = 14
TOTAL_LIBRARIANS_COLUMN = 15
TOTAL_STAFF_COLUMN = 17
SALARIES_COLUMN = 23

#ignore commas in data since population is set with comma separator 
def getFixedRow(row):
    inquotes = False
    retval = ""
    for char in row:
        if char == "\"":
            inquotes = not inquotes
        elif inquotes and char == ',':
            pass
        else:
            retval = retval + char
    return retval.split(',')

#create empty list to append later 
unduplicatePopulationList = []
#ignore first row 
isfirstline = True

# loop to ignore first row 
for row in libinfo:
    if isfirstline: 
        isfirstline = False
        continue 
# ignores commas in all data
    row = getFixedRow(row)
    unduplicatePopulationList.append(int(row[UNDUPLICATED_POPULATION_COLUMN]))
medianPop = stats.median(unduplicatePopulationList)

#create empty lists for append later 
libinfo.seek(0)
lowPopMlisLibrarians = []
lowPopTotalLibrarians = []
lowPopTotalStaff = []
lowPopTotalSalaries = []

highPopMlisLibrarians = []
highPopTotalLibrarians = []
highPopTotalStaff = []
highPopTotalSalaries = []

#create empty dicts to append 
stateToMlisDict = {}
bestStates = {}

#ignore first line (csv headers)
isfirstline = True
for row in libinfo:
    if isfirstline:
        isfirstline = False
        continue
    
    row = getFixedRow(row)
    #read pop as an int, not a string 
    unduplicatePopulation = int(row[UNDUPLICATED_POPULATION_COLUMN])
    #create float variables for data  
    numMlisLibs = float(row[MLIS_LIBRARIANS_COLUMN])
    numTotalLibs = float(row[TOTAL_LIBRARIANS_COLUMN])
    numTotalStaff = float(row[TOTAL_STAFF_COLUMN])
    totalSalaries = float(row[SALARIES_COLUMN])
    #check median population in "unduplicated population" column 
    if unduplicatePopulation <= medianPop and unduplicatePopulation >= 0: 
        lowPopMlisLibrarians.append(numMlisLibs)
        lowPopTotalLibrarians.append(numTotalLibs)
        #finds salaries that are = or greater than 0 to ignore entries that read negative (ex: -9)
        if (totalSalaries >= 0):
            lowPopTotalStaff.append(numTotalStaff)
            lowPopTotalSalaries.append(totalSalaries)
    #if undupe pop is greater than median, appends to high pop lists 
    else:
        highPopMlisLibrarians.append(numMlisLibs)
        highPopTotalLibrarians.append(numTotalLibs)
        #finds salaries that are = or greater than 0 to ignore entries that read negative (ex: -9)
        if (totalSalaries >= 0):
            highPopTotalStaff.append(numTotalStaff)
            highPopTotalSalaries.append(totalSalaries)
    #finds states with MLS staff and total librarians         
    state = row[STATE_COLUMN]
    if state not in stateToMlisDict:
        stateToMlisDict[state] = [0.0, 0.0]
    stateToMlisDict[state][0] += numMlisLibs
    stateToMlisDict[state][1] += numTotalLibs
#loop over all the states for dict created in 96-100  
for state in stateToMlisDict:
    try:
        #get data for current state 
        thisState = stateToMlisDict[state]
        #get % of librarians with MLS 
        thisStatePct = 100 * thisState[0] / thisState[1]
        #get state with worth % in dict 
        lowestPct = min(bestStates.keys()) if len(bestStates.keys()) > 0 else 0.0
        #if thisState has a better %, 
        if thisStatePct > lowestPct:
            #if already 5 states in dict, remove entry with lowest % 
            if (len(bestStates) == 5):
                bestStates.pop(lowestPct, None)
            #add current state to dict 
            bestStates[thisStatePct] = state
#skip states with no librarians to avoid division by 0 (ex: guam) 
    except:
        pass
#descriptive stats math        
smallAvgLibs = sum(lowPopTotalLibrarians) / len(lowPopTotalLibrarians)
smallAvgMlisLibs = sum(lowPopMlisLibrarians) / len(lowPopMlisLibrarians)
smallAvgSalary = sum(lowPopTotalSalaries) / sum(lowPopTotalStaff)

largeAvgLibs = sum(highPopTotalLibrarians) / len(highPopTotalLibrarians)
largeAvgMlisLibs = sum(highPopMlisLibrarians) / len(highPopMlisLibrarians)
largeAvgSalary = sum(highPopTotalSalaries) / sum(highPopTotalStaff)


#Begin same code for 2015 dataset 
#open CSV file and call "2015libinfo" 
libinfo15 = open('2015librarybackup.csv', 'r')


#set columns as variables for easy retrieval 
STATE_COLUMN15 = 0
UNDUPLICATED_POPULATION_COLUMN15 = 7
MLIS_LIBRARIANS_COLUMN15 = 11
TOTAL_LIBRARIANS_COLUMN15 = 12
TOTAL_STAFF_COLUMN15 = 14
SALARIES_COLUMN15 = 20

#ignore commas in data since population is set with comma separator 
def getFixedRow15(row):
    inquotes = False
    retval = ""
    for char in row:
        if char == "\"":
            inquotes = not inquotes
        elif inquotes and char == ',':
            pass
        else:
            retval = retval + char
    return retval.split(',')

#create empty list to append later 
unduplicatePopulationList15 = []
#ignore first row 
isfirstline = True

# loop to ignore first row 
for row in libinfo15:
    if isfirstline: 
        isfirstline = False
        continue 
# ignores commas in all data
    row = getFixedRow15(row)
    unduplicatePopulationList15.append(int(row[UNDUPLICATED_POPULATION_COLUMN15]))
medianPop15 = stats.median(unduplicatePopulationList15)

#create empty lists for append later 
libinfo15.seek(0)
lowPopMlisLibrarians15 = []
lowPopTotalLibrarians15 = []
lowPopTotalStaff15 = []
lowPopTotalSalaries15 = []

highPopMlisLibrarians15 = []
highPopTotalLibrarians15 = []
highPopTotalStaff15 = []
highPopTotalSalaries15 = []

#create empty dicts to append 
stateToMlisDict15 = {}
bestStates15 = {}

#ignore first line (csv headers)
isfirstline = True
for row in libinfo15:
    if isfirstline:
        isfirstline = False
        continue
    
    row = getFixedRow15(row)
    #read pop as an int, not a string 
    unduplicatePopulation15 = int(row[UNDUPLICATED_POPULATION_COLUMN15])
    #create float variables for data  
    numMlisLibs15 = float(row[MLIS_LIBRARIANS_COLUMN15])
    numTotalLibs15 = float(row[TOTAL_LIBRARIANS_COLUMN15])
    numTotalStaff15 = float(row[TOTAL_STAFF_COLUMN15])
    totalSalaries15 = float(row[SALARIES_COLUMN15])
    #check median population in "unduplicated population" column 
    if unduplicatePopulation15 <= medianPop and unduplicatePopulation15 >= 0:
        lowPopMlisLibrarians15.append(numMlisLibs15)
        lowPopTotalLibrarians15.append(numTotalLibs15)
        #finds salaries that are = or greater than 0 to ignore entries that read negative (ex: -9)
        if (totalSalaries15 >= 0):
            lowPopTotalStaff15.append(numTotalStaff15)
            lowPopTotalSalaries15.append(totalSalaries15)
    #if undupe pop is greater than median, appends to high pop lists 
    else:
        highPopMlisLibrarians15.append(numMlisLibs15)
        highPopTotalLibrarians15.append(numTotalLibs15)
        #finds salaries that are = or greater than 0 to ignore entries that read negative (ex: -9)
        if (totalSalaries15 >= 0):
            highPopTotalStaff15.append(numTotalStaff15)
            highPopTotalSalaries15.append(totalSalaries15)
    #finds states with MLS staff and total librarians         
    state = row[STATE_COLUMN15]
    if state not in stateToMlisDict15:
        stateToMlisDict15[state] = [0.0, 0.0]
    stateToMlisDict15[state][0] += numMlisLibs15
    stateToMlisDict15[state][1] += numTotalLibs15
#loop over all the states for dict created in 96-100  
for state in stateToMlisDict15:
    try:
        #get data for current state 
        thisState15 = stateToMlisDict15[state]
        #get % of librarians with MLS 
        thisStatePct15= 100 * thisState15[0] / thisState15[1]
        #get state with worth % in dict 
        lowestPct15 = min(bestStates15.keys()) if len(bestStates15.keys()) > 0 else 0.0
        #if thisState has a better %, 
        if thisStatePct15 > lowestPct15:
            #if already 5 states in dict, remove entry with lowest % 
            if (len(bestStates15) == 5):
                bestStates15.pop(lowestPct15, None)
            #add current state to dict 
            bestStates15[thisStatePct15] = state
#skip states with no librarians to avoid division by 0 (ex: guam) 
    except:
        pass
#descriptive stats math        
smallAvgLibs15 = sum(lowPopTotalLibrarians15) / len(lowPopTotalLibrarians15)
smallAvgMlisLibs15 = sum(lowPopMlisLibrarians15) / len(lowPopMlisLibrarians15)
smallAvgSalary15 = sum(lowPopTotalSalaries15) / sum(lowPopTotalStaff15)

largeAvgLibs15 = sum(highPopTotalLibrarians15) / len(highPopTotalLibrarians15)
largeAvgMlisLibs15 = sum(highPopMlisLibrarians15) / len(highPopMlisLibrarians15)
largeAvgSalary15 = sum(highPopTotalSalaries15) / sum(highPopTotalStaff15)


#print output for 2015 and 2016 
print("In 2015, median population served by libraries in this data: %d" % medianPop15)
print("In 2015, libraries with below median populations:")
print("\tAverage number of librarians: %.2f" % (smallAvgLibs15))
print("\tAverage number of librarians with MLIS: %.2f" % smallAvgMlisLibs15)
print("\tPercentage of MLIS librarians of total: %.2f" % (100 * smallAvgMlisLibs15 / smallAvgLibs15))
print("\tAverage salary, all staff (where data available): %.2f" % smallAvgSalary15)
print("")

print("In 2016, median population served by libraries in this data: %d" % medianPop)
print("In 2016. Libraries with below median populations:")
print("\tAverage number of librarians: %.2f" % (smallAvgLibs))
print("\tAverage number of librarians with MLIS: %.2f" % smallAvgMlisLibs)
print("\tPercentage of MLIS librarians of total: %.2f" % (100 * smallAvgMlisLibs / smallAvgLibs))
print("\tAverage salary, all staff (where data available): %.2f" % smallAvgSalary)
print("")

print("In 2015, libraries with above median population:")
print("\tAverage number of librarians: %.2f" % largeAvgLibs15)
print("\tAverage number of librarians with MLIS: %.2f" % largeAvgMlisLibs15)
print("\tPercentage of MLIS librarians of total: %.2f" % (100 * largeAvgMlisLibs15 / largeAvgLibs15))
print("\tAverage salary, all staff (where data available): %.2f" % largeAvgSalary15)
print("")

print("In 2016, Libraries with above median population:")
print("\tAverage number of librarians: %.2f" % largeAvgLibs)
print("\tAverage number of librarians with MLIS: %.2f" % largeAvgMlisLibs)
print("\tPercentage of MLIS librarians of total: %.2f" % (100 * largeAvgMlisLibs / largeAvgLibs))
print("\tAverage salary, all staff (where data available): %.2f" % largeAvgSalary)
print("")

print("In 2015, the five states with the highest rates of MLIS librarians:")
for pct in reversed(sorted(bestStates15.keys())):
    print("In %s, %.2f percent of library staff has an MLIS." % (bestStates15[pct], pct))
print("")
print("In 2016, The five states with the highest rates of MLIS librarians:")
for pct in reversed(sorted(bestStates.keys())):
    print("In %s, %.2f percent of library staff has an MLIS." % (bestStates[pct], pct))
print("")




