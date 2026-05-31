err = 0
inf = 0
warn = 0

with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\python_concepts\Automation\sample.log") as f:
    lines = f.readlines()

for line in lines:
    if "ERROR" in line:
        err += 1
    if "WARNING" in line:
        warn += 1
    if "INFO" in line:
        inf += 1

count = len(lines)

if count > 0:
    error_rate = (err / count) * 100
else:
    error_rate = 0

report = {
    "Total Logs": count,
    "Errors": err,
    "Warnings": warn,
    "Info": inf,
    "Error Rate (%)": round(error_rate, 2)
}

print("Monitoring Report")
print("-----------------")

for key, value in report.items():
    print(f"{key}: {value}")