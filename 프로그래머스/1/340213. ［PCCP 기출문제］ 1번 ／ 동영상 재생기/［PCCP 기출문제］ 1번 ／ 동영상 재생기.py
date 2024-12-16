def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_ttsec = ttsec(video_len)
    pos_ttsec = ttsec(pos)
    start_ttsec = ttsec(op_start)
    end_ttsec = ttsec(op_end)
    
    pos_ttsec = passOpening(pos_ttsec, start_ttsec, end_ttsec)
    
    for command in commands:
        pos_ttsec = passOpening(pos_ttsec, start_ttsec, end_ttsec)
        if command == "prev":
            pos_ttsec -= 10
            if pos_ttsec < 0:
                pos_ttsec = 0
        else:
            pos_ttsec += 10
            if pos_ttsec > video_ttsec:
                pos_ttsec = video_ttsec
                
    pos_ttsec = passOpening(pos_ttsec, start_ttsec, end_ttsec)
        
    #min = pos_ttsec // 60
    #sec = pos_ttsec % 60
    min, sec = divmod(pos_ttsec, 60)
    answer = f"{min:02d}:{sec:02d}"
    
    return answer

def ttsec(vlen):
    min, sec = map(int, vlen.split(":"))
    vlen = min*60 + sec
    
    return vlen

def passOpening(pos_ttsec, start_ttsec, end_ttsec):
    if start_ttsec <= pos_ttsec and pos_ttsec <= end_ttsec:
        pos_ttsec = end_ttsec
        
    return pos_ttsec