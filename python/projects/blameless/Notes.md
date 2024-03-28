### Bugs

#### Not Random

This isn't random at all; It returns the same 10 specs every time.
The top 10 specs in the data file to be precise.

```python
api_specs = api_specs[:10]
Random(seed).shuffle(api_specs[:10])
```

#### We really shouldn't be using eval()

```python
api_specs = [eval(api_spec.strip().format(seed)) for api_spec in api_specs]
```
