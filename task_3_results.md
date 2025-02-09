# Comparison of Substring Search Algorithms

In this study, we compare the efficiency of three substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp. The comparison is based on two text files (Article 1 and Article 2). We measure the execution time of each algorithm for two types of substrings: one that actually exists in the text and another that is fictional (randomly generated).

## Results

### Article 1

- **Existing Substring**

  - Knuth-Morris-Pratt: 0.000015 sec
  - Boyer-Moore: 0.000582 sec
  - Rabin-Karp: 0.000016 sec
  - **Fastest Algorithm**: Knuth-Morris-Pratt

- **Non-existing Substring**
  - Knuth-Morris-Pratt: 0.003401 sec
  - Boyer-Moore: 0.000854 sec
  - Rabin-Karp: 0.003989 sec
  - **Fastest Algorithm**: Boyer-Moore

### Article 2

- **Existing Substring**

  - Knuth-Morris-Pratt: 0.004823 sec
  - Boyer-Moore: 0.001241 sec
  - Rabin-Karp: 0.005682 sec
  - **Fastest Algorithm**: Boyer-Moore

- **Non-existing Substring**
  - Knuth-Morris-Pratt: 0.004822 sec
  - Boyer-Moore: 0.001165 sec
  - Rabin-Karp: 0.005901 sec
  - **Fastest Algorithm**: Boyer-Moore

Overall, Boyer-Moore demonstrates the best performance for most scenarios.Boyer-Moore mostly outperforms the others when dealing with large alphabets or longer patterns because it can skip more characters on average. Knuth-Morris-Pratt has an advantage when the pattern has repeated sub-patterns. Each algorithm's efficiency depends on the size of the text, the structure of the pattern, and the nature of the characters involved.
