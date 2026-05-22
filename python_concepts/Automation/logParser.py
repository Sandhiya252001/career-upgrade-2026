ERR = 0
INF = 0
WARN = 0

with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\python_concepts\Automation\sample.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            ERR += 1
        if "INFO" in line:
            INF += 1
        if "WARNING" in line:
            WARN += 1

max_count = max(ERR, INF, WARN)

if ERR == max_count:
    print("ERROR is most frequent")

if INF == max_count:
    print("INFO is most frequent")

if WARN == max_count:
    print("WARNING is most frequent")

print(f"ERROR count: {ERR}\nINFO COUNT: {INF}\nWARN Count: {WARN}")