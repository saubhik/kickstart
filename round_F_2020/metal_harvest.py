def main():
    cases = int(input())
    for case in range(cases):
        n, k = map(int, input().split())

        intervals = [[0, 0]] * n
        for i in range(n):
            intervals[i] = list(map(int, input().split()))
        intervals.sort()

        deployments, last_deployment_end = 0, 0
        for interval in intervals:
            si, ei = interval

            # Interval not covered.
            if ei > last_deployment_end:
                last_deployment_start = max(last_deployment_end, si)
                uncovered_length = ei - last_deployment_start
                num_deployments = uncovered_length // k + int(uncovered_length % k != 0)
                deployments += num_deployments
                last_deployment_end = last_deployment_start + num_deployments * k

        print("Case #{}: {}".format(case + 1, deployments))


if __name__ == "__main__":
    main()
