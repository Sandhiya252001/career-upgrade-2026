info_count=0
error_count=0
warn_count=0
with open('python_practice/logDemo.txt','r') as f:
    for line in f:
        if "INFO" in line:
            info_count+=1
        elif "ERROR" in line:
            error_count+=1
        elif "WARNING" in line:
            warn_count+=1
print(f"INFO : {info_count}\nERROR: {error_count}\nWARNING: {warn_count}")


# if __name__ == '__main__':
#     records = []

#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])

#     # Get all scores
#     scores = sorted(set([score for name, score in records]))

#     # Second lowest score
#     second_lowest = scores[1]

#     # Get names with second lowest score
#     names = [name for name, score in records if score == second_lowest]

#     # Sort names alphabetically
#     names.sort()

#     for name in names:
#         print(name)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    value=sum(student_marks[query_name])/len(student_marks[query_name])
    print(f"{value:.2f}")
   

     

            
            
    
        
        
       
        
    