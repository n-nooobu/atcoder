import io
import sys

# input here
_INPUT = """\
10 4
1346 1347 1348 1349
1353 1354 1355 1356
1360 1361 1362 1363
1367 1368 1369 1370
1374 1375 1376 1377
1381 1382 1383 1384
1388 1389 1390 1391
1395 1396 1397 1398
1402 1403 1404 1405
1409 1410 1411 1412

"""
sys.stdin = io.StringIO(_INPUT)



import sys

N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

j0 = (B[0][0] - 1) % 7
i0 = (B[0][0] - 1 - j0) // 7
for a in range(N):
    i = i0 + a
    for b in range(M):
        j = j0 + b
        if j >= 7:
            print('No')
            sys.exit()
        if B[a][b] != i * 7 + j + 1:
            print('No')
            sys.exit()

print('Yes')
