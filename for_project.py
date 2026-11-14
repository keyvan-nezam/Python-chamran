width = 8
height = 4

print("        ",end="")

for i in range(width):
    print("─", end="")
print()
print("        ",end="")

for i in range(height - 2):
    print("│" + " " * (width - 2) + "│")
    print("        ",end="")

for i in range(width):
    print("─", end="")
print()
