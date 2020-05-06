import random 
import time

ttime = random.randint(1, 10)
print('Your target time is {} seconds. Good luck!'.format(
    ttime))

input('-' * 20 + 'Press Enter to Begin' + '-' * 20)
stime = time.perf_counter()

print('Wait {} seconds to press the next Enter'.format(ttime))

input('-' * 20 + 'Press Enter to Begin' + '-' * 20)
etime = time.perf_counter() - stime

if etime == ttime:
    print('Unbelievable! You got it right!')
else:
    print('You are off by {} seconds :('.format(abs(etime-ttime)))
    print('Better luck next time!')


