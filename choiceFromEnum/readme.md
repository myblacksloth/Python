

# Choice a class to use using an enumChoice a class to use using an enum

Si consiglia di creare una classe che rappresenta l'oggetto generico e di usare l'enumerazione per la scelta della sottoclasse corrispondente

## enumerazione che indica gli oggetti da usare

```python
class ManyChoices(Enum):
    A = FirstAlgo
    B = SecondAlgo
```

## Scelta dell'oggetto

```python
ALGO = ManyChoices.A
```

## uso dell'oggetto

```python
self.algo = conf.ALGO.value()
        self.algoValue = conf.ALGO.value()
```

## esecuzione

```python
print(f"current algo is {self.algo}")
```

    current algo is ManyChoices.A

```python
print(f"current algo is {self.algoValue}")
```

    current algo is <src.algos.firstAlgo.FirstAlgo object at 0x1083c4b50>