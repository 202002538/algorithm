# 해시/ 베스트앨범
from collections import defaultdict

def solution(genres, plays):
    answer = []

    # 딕셔너리 초기화 --> 키: 장르명/ 밸류: (재생횟수, 곡번호)
    my_dict = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        my_dict[g].append([p,i])

    # 총 재생횟수 카운트 후 밸류 맨뒤에 넣음
    for k, v in my_dict.items():
        n = 0
        for ele in v:
            n += ele[0]
        my_dict[k].append([n])

    # 총 재생횟수로 장르 정렬
    my_dict = dict(sorted(my_dict.items(), key=lambda x: x[1][-1], reverse=True))

    # 각 재생횟수로 장르 내 곡들 정렬, 상위 2곡 수록
    for k in my_dict.keys():
        my_dict[k] = my_dict[k][:-1] #맨끝의 총 재생횟수 제거
        my_dict[k] = sorted(my_dict[k], key=lambda x:x[0], reverse=True)
        for i in my_dict[k][:2]:
            answer.append(i[1])
    return answer

if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))