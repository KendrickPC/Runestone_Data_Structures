# 3.10.discussion_questions.py

# 1. Give the Big-O performance of the following code fragment:
for i in range(n):
   for j in range(n):
      k = 2 + 2

'''
Double nested loop so efficiency is O(n^2)
'''

#2. Give the Big-O performance of the following code fragment:
for i in range(n):
     k = 2 + 2
'''
O(n)
'''

#3. Give the Big-O performance of the following code fragment:
i = n
while i > 0:
   k = 2 + 2
   i = i // 2
'''
O(log(n)) because i is divided in half every time.
'''

#4. Give the Big-O performance of the following code fragment:
for i in range(n):
   for j in range(n):
      for k in range(n):
         k = 2 + 2

'''
O(n^3) becasue the loop is nested three times
'''

#5. Give the Big-O performance of the following code fragment:
for i in range(n):
   k = 2 + 2
for j in range(n):
   k = 2 + 2
for k in range(n):
   k = 2 + 2

'''
O(3n) or basically, O(n)
'''