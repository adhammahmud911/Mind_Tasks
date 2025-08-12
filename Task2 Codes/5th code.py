import re

# Get dimensions
rows, cols = map(int, input("Enter matrix size (rows cols): ").split())

# Get matrix lines
print(f"Please input {rows} lines, each containing {cols} characters:")
grid = []
for _ in range(rows):
    line = input()
    # Ensure each row is exactly `cols` characters
    line = (line + " " * cols)[:cols]
    grid.append(line)

# Read column by column to form the raw message
message = ""
for c in range(cols):
    for r in range(rows):
        message += grid[r][c]

# Replace unwanted characters between alphanumeric characters with a space
final_message = re.sub(r'(?<=\w)([^\w]+)(?=\w)', " ", message)

print("The text is:", final_message)
