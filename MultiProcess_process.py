import time
from multiprocessing import Process 
# processモジュールを使用したマルチプロセス

def search_prime(x):
    isprime = 0 #素数なら最後まで0のまま
    # エラトステネスのふるいで素数判別を行う関数
    if x % 2 == 0:
        isprime+=1
        
    for num in range(3, int(x**0.5) + 1, 2):
        if x % num == 0:
            isprime+=1
            # print(isprime,x,num)
    if (isprime == 0):
        print("{}:Prime Number".format(x))
    else:
        print("{}:Not Prime Number".format(x))


    
numbers = [10**18+3, 10**17+13, 10**17+19, 10**15+21, 10**14+49]
# numbers = [3,5,7,11,17]  # 実行テスト

start = time.time()

processes = []
for n in numbers:
    process = Process(target=search_prime,args=(n,))
    process.start()
    processes.append(process)
    # print(process)
for p in processes:
    p.join()
end = time.time()

print("以上 {}個の素数判別にかかった時間は {} 秒でした．".format(len(numbers),end - start))
