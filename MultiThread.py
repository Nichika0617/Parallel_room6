import time
from concurrent import futures

def search_prime(x):
    if x % 2 == 0:
        return False

    for num in range(3, int(x**0.5) + 1, 2):
        if x % num == 0:
            return False

    return True

numbers = [10**18+3, 10**17+13, 10**17+19, 10**15+21, 10**14+49]
# numbers = [3,5,7,11,17]  # 実行テスト

start = time.time()
with futures.ThreadPoolExecutor() as executor:
    # スレッドの束を最初に生成する，作った束に処理適当に割り振る
    mappings = {executor.submit(search_prime, n): n for n in numbers}
    for future in futures.as_completed(mappings):
        target = mappings[future]
        result = future.result()
        if result == True:
            print("{n}:Prime Number".format(n=target))
        else:
            print("{n}:Not Prime Number".format(n=target))
end = time.time()

print("以上 {}個の素数判別にかかった時間は {} 秒でした．".format(len(numbers),end - start))
