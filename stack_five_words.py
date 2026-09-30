stack = []
maximum = 7

words = ["apple", "banana", "cherry", "orange", "grape"]

for word in words:
    if len(stack) < maximum:
        stack.append(word)

print(stack[-1])

stack.pop()
stack.pop()

print(stack[-1])