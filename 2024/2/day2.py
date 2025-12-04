reports = []

with open("day2.txt", "r") as file:
    for line in file:
        row = [int(c) for c in line.strip().split()]
        reports.append(row)

count = 0

def is_safe(report: list) -> bool:
    ascending = True if report[0] < report[len(report) - 1] else False
    for i in range(len(report) - 1):
        if not ascending and not (0 < (report[i] - report[i + 1]) < 4):
            break;
        if ascending and not (4 > (report[i + 1] - report[i]) > 0):
            break;
        
        if i == len(report) - 2:
            return True
    
    print(report)
    return False

for report in reports:
    safe = is_safe(report)
    
    if safe == True:
        count += 1
    else:
        for i in range(len(report)):
            # print(report)
            new_report = report[0:i] + report[i+1:]
            # print("new", new_report)
            if is_safe(new_report):
                count += 1
                break;
    
print(count)