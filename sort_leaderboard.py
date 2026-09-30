LeaderName = ["John", "Sarah", "Mike", "Emma"]
LeaderPoints = [50, 80, 60, 90]

for i in range(len(LeaderPoints)):
    for j in range(len(LeaderPoints) - 1 - i):
        if LeaderPoints[j] < LeaderPoints[j + 1]:
            LeaderPoints[j], LeaderPoints[j + 1] = LeaderPoints[j + 1], LeaderPoints[j]
            LeaderName[j], LeaderName[j + 1] = LeaderName[j + 1], LeaderName[j]

print(LeaderName)
print(LeaderPoints)