import sys, os; sys.path.insert(0, os.path.abspath('..'));
''' Some reason below import is not working'''
"""import sys
# feb dir contains fibo.py
sys.path.append('example/feb')"""

from feb.fibo import fib
print (fib(500))