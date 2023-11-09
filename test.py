# coding=utf-8
"""This is a test python programm"""
# * if __name__ == "__main__":
# !
# ?
# TODO
# @param


import threading
import time

# *Thread继承
# class MyThread(threading.Thread):
#     """MyThread继承测试"""

#     def __init__(self, name=None):
#         super().__init__(name=name)

#     def run(self):
#         t = threading.current_thread()

#         for n in range(5):
#             print("第{0}次执行此线程{1}".format(n, t.name))
#             time.sleep(0.5)
#         print("线程{0}执行完成".format(t.name))


# t1 = MyThread("Thread1_ByKevin")
# t2 = MyThread("Thread2_ByKevin")

# t1.start()
# t2.start()

# *Thread合并
# value = []
# def thread_body():
#     print("t1子线程开始...")

#     for n in range(5):
#         print("t1子线程执行...")
#         value.append(n**2)
#         time.sleep(2)

#     print("t1子线程结束...")


# print("主线程开始执行...")
# t1 = threading.Thread(target=thread_body)

# t1.start()
# t1.join()
# print("value = {0}".format(value))
# print("主线程结束...")

# *Thread控制
# ACTIVE = True
# def working_body():
#     """working body"""
#     while ACTIVE:
#         print("工作线程执行...")
#         time.sleep(2)
#     print("工作线程结束...")


# def control_body():
#     """control body"""
#     global ACTIVE
#     while ACTIVE:
#         command = input("请输入停止指令: ")
#         if command == "exit":
#             ACTIVE = False
#             print("控制线程结束...")


# workthread = threading.Thread(target=working_body)
# workthread.start()

# controlthread = threading.Thread(target=control_body)
# controlthread.start()
