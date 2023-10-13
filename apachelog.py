import re


def aggregatelog(filename):

    counter = {
        'IP' : {},
        'Method' : {}
    }

    with open(filename) as fh:
        fstring = fh.readlines()

    for row in fstring:
        pattern = re.match(r'((?P<IP>^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S*\s+\S*\s+\[.*\]\s"(?P<Method>[A-Z]*))',row)
        ipaddress = pattern.group('IP')
        ipmethod = pattern.group('Method')
        
        exist = ipaddress in counter['IP'].keys()
        if(exist==True):
            counter['IP'][ipaddress] = counter['IP'][ipaddress] + 1
        else:
            counter['IP'][ipaddress] = 1
            
        exist2 = ipmethod in counter['Method'].keys()
        if(exist2==True):
            counter['Method'][ipmethod] = counter['Method'][ipmethod] + 1
        else:
            counter['Method'][ipmethod] = 1
        

    


        

            
    return counter