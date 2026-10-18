"""
RECORD CHECK  -  my version
===========================

Name  :Mugabo Gloire Salvy
Lane  :   Cyber       (delete two)
Date  :18/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent,warning_at=90):
    if percent>=100:
        return"OVER LIMIT"
    elif percent>=warning_at:
        return "WARNING"
    else:
        return"OK"
def check_record(value,limit):
    
    difference =limit - value
    percent=(value/limit)*100
    status = status_of(percent)
    return difference,percent,status
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
def show_message (text):
    """Print a one line message(missing file)"""
    print(text)

def load_records(path):
    records = []
    with open(path) as f:
        for line in f :
            line = line.strip()
            if not line:
                continue
            label,value,limit =line.split(",")
            records.append({"label":label,"value":float(value),"limit":float(limit)})
        return records
def save_results(path,results):
    with open(path,"w") as f:
        for label,status in results:
            f.write(f"{label},{status}\n")
try:
    records = load_records("records.txt")
except FileNotFoundError:
    show_message("records.txt not found - starting with no records")
    records=[]
results = []
over_count = 0
for r in records:
    difference , percent,status = check_record(r["value"],r["limit"])
    print_report(r["label"],r["value"],r["limit"],difference,percent,status)
    results.append((r['label'],status))
    if status == "OVER LIMIT":
                over_count +=1
save_results("results.txt",results)
show_message(f"Records over limit:{over_count}")            

