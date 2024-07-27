# 입력받기
numbers = list(map(int, input().split()))
order = input().strip()

# 세 수 정렬하기
sorted_numbers = sorted(numbers)

# 출력 순서에 맞게 출력하기
result = [0] * 3
for i, char in enumerate(order):
    if char == 'A':
        result[i] = sorted_numbers[0]
    elif char == 'B':
        result[i] = sorted_numbers[1]
    elif char == 'C':
        result[i] = sorted_numbers[2]

# 결과 출력하기
print(result[0], result[1], result[2])
