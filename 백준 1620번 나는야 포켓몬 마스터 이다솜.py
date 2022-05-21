# https://www.acmicpc.net/problem/1620

# 입력
# 입력 수 / 반환 정답 수
# 입력 ...
# 숫자 / 문자 확인 후 알맞는 값 반환

import sys

n, m = map(int, input().split())

dicName = {}
dicNum = {}
for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    dicName[i] = name
    dicNum[name] = i

for i in range(m):
    answer = sys.stdin.readline().strip()
    # .isdigit() - String 클래스 메서드
    # 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
    if answer.isdigit():
        print(dicName[int(answer)])
    else:
        print(dicNum[answer])