#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return [num for num, prime in enumerate(is_prime) if prime]

def prime_game_winner(n, primes):
    prime_set = set(primes)
    moves = 0
    current_numbers = set(range(1, n + 1))
    
    while True:
        found_prime = False
        for prime in primes:
            if prime in current_numbers:
                found_prime = True
                moves += 1
                multiples = set(range(prime, n + 1, prime))
                current_numbers -= multiples
                break
        if not found_prime:
            break
    
    return "Maria" if moves % 2 == 1 else "Ben"

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    results = {}

    for n in nums:
        if n in results:
            continue
        results[n] = prime_game_winner(n, primes)
    
    maria_wins = sum(1 for result in results.values() if result == "Maria")
    ben_wins = x - maria_wins
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test the function with the example provided
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
