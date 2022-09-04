#특정 번호의 학생은 제외하기

scores = [90,85,77,65,97]
cheating_student_list = {2,4}

for i in range(len(scores)):
    if i+1 in cheating_student_list:
        continue
    if scores[i] > 80:
        print(i+1,'번 학생은 합격입니다.')


#구구단 예제

for i in range(2,10):
    for j in range(1,10):
        print(i,' X ', j,' = ',i*j)
    print()

