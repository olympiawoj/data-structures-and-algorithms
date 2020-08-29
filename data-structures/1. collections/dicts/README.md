# Dictionary

https://www.w3schools.com/python/python_dictionaries.asp

- A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.


```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```

## Access Items
- By referring to it's key name inside square brackets
item = dictname["keyname"]
x = thisdict["model"]

- Method called `get()` which gives you the same result

x = thisdict.get("model")


## Change Values
- You can change the value of a specific item by referring to it's key name
thisdict["year"] = 2018


## Loop through a dictionary
- You can loop through a dictionary by using a `for` loop
- While looping through a dictionary, the return value are the `keys` of the dictionary, but there are methods to return the `values` as well

### Print all key names in the dictionary
```python
for x in thisdict:
  print(x)
```

### Print all values
```python
for x in thisdict:
  print(thisdict[x])


for x in thisdict.values():
  print(x)
```

## Loop through all keys and values
```python
for x, y in thisdict.items():
  print(x, y)

```


## Check if key exists



## Dict Length




**Dictionaries**
- We have a group of values and they're stored as key/value pairs
- Look v similar to objects you might've seen in JavaScript
- You will sometimes see people just JS objects in a dictionary-like manner
- KEY is name of the class/subject and value is the grade in that particular subject
- We access values using get function and entering key as parameter
- We can add values to our dictionary by simply using a key that does not exist
- If we use a key that DOES exist, for example English you can see was in original dictionary, it will not add a new key/value pair, instead it updates it
- Couple ways to remove —> either remove specific item by specifiying the key OR pop to remove the last item
- Like all other collections, length is accessible to us and we can traverse with a for loop