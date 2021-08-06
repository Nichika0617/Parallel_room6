import time
import threading
# threadingモジュールを使用したマルチプロセス

def search_prime(x):
    isprime = 0 #素数なら0
    # エラトステネスのふるい
    if x % 2 == 0:
        isprime+=1
        
    for num in range(3, int(x**0.5) + 1, 2):
        if x % num == 0:
            isprime+=1
    
    if (isprime == 0):
            print("{}:Prime Number".format(x))
    else:
        print("{}:Not Prime Number".format(x))
            

numbers = [10**18+3, 10**17+13, 10**17+19, 10**15+21, 10**14+49]
# numbers = [3,5,7,11,17]  # 実行テスト

start = time.time()

threads = []
for n in numbers:
    thread = threading.Thread(target=search_prime,args=(n,))
    threads.append(thread)
    thread.start()
    # print(t)
for th in threads:
    th.join()
end = time.time()

print("以上 {}個の素数判別にかかった時間は {} 秒でした．".format(len(numbers),end - start))
