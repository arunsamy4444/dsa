scores = {}
name = ['Arun','Samy' , 'Zoro']
grades = [90, 85, 92]

for i in range(len(name)):
    scores[name[i]] = grades[i]
for name, grade in scores.items():
    print(name, grade)
k = list(scores.keys())
v = list(scores.values())

print(scores)
print(k[2])     # 'Zoro'
print(v[2])   # 92

