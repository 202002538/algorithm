# Summer/Winter Coding(~2018) / 스티커 모으기(2)

def dp(s):
    s[1] = max(s[0], s[1])
    for i in range(2, len(s)):
        s[i] = max(s[i-1], s[i-2] + s[i])
    return s[-1]

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker[0], sticker[1])

    pick_start = sticker[0:-1]
    not_pick_start = sticker[1:]
    return max(dp(pick_start), dp(not_pick_start))

if __name__ == '__main__':
    print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
    print(solution([1, 3, 2, 5, 4]))
