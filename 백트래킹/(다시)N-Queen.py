import sys
from collections import deque
input = sys.stdin.readline

def promising(cdx):
    for i in range(cdx):
        if(board[cdx] == board[i] or abs(cdx - i) == abs(board[cdx] - board[i])):
            return 0
    return 1

def nqueen(cdx):
    global answer

    if cdx == N:
        answer+=1
        return
    
    for i in range(N):
        board[cdx] =i
        if promising(cdx):
            nqueen(cdx + 1)

if __name__ == "__main__":
    N = int(input())
    answer = 0
    board = [0] * (N)
    nqueen(0)
    print(answer)