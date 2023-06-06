import sys
input = sys.stdin.readline

def Rev(N):
    N = int(str(N)[::-1])

    return N


if __name__ == "__main__":
    X, Y = map(int, input().split())
    print(Rev(Rev(X) + Rev(Y)))


