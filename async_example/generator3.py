# 제너레이터라는 것을 알아보긴 했지만, 제너레이터를 사용해야하는 이유는 무엇일까요?
import random
import os
import time
import psutil

process = psutil.Process(os.getpid())
titles = ["달빛조각사", "김비서가 왜그럴까", "롱리브더킹", "나 혼자만 레벨업", "독고", "묵향"]
expose = ["메인홈", "랭킹", "이벤트페이지", "뽑기권", "카테고리홈", "기다리면 무료", "오리지널"]


def memory_usage_mb():
    return process.memory_info().rss / 1000000


mem_before = memory_usage_mb()
print(f"Memory (Before): {mem_before:.2f}Mb")


def series_product_list(size):
    result = []
    for n in range(size):
        series = {
            "id": n,
            "title": random.choice(titles),
            "expose": random.choice(expose),
            "update_dt": time.time(),
        }
        result.append(series)
    return result


def series_product_gen(size):
    for n in range(size):
        series = {
            "id": n,
            "title": random.choice(titles),
            "expose": random.choice(expose),
            "update_dt": time.time(),
        }
        yield series


SIZE = 3000000
before = time.perf_counter()
# series_list = series_product_list(SIZE)
series_gen = series_product_gen(SIZE)
after = time.perf_counter()

mem_after = memory_usage_mb()
print(f"Memory (After): {mem_after:.2f}Mb")
print(f"Used Memory : {(mem_after - mem_before):.2f}Mb")
print(f"Elapsed Time : {(after - before):.2f}")

# 리스트 사용시
# Memory (Before): 10.47Mb
# Memory (After): 1002.76Mb
# Used Memory : 992.29Mb
# Elapsed Time : 6.25

# 제너레이터 사용시
# Memory (Before): 10.45Mb
# Memory (After): 10.47Mb
# Used Memory : 0.02Mb
# Elapsed Time : 0.00
