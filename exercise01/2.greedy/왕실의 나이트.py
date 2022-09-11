input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])-ord('a'))+1 #ord: 아스키코드 출력

steps = ((-1,-2),(-1,2),(1,-2),(1,2),(2,1),(2,-1),(-2,1),(-2,-1))
cnt = 0

for step in steps:
    next_row = row + step[1]
    next_col = col + step[0]

    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        #print(next_row, next_col)
        cnt+=1

print(cnt)


