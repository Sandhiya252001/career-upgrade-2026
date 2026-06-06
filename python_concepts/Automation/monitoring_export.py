Err=0
warn=0
with open(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\python_concepts\Automation\sample.log") as f:
    line=f.readlines()
    for i in line:
        if "ERROR" in i:
            Err+=1
        if "WARNING" in i:
            warn+=1
Total=len(line)
if Total > 0:
    error_rate = ( Err/ Total) * 100
else:
    error_rate = 0
print(f"Monitoring Report",
          "\n-----------------",
          f"\nTotal Logs:{Total}",
          f"\nErrors: {Err}",
          f"\nWarnings: {warn}",
          f"\nError Rate: {error_rate} ")

