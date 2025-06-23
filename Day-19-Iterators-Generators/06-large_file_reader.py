def read_large_file():
    for i in range(10000):
        yield f"Line{i}"


for line in read_large_file():
    if int(line.split("Line")[1]) > 10:
        break
    print(line)
