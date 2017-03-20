n = int(raw_input())
jobs = []
for i in xrange(n):
    w, l = map(int, raw_input().split(" "))
    jobs.append((w,l))

print jobs
