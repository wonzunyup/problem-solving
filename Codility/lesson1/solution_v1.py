def solution(N):
    max_gap = 0
    binary = ""
    
    while N > 1 :
        binary += str((N % 2))
        N //= 2
    binary += str(N)
    binary = binary[::-1]
    
    for i in range(len(binary)) :
        if binary[i] == '0' :
            temp = 0
            for j in range(i, len(binary)) :
                if binary[j] == '1' : break
                if j == len(binary) - 1 :
                    temp = 0
                    break
                temp += 1
            if temp > max_gap : max_gap = temp
    return max_gap
