# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python
def solution(brown, yellow):
    t = brown + yellow
    for a in range(1, yellow + 1):
        if yellow % a == 0:
            b = yellow // a
            if (a + 2) * (b + 2) == t:
                return [a + 2, b + 2] if a > b else [b + 2, a + 2]
print(solution(8, 1))