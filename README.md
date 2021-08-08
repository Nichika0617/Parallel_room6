# エラトステネスの篩による素数判別のを逐次処理，並列処理で行い，処理時間の出力を行うプログラム

## プログラム
* SingleThread
  * エラトステネスの篩による素数判別を逐次処理で行う
* MultiThread
  * エラトステネスの篩による素数判別をconcurrent.futuresのThreadPoolExecutorクラスを用いて並列処理で行う．
* MultiThread_threading
  * エラトステネスの篩による素数判別をthreadingモジュールを用いて並列処理行う．
* MultiProcess
  * エラトステネスの篩による素数判別をconcurrent.futuresのProcessPoolExecutorクラスを用いて並列処理で行う．
* MultiProcess_process
  * エラトステネスの篩による素数判別をmultiprocessingモジュールを用いて行う．


## 開発環境
* Python
  * concurrent.futures
  * threading
  * multiprocessing
  
## 実行方法
ターミナルより．

```python ファイル名```

と実行することでプログラムを動かすことができる．

処理が終わると素数判別にかかった時間が出力される．