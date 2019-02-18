def perulangan():

	print(" ")
	
	import random
	a = 0
	jumlah = int(input("Masukkan Jumlah N : "))

	print(" ")

	for x in range(0,jumlah):
		i=random.uniform(0.0,0.5)
		a+=1
		print("data ke-",a,"=>",i)

	print(" ")
	print("Terimakasih Sudah Menggunakan Program Ini ")
	print(" ")
	print("DILARANG KERAS MENG COPPY PROGRAM TANPA IZIN")
	print(" ")
	
	jawab = "ya"
	hitung = 0
	while jawab == "ya":
		hitung += 1
		jawab = input("Ingin Mengulang Program Ini ? (ya/tidak) ")
		if jawab == "ya" :
			return perulangan()
		elif jawab == "tidak" :
			break
	print("Total perulangan : ",hitung)

perulangan()