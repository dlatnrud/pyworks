# thread_test.py
import time
import threading    # 스레드를 생성하기 위해서는 threading 모듈이 필요
# 멀티 스레드 - 실행된 프로세서가 2개 이상인 것

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)
print("Start")

threads = []    # [t1, t2, t3, t4, t5]
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성(실행할 작업 생성)
    threads.append(t)

for t in threads:
    t.start()   # 스레드를 실행

for t in threads:
    t.join()    # 멀티(병렬) 스레드에서 사용되어야 함(join으로 스레드가 종료될 때까지 기다린다.)

print("End")