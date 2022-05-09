m, d = map(int, input().split())

MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

# 1월 1일 월요일

total_days = d # 입력 월의 days에
for n in MONTH[:m-1] :
    total_days += n # 입력 월 이전 days (=n) 더하기

index = total_days % 7 - 1 # 전체 days를 요일의 개수 7로 모듈러 연산
print(DAYS[index])