# 자릿수가 높은 것부터 하나씩 맞춰나가기

def solution(N, number):
    # 허뎝님의 수정 피드백 -> 테스트 케이스가 바뀌면서 예외 사항을 추가해야 함.
    if N == number:
        return 1

    # 1. [ SET x 8 ] 초기화
    s = [set() for x in range(8)]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    print(s)

    # 3. n 일반화
    #   {
    #       "n" * i U
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set,
    #    }
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            print(f"{i}, {j}")
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1
    for i in s:
        print(i)

    return answer

print(solution(5, 12))