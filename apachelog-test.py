import apachelog

logfilename = 'access.log'
log = apachelog.aggregatelog(logfilename)
sorted_method = dict(sorted(log['Method'].items(), key=lambda item:item[1],reverse=True))
for row in sorted_method.keys():
    print("Method   " + str(row) + " :     " + str(sorted_method[row]))
    
maxip = ""
maxipcount = 0
uniqueip = 0
for row in log['IP'].keys():
    if(log['IP'][row]>maxipcount):
        maxip = row
        maxipcount = log['IP'][row]
    if(log['IP'][row]>=1):
        uniqueip = uniqueip+1
    
print("Most popular IP Address is " + str(maxip) + " with " + str(maxipcount) + " occurrences")
print("Number of Unique IP Addresses: " + str(uniqueip))