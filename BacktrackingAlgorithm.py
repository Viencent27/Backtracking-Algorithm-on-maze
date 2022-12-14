from RandMapMaze import maze, panjang, lebar

# Cek apakah ada neighbour yg kosong
def neighbourKosong(l, p):
  if maze[l+1][p] == " ":
    l += 1
  elif maze[l][p-1] == " ":
    p -= 1
  elif maze[l][p+1] == " ":
    p += 1
  elif maze[l-1][p] == " ":
    l -= 1
  
  return l, p

# Untuk mendapatkan index start
for i in range(panjang):
  if maze[0][i] == " ":
    tempPanjang = i
    break

count = 1
tempLebar = 1
maze[0][tempPanjang] = 0

# Memberi angka pada index yg dikunjungi menggunakan algoritma backtracking
while(" " in maze[lebar-1]):
  # Harus di awal, karna jika index [-1][] bisa jd paling bawah
  maze[tempLebar][tempPanjang] = count
  count += 1

  if tempLebar != lebar - 1:  # Biar ga index out of range abis cetak di finish
    if maze[tempLebar][tempPanjang-1] == " ": # Pindah ke kiri
      tempPanjang -= 1
    elif maze[tempLebar][tempPanjang+1] == " ": # Pindah ke kanan
      tempPanjang += 1
    elif maze[tempLebar-1][tempPanjang] == " ": # Pindah ke atas
      tempLebar -= 1
    elif maze[tempLebar+1][tempPanjang] == " ": # Pindah ke bawah
      tempLebar += 1
    else: # Kalo gabisa pindah mundur sampai ada yg kosong (" ")
      while(True):  # Backtracking
        tempLebar, tempPanjang = neighbourKosong(tempLebar, tempPanjang)
        if maze[tempLebar][tempPanjang] == " ": # Jika ketemu yg kosong
          break
        else:
          if maze[tempLebar][tempPanjang-1] not in ["⛝", " "]: # Cek ke kiri ada angka atau tidak
            if maze[tempLebar][tempPanjang-1] < count:  # Jika angkanya lebih kecil dari count
              count = maze[tempLebar][tempPanjang]  # Nilai count diubah menjadi count index saat ini
              tempPanjang -= 1  # Pindah index ke kiri
              continue
          if maze[tempLebar-1][tempPanjang] not in ["⛝", " "]: # Cek ke atas ada angka atau tidak
            if maze[tempLebar-1][tempPanjang] < count:  # Jika angkanya lebih kecil dari count
              count = maze[tempLebar][tempPanjang]  # Nilai count diubah menjadi count index saat ini
              tempLebar -= 1  # Pindah index ke atas
              continue
          if maze[tempLebar+1][tempPanjang] not in ["⛝", " "]: # Cek ke bawah ada angka atau tidak
            if maze[tempLebar+1][tempPanjang] < count:  # Jika angkanya lebih kecil dari count
              count = maze[tempLebar][tempPanjang]  # Nilai count diubah menjadi count index saat ini
              tempLebar += 1  # Pindah index ke bawah
              continue
          if maze[tempLebar][tempPanjang+1] not in ["⛝", " "]: # Cek ke kanan ada angka atau tidak
            if maze[tempLebar][tempPanjang+1] < count:  # Jika angkanya lebih kecil dari count
              count = maze[tempLebar][tempPanjang]  # Nilai count diubah menjadi count index saat ini
              tempPanjang += 1  # Pindah index ke kanan

# Cetak maze
for i in range(lebar):
  for j in range(panjang):
    if len(str(maze[i][j])) == 1:
      if maze[i][j] == "⛝":
        print("\033[1;31m" + maze[i][j], end="  ")
      else:
        print("\033[0;37m" + str(maze[i][j]), end="  ")
    elif len(str(maze[i][j])) == 2:
      print("\033[0;37m" + str(maze[i][j]), end=" ")
    else:
      print("\033[0;37m" + str(maze[i][j]), end="")
  print()