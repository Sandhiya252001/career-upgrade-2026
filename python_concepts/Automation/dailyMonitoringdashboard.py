Err=0
Info=0
Warn=0
with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\python_concepts\Automation\sample.log") as f:
    line=f.readlines()
    for i in line:
        if "ERROR" in i:
            Err+=1
        if "WARNING" in i:
            Warn+=1
        if "INFO" in i:
            Info+=1
Total=len(line)
ErrPer=(Err/Total)*100
if ErrPer<60:
    SystemHealth="Healthy"
else:
    SystemHealth="Warning"
report = (
    f"Total Logs: {Total}\n"
    f"INFO Count: {Info}\n"
    f"ERROR Count: {Err}\n"
    f"WARNING Count: {Warn}\n"
    f"Error Rate: {ErrPer:.2f}%\n"
    f"Status: {SystemHealth}"
)

print(report)

with open("dashboard.txt", "a") as f:
    f.write(report)



