from datetime import datetime
ERR=0
INF=0
WARN=0
with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\python_concepts\Automation\sample.log") as f:
    file=f.readlines()
    for i in file:
        
        if "ERROR" in i:
            ERR += 1
        if "INFO" in i:
            INF += 1
        if "WARNING" in i:
            WARN += 1
TotalLogs = len(file)
if TotalLogs > 0:
    error_rate = ( ERR/ TotalLogs) * 100
else:
    error_rate = 0
timestamp = datetime.now()

print("Monitoring Report")
print("-----------------")
print("Timestamp:", timestamp)
print("Total Logs:", TotalLogs)
print("Errors:", ERR)
print("Error Rate:", round(error_rate, 2), "%")

    