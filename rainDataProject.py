import matplotlib.pyplot as plt

def fileReader():
    global fileobject
    filename = input ("Enter the name of the file -->")
    try:
        fileobject = open (filename, 'r')
    except Exception as e:
        print (e)

def rainDataList ():

    global dataSet 
    dataSet = []

    for line in fileobject:
        rawList = line.split(',')
        dataSet.append([(rawList[0]), float(rawList[1])])

def November():
    global NovList
    NovList = [item for item in dataSet if 'Nov' in item[0]]

def December():
    global DecList
    DecList = [item for item in dataSet if 'Dec' in item[0]]

def January():
    global JanList
    JanList = [item for item in dataSet if 'Jan' in item[0]]

def Febuary():
    global FebList
    FebList = [item for item in dataSet if 'Feb' in item[0]]

def March():
    global MarList
    MarList = [item for item in dataSet if 'Mar' in item[0]]

def April():
    global AprList
    AprList = [item for item in dataSet if 'Apr' in item[0]]

def May():
    global MayList
    MayList = [item for item in dataSet if 'May' in item[0]]

def June():
    global JunList
    JunList = [item for item in dataSet if 'Jun' in item[0]]

def July():
    global JulList
    JulList = [item for item in dataSet if 'Jul' in item[0]]

def August():
    global AugList
    AugList = [item for item in dataSet if 'Aug' in item[0]]

def September():
    global SepList
    SepList = [item for item in dataSet if 'Sep' in item[0]]

def October():
    global OctList
    OctList = [item for item in dataSet if 'Oct' in item[0]]

def monthAverage(month):
    sum = 0
    for i in month:
        sum += (i[1])
    monthAverage = sum/len(month)
    monthAverageFinal = ("{:.2f}".format(monthAverage))
    return(float(monthAverageFinal))

def main():
    fileReader()
    rainDataList()
    January()
    Febuary()
    March()
    April()
    May()
    June()
    July()
    August()
    September()
    October()
    November()
    December()

    months = ['Jan', 'Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug','Sep','Oct','Nov','Dec']
    avgAnnualList = [(monthAverage(JanList)), (monthAverage(FebList)), (monthAverage(MarList)), 
    (monthAverage(AprList)), (monthAverage(MayList)), (monthAverage(JunList)), (monthAverage(JulList)),
    (monthAverage(AugList)), (monthAverage(SepList)), (monthAverage(OctList)), (monthAverage(NovList)),
    (monthAverage(DecList))]

    plt.title('Average Rainfall by Month')
    plt.xlabel('Months of the year')
    plt.ylabel('Average')
    plt.bar(months, avgAnnualList)
    plt.show()

main()

    
