from pathlib import Path

path1 = Path("ecommerce")
print(path1.exists())

path2 = Path()
for file in path2.glob('*.py'):
    print(file)
for file in path2.glob('*'):
    print(file)

