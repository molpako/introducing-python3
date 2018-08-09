# deque = スタックとキューの機能を持つ
# 回文がどうかチェックするサンプル

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True

palindrome('a')
palindrome('racecar')
palindrome('')
palindrome('radar')
palindrome('halibut')
