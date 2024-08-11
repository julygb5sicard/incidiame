def my_generator():
    yield [3, 13, 0.0026151305454316953]

# Using the generator
gen = my_generator()
result = next(gen)
print(result)  # Output: [3, 13, 0.0026151305454316953]
