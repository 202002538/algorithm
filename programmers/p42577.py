# 해시/ 전화번호 목록
from collections import Counter

def solution(phone_book):
    pb = Counter(phone_book)

    for i in pb:
        s = ''
        for j in i:
            s += j
            if s in pb and s != i:
                return False

    return True

if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
    print(solution(["12","123","1235","567","88"]))