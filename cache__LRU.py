from functools import lru_cache

@lru_cache(maxsize=10)
def factorial(n):
    if n<=1: return 1
    print(f'computing {n}!')
    return n * factorial(n-1)

print(factorial(5))
print(factorial(3))
print(factorial(10))
print(factorial(20))


''' out>
computing 5!
computing 4!
computing 3!
computing 2!
120
6
computing 10!
computing 9!
computing 8!
computing 7!
computing 6!
3628800
computing 20!
computing 19!
computing 18!
computing 17!
computing 16!
computing 15!
computing 14!
computing 13!
computing 12!
computing 11!
2432902008176640000
'''