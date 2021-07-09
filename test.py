# # _*_ coding: utf-8 _*_
# # def longestPalindrome( s: str) -> str:
# #     if len(s) < 2 or s == s[::-1]:
# #         return s
# #     res = s[0]
# #     maxlen = 1
# #     for i in range(1, len(s)):
# #         print('i: ',i,'  s[i]: ',s[i])
# #         odd = s[i - maxlen - 1: i + 1]
# #         print(odd)
# #         even = s[i - maxlen: i + 1]
# #         print(even)
# #         if odd == odd[::-1] and i - maxlen - 1 >= 0:
# #             res = odd
# #             maxlen += 2
# #             print('maxlenth: ',maxlen)
# #             continue
# #         if even == even[::-1] and i - maxlen >= 0:
# #             res = even
# #             maxlen += 1
# #             print('maxlenth: ',maxlen)
# #             continue
# #     return res
# #
# #
# # s='5434567890098765432'
# # print()
# # print(longestPalindrome(s))
#
# import sys
from memory_profiler import profile
#
#
# s='a test '
# if s.split():
#     print('s.split():  ',s.split())
#
# # t='你好， 外星人不在家 ' + ' 外星人不在家,哈哈'*4999
# # print(s.split()[-1])
# # print('sys.getsizeof(s.split()):', sys.getsizeof(s.split()))
# # print('sys.getsizeof(t.split()):', sys.getsizeof(t.split()))
# # print('len(t.split()[-1]): ',len(t.split()[-1]),'sys.getsizeof(len(t.split()[-1])): ',sys.getsizeof(len(t.split()[-1])))
# # print('len(s.split()[-1]): ',len(s.split()[-1]),'sys.getsizeof(len(s.split()[-1])): ',sys.getsizeof(len(s.split()[-1])))
# # print('s total(K):',sys.getsizeof(s)+sys.getsizeof(s.split())+sys.getsizeof(len(s.split()[-1]))+sys.getsizeof(s.split()[-1]))
# # print('t total(K):',sys.getsizeof(t)+sys.getsizeof(t.split())+sys.getsizeof(len(t.split()[-1]))+sys.getsizeof(t.split()[-1]))
# # # @profile
# # def get_last_len(s):
# #     a=' ssatage' *5000
# #     a.split()[-1]
# #     return len(s.split()[-1])
#
#
# if __name__ == '__main__':
#     # print(get_last_len(t))
#     # print('sys.getsizeof(get_last_len(t)):', sys.getsizeof(get_last_len(t)))
#     pass




# nums=[2,3,1,2,4,3,6]
# target=6
# minlenth = len(nums)
# for i in range(0, len(nums)):
#     for j in range(i+1, len(nums)+1):
#         a = nums[i:j]
#         if sum(nums[i:j]) >= target :
#             minlenth = min(minlenth, j - i )
#             break
#         else:
#             continue
# print(minlenth)


#
# numRows = 5
# fi = [[1] * i for i in range(1,numRows+1)]
# for i in range(2,numRows):
#     for j in range(1, i):
#         fi[i][j] = fi[i - 1][j - 1] + fi[i - 1][j]
#
# print(fi)
#
#
# s=[1]
# s.append(0)
# N=[s[i-1]+s[i] for i in range(len(s))]
# s=N[:]
# s.append(0)
# N=[s[i-1]+s[i] for i in range(len(s))]
# print(N)
#
# @profile
# def fii(rownum):
#     s=[1]
#     N=s
#     t=[1]
#     for i in range(1,rownum):
#         s.append(0)
#         print('i',i)
#         print('len',len(s))
#         N = [s[i-1]+s[i] for i in range(len(s))]
#         print(N)
#         s=N[:]
#
#         print('---------')
#
#     print(N)
#
#     for i in range(1,rownum+1):
#         print(i)
#         # fis = i
#         # t.append()
#
#
#
# fii(6)
nums=[0,1,1,0,56,2]
i = 0
j = len(nums)
# for x in range(j):
#     if nums[x] != 0:
#         nums[i] = nums[x]
#         i += 1
# for y in range(i,j):
#     nums[y]=0


# import json
#
# json.loads()


s = 'abcde'
print(s[::-1])

print(sum([i for i in range(1,101)]))



from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')