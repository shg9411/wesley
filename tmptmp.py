import sys

N = int(sys.stdin.readline())
data = [ sys.stdin.readline().strip() for _ in range(N)]
result = [[] for _ in range(51)]
for i in data:
    result[len(i)].append(i)
for index1 in result:
    # 길이의 비교
    if len(index1) == 1:
        print(*index1)
    elif len(index1) > 1:
        compare = [0 for _ in range(len(index1))]
        # 숫자 더하기 비교
        for i in range(len(index1)):
            count = 0
            for j in range(len(index1[i])):
                if 48 <= ord(index1[i][j]) <= 57:
                    count += ord(index1[i][j])%48
            compare[i] = [i,count]
        compare.sort(key = lambda x:x[1])
        for i in range(len(compare)):
            compare[i] = result[result.index(index1)][compare[i][0]]
        
        # 숫자로 비교가 안될 시 정렬
        if compare == index1:
            index1.sort()
            print(*index1,sep='\n')
        else:
            print(*compare,sep='\n')