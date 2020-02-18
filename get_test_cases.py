import requests, json, sys
size, level  = 4, 2
url = f"http://www.cs.utep.edu/cheon/ws/sudoku/new/?size={size}&level={level}"
data = json.loads(requests.get(url).text)
print(data)
matrix = [[0]*size for _ in range(size)]
for point in data["squares"]:
    matrix[point["x"]][point["y"]] = point["value"]
with open(sys.argv[1], "w") as file:
    file.writelines([" ".join(list(map(str, x)))+"\n" for x in matrix])