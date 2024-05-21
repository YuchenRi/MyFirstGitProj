def capitalize_and_ascii_sum(word: str):
    return sum(ord(x) for x in word.capitalize())
animals = ["cat","dog","cow"]
animal_output = list(map(capitalize_and_ascii_sum, animals))
print(animal_output)

# Lambda 

numbers = [2,4,6,8,10,12]
squares = map(lambda y: y ** 2, numbers)
print(list(squares))