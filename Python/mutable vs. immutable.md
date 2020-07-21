# mutable vs. immutable

- immutable: String, Tuple, Range

```python
# immutable
a = 1
print(id(a))
a += 1
print(id(a))

a = 'a'
print(id(a))
a += 'b'
print(id(a))
```

- mutable: List, Set, Dictionary

```python
# mutable
a = [1,2]
print(a)
print(id(a))
a.append(3)
print(a)
print(id(a))
```

