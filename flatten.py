colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

flatten_colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}


def flatten(dict_colors):
    final_dict = {}
    for key_colors in dict_colors:
        for key_sub in dict_colors[key_colors]:
            final_dict[key_colors + '_' + key_sub] = dict_colors[key_colors][key_sub]

    return final_dict

assert flatten(colors) == flatten_colors, "Test Failed"
print("PASSED")
