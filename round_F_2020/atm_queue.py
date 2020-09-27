def main():
    cases = int(input())
    for case in range(cases):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        for i in range(n):
            a[i] = (a[i] // x + int(a[i] % x != 0), i)
        a.sort()
        print("Case #{}:".format(case + 1), end=" ")
        for i in range(n):
            end = "\n" if i == n - 1 else " "
            print(a[i][1] + 1, end=end)


if __name__ == "__main__":
    main()
