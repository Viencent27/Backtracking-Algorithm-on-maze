import random

# Fungsi cetak maze
def cetakMaze(maze):
  for i in range(lebar):
    for j in range(panjang):
      print(maze[i][j], end=" ")
    print("")

# Fungsi cek neighbour
def cekNeighbour(randWall):
  jalan = 0
  if maze[randWall[0]-1][randWall[1]] == " ":
    jalan += 1
  if maze[randWall[0]+1][randWall[1]] == " ":
    jalan += 1
  if maze[randWall[0]][randWall[1]-1] == " ":
    jalan += 1
  if maze[randWall[0]][randWall[1]+1] == " ":
    jalan += 1
  
  return jalan

# Fungsi untuk menghapus daftar index di variabel walls
def delWall(randWall):
  for i in walls:
    if i[0] == randWall[0] and i[1] == randWall[1]:
      walls.remove(i)

# Fungsi untuk menandai wall bagian atas
def wallTop(randWall):
  if randWall[0] != 0:
    if maze[randWall[0]-1][randWall[1]] != " ":
      maze[randWall[0]-1][randWall[1]] = wall
    if [randWall[0]-1, randWall[1]] not in walls:
      walls.append([randWall[0]-1, randWall[1]])

# Fungsi untuk menandai wall bagian kanan
def wallRight(randWall):
  if randWall[1] != panjang - 1:
    if maze[randWall[0]][randWall[1]+1] != " ":
      maze[randWall[0]][randWall[1]+1] = wall
    if [randWall[0], randWall[1]+1] not in walls:
      walls.append([randWall[0], randWall[1]+1])

# Fungsi untuk menandai wall bagian bawah
def wallBottom(randWall):
  if randWall[0] != lebar - 1:
    if maze[randWall[0]+1][randWall[1]] != " ":
      maze[randWall[0]+1][randWall[1]] = wall
    if [randWall[0]+1, randWall[1]] not in walls:
      walls.append([randWall[0]+1, randWall[1]])

# Fungsi untuk menandai wall bagian kiri
def wallLeft(randWall):
  if randWall[1] != 0:
    if maze[randWall[0]][randWall[1]-1] != " ":
      maze[randWall[0]][randWall[1]-1] = wall
    if [randWall[0], randWall[1]-1] not in walls:
      walls.append([randWall[0], randWall[1]-1])

# Input panjang dan lebar maze
wall = "⛝"
maze = []
panjang = int(input("Masukkan panjang maze = "))
lebar = int(input("Masukkan lebar maze = "))

# Tandai semua cells unvisited
for i in range(lebar):
  line = []
  for j in range(panjang):
    line.append("U")
  maze.append(line)

# Index awal random
randPanjang = random.randrange(1, panjang-1)
randLebar = random.randrange(1, lebar-1)

# Tandai index awal menjadi jalan dan neighbour menjadi wall
maze[randLebar][randPanjang] = " "
maze[randLebar-1][randPanjang] = wall
maze[randLebar+1][randPanjang] = wall
maze[randLebar][randPanjang-1] = wall
maze[randLebar][randPanjang+1] = wall

# Variabel untuk menampung index wall yg dpt berubah menjadi jalan
walls = []
walls.append([randLebar-1, randPanjang])
walls.append([randLebar+1, randPanjang])
walls.append([randLebar, randPanjang-1])
walls.append([randLebar, randPanjang+1])

# Selama masih ada index wall yg dpt berubah menjadi jalan
while(walls):
  # Ambil random wall dari variabel walls
  randWall = walls[random.randrange(len(walls))-1]

  # Jika wall di sebelah kiri jalan dan tidak di index 0
  if randWall[1] != 0:
    if maze[randWall[0]][randWall[1]-1] == "U" and maze[randWall[0]][randWall[1]+1] == " ": # U ⛝ " "
      # Cek banyak jalan di neighbour
      jalan = cekNeighbour(randWall)
      if jalan < 2:
        # Tandai sebagai jalan
        maze[randWall[0]][randWall[1]] = " "

        # Tandai wall baru
        wallTop(randWall)
        wallBottom(randWall)
        wallLeft(randWall)

      # Hapus wall dari walls
      delWall(randWall)
      
      continue
  
  # Jika wall di sebelah atas jalan dan tidak di index 0
  if randWall[0] != 0:                                                                      # U
    if maze[randWall[0]-1][randWall[1]] == "U" and maze[randWall[0]+1][randWall[1]] == " ": # ⛝
      # Cek banyak jalan di neighbour                                                         " "
      jalan = cekNeighbour(randWall)
      if jalan < 2:
        # Tandai sebagai jalan
        maze[randWall[0]][randWall[1]] = " "

        # Tandai wall baru
        wallTop(randWall)
        wallRight(randWall)
        wallLeft(randWall)

      # Hapus wall dari walls
      delWall(randWall)
      
      continue

  # Jika wall di sebelah kanan jalan dan tidak di index panjang - 1
  if randWall[1] != panjang - 1:
    if maze[randWall[0]][randWall[1]+1] == "U" and maze[randWall[0]][randWall[1]-1] == " ": # " " ⛝ U
      # Cek banyak jalan di neighbour
      jalan = cekNeighbour(randWall)
      if jalan < 2:
        # Tandai sebagai jalan
        maze[randWall[0]][randWall[1]] = " "

        # Tandai wall baru
        wallTop(randWall)
        wallRight(randWall)
        wallBottom(randWall)

      # Hapus wall dari walls
      delWall(randWall)
      
      continue

  # Jika wall di sebelah bawah jalan dan tidak di index lebar - 1
  if randWall[0] != lebar - 1:                                                              # " "
    if maze[randWall[0]+1][randWall[1]] == "U" and maze[randWall[0]-1][randWall[1]] == " ": # ⛝
      # Cek banyak jalan di neighbour                                                         U
      jalan = cekNeighbour(randWall)
      if jalan < 2:
        # Tandai sebagai jalan
        maze[randWall[0]][randWall[1]] = " "

        # Tandai wall baru
        wallLeft(randWall)
        wallRight(randWall)
        wallBottom(randWall)

      # Hapus wall dari walls
      delWall(randWall)
  
  delWall(randWall)

# Ubah unvisited menjadi wall
for i in range(lebar):
  for j in range(panjang):
    if maze[i][j] == "U":
      maze[i][j] = wall

# Random tempat start dan finish
start = []
finish = []
for j in range(panjang):
  if maze[1][j] == " ":
    start.append(j)
  if maze[lebar-2][j] == " ":
    finish.append(j)
maze[0][random.choice(start)] = " "
maze[lebar-1][random.choice(finish)] = " "

if __name__ == '__main__':
  cetakMaze(maze)