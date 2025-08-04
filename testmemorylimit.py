# # # Try allocating a large object
# # try:
# #     big_list = [0] * (10**8)  # ~800MB
# #     print("Success")
# # except MemoryError:
# #     print("Memory Limit Hit!")
# import time
# def heavy_task():
#     count = 0
#     for i in range(10**9):
#         count += i

# start = time.time()
# heavy_task()
# print("CPU-heavy task finished in", time.time() - start, "seconds")

