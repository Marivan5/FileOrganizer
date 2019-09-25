import shutil, os, time, stat, datetime

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    if f.endswith('.py'): # ignore python file
        continue
    fStat = os.stat(f)
    fCreated = fStat[stat.ST_CTIME]
    fModified = fStat[stat.ST_MTIME]
    fAccess = fStat[stat.ST_ATIME]
    oldestDate = min(fCreated, fModified, fAccess)
    fYear = str(datetime.date.fromtimestamp(oldestDate).year)
    fMonth = datetime.date.fromtimestamp(oldestDate).strftime("%B")
    dirName = str(fYear + '\\' + str(fMonth))
    if not os.path.exists(fYear):
        os.mkdir(fYear)
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    print('Moving file \'' + str(f) + '\'')
    shutil.move(f, dirName)