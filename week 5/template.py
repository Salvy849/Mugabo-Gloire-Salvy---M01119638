"""
RECORD CHECK  -  my version
===========================

Name  :Mugabo Gloire Salvy
Lane  :  Cyber      (delete two)
Date  :22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    def __init__(self,label,value,limit):
        self.label = label
        self.value = value
        self.limit = limit
    def status(self):
        pct = (self.value/self.limit)*100
        if pct >=100:
            return"OVER LIMIT" 
        elif pct>= 90:
            return"WARNING"
        return "OK"
def load_records(path):
    result = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label,value,limit=line.split(",")
            result.append(Record(label,float(value),float(limit)))
    return result
records = load_records("record.txt")
over_limit_count = 0
for record in records:
        result = record.status()
        if result == "OVER LIMIT":
            over_limit_count+=1
        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {record.label}")
        print("=" * 34)
        print(f"used:{record.value}")
        print(f"total:{record.limit}")
        print(f"status:{result}")
        print("=" * 34)
print()
prin(t(f"{over_limit_count} of {len(records)} records are OVER LIMIT"))
        


    



# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

  # replace with your code


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
