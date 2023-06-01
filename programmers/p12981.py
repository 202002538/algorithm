# Summer/Winter Coding(~2018) / 영어 끝말잇기
from collections import deque

def solution(n, words):
    used_word = deque([words.pop(0)])
    for i, w in enumerate(words):
        if w not in used_word and w[0] == used_word[-1][-1]:
            used_word.append(w)
        else:
            return [((i+1) % n) + 1, ((i+1) // n) + 1]
    else:
        return [0,0]

if __name__ == '__main__':
    print(solution(3, 	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

