# JSON lines benchmark

Benchmark for (stream-)parsing a JSON lines document.

## Usage

```
pip install -r requirements.txt
python create.py

ipython

In [2]: %timeit sum()
Sum of all keys: 1000001
Sum of all keys: 1000001
Sum of all keys: 1000001
Sum of all keys: 1000001
Sum of all keys: 1000001
Sum of all keys: 1000001
Sum of all keys: 1000001
Sum of all keys: 1000001
3.74 s ± 152 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [3]: %timeit search(uuid)
Found uuid 9531ba30-90ee-4dd1-afe8-47fd8417701b, key 2
Found uuid 9531ba30-90ee-4dd1-afe8-47fd8417701b, key 2
Found uuid 9531ba30-90ee-4dd1-afe8-47fd8417701b, key 2
Found uuid 9531ba30-90ee-4dd1-afe8-47fd8417701b, key 2
Found uuid 9531ba30-90ee-4dd1-afe8-47fd8417701b, key 2
Found uuid 9531ba30-90ee-4dd1-afe8-47fd8417701b, key 2
Found uuid 9531ba30-90ee-4dd1-afe8-47fd8417701b, key 2
Found uuid 9531ba30-90ee-4dd1-afe8-47fd8417701b, key 2
1.79 s ± 53 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

## Preliminary results

 * 3.7s to fetch 1M records (3.7 mus / record)
 * 1.8s to find a record in the middle of the bunch
