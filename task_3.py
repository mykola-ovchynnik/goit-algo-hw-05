import timeit
import re
import random
import string
from collections import defaultdict


def kmp_search(pattern, text):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return True
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def boyer_moore_search(pattern, text):
    def build_bad_character_table(pattern):
        bad_char = {char: -1 for char in set(text)}
        for i, char in enumerate(pattern):
            bad_char[char] = i
        return bad_char

    bad_char = build_bad_character_table(pattern)
    m, n = len(pattern), len(text)
    shift = 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            return True
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))
    return False


def rabin_karp_search(pattern, text, prime=101):
    d = 256
    m, n = len(pattern), len(text)
    p_hash = t_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i : i + m] == pattern:
                return True
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime
    return False


def measure_time(func, pattern, text):
    return timeit.timeit(lambda: func(pattern, text), number=1)


def read_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


text1 = read_text("article1.txt")
text2 = read_text("article2.txt")

existing_substring = text1[:20]
non_existing_substring = "".join(random.choices(string.ascii_letters, k=20))

results = defaultdict(dict)
for algo, func in zip(
    ["KMP", "Boyer-Moore", "Rabin-Karp"],
    [kmp_search, boyer_moore_search, rabin_karp_search],
):
    results[algo]["Article 1 - Existing"] = measure_time(
        func, existing_substring, text1
    )
    results[algo]["Article 1 - Non-existing"] = measure_time(
        func, non_existing_substring, text1
    )
    results[algo]["Article 2 - Existing"] = measure_time(
        func, existing_substring, text2
    )
    results[algo]["Article 2 - Non-existing"] = measure_time(
        func, non_existing_substring, text2
    )

for category in results[list(results.keys())[0]].keys():
    fastest_algo = min(results, key=lambda algo: results[algo][category])
    print(
        f"Fastest for {category}: {fastest_algo} ({results[fastest_algo][category]:.6f} sec)"
    )
