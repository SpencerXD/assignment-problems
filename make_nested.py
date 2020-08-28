def make_nested(colors):
    two_keys = {}
    for string in colors:
        strsplit = string.split('_')
        if strsplit[0] not in two_keys:
            two_keys[strsplit[0]] = {}
        two_keys[strsplit[0]][strsplit[1]] = colors[string]
    return two_keys
assert make_nested({
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
 }) == {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}, "Test Failed"
print("PASSED")
