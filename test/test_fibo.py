import sys
# feb dir contains fibo.py
sys.path.append('example/feb')


from feb.fibo import fib
print (fib(500))