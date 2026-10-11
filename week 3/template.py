"""
RECORD CHECK  -  my version
===========================

Name  :Mugabo Gloire Salvy
Lane  :  Cyber       (delete two)
Date  :9/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent,warning_at=90):
    if percent>=100:
        return"Over Limit"
    elif percent>=warning_at:
        return "Warning"
    else:
        return"ok"

def check(value,limit):
    difference =limit - value
    percent=(value/limit)*100
    return difference,percent

def print_report(label,value,limit,difference,percent,status):
    print()
    print("="*34)
    print(f"RECORD CHECK - {label}")
    print("="*34)
    print(f"Used :{value:>10.2f}")
    print(f"total :{limit:>10.2f}")
    print(f"Free :{difference:>10.2f}")
    print(f"Percent :{percent:>10.2f}%")
    print(f"Status :{status:>10}")
    print("="*34)





over_count = 0

while True:

    label = input("Hostname(or'quit'to stop):")
    if label.lower() =="quit":
        break     
    value = float(input("GB used:"))   
    limit = float(input("GB total:"))    


    difference,percent  = check(value,limit)  
    status = status_of(percent)
    if status=="OVER LIMIT":
        over_count+=1      



    print_report(label,value,limit,difference,percent,status)
print("Records Over Limit:",over_count)

