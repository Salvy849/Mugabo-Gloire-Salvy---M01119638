"""
RECORD CHECK  -  srv-01
===========================

Name  :Mugabo Gloire Salvy 
Lane  :   Cyber       (delete two)
Date  :3/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
overlimit_count = 0
while True:
    label = input("Enter the label (or type 'quit' to exit): ")      # replace with an input() call
    if label == "quit":
        break
        # replace with an input() call, converted with float()
      # replace with an input() call
    value = float(input("Enter the value: "))     # replace with an input() call, converted with float()
    limit = float(input("Enter the limit: "))     # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

    difference = limit - value  # replace with your calculation
    percent =value*100/limit
    if percent >= 100:
        status = "OVER LIMIT"
        overlimit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

  # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print(f"Value is : {value:>10.2f}")
    print(f"Limit is : {limit:>10.2f}")
    print(f"Difference is : {difference:>10.2f}")
    print(f"Percent is : {percent:>10.2f}%")
    print(f"Status is : {status:>13}")
    print("=" * 34)

# your report lines go here
print("Total records over limit:", overlimit_count)
print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
