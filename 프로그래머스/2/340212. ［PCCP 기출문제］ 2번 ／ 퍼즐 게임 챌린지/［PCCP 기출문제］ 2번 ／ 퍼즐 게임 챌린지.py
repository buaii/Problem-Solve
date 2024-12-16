def solution(diffs, times, limit):
    max_level = max(diffs)
    min_level = min(diffs)  # 최소 난이도는 0부터 시작
    cur_level = max_level

    while min_level <= max_level:
        cur_level = (max_level + min_level) // 2
        answer = 0
        prev_t = 0
        
        # 현재 `cur_level`에 따른 시간 계산
        for diff, t in zip(diffs, times):
            if diff <= cur_level:
                answer += t
            else:
                answer += (t + prev_t) * (diff - cur_level) + t
            prev_t = t

        # 제한 시간을 초과하면 난이도 범위 증가
        if answer > limit:
            min_level = cur_level + 1
        elif answer == limit:
            min_level = cur_level
            break
        else:
            max_level = cur_level - 1

    return min_level  # 최적의 난이도를 반환
