"""
RECORD CHECK  -  my version
===========================

Name  :  Mugabo Gloire Salvy
Lane  :  IT
Date  :  11/11/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Clean one messy line and return it as a dict."""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)

    record = {"hostname": hostname_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())
    return record


def status_of(used, total):
    """Return OVER LIMIT, WARNING or OK for one record."""
    percent = used / total * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
messy_lines = []
with open("messy_lines.txt") as file:
    for line in file:
        messy_lines.append(line)


# =============================================================== PROCESS + OUTPUT
flagged = 0
for raw_record in messy_lines:
    record = parse_line(raw_record)
    status = status_of(record["used"], record["total"])
    print(record, status)
    if status != "OK":
        flagged += 1

print(f"{len(messy_lines)} records, {flagged} flagged")


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records
#    [x] Run it with a value that will not convert to a number - write the
#        error down
#    [x] Check every function does one job, with a docstring
