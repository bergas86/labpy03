def perulangan():

	print(" ")
	
	max=0
	while True:
		a=int(input("Masukkan Bilangan = "))
		if max < a:
			max = a
		if a==0:
			print(" ")
			print("Bilangan Terbesar = ",max)
			print(" ")
			print("~Terimakasih Sudah Menggunakan Program Ini~")
			print(" ")
			print("DILARANG KERAS MENG COPPY PROGRAM TANPA IZIN")
			print(" ")
			jawab = "ya"
			while jawab == "ya":
				jawab = input(" Ingin Mengulang Program Ini ? (ya/tidak) ")
				if jawab == "ya" :
					return perulangan()
				elif jawab == "tidak" :
					break
			print(" ")

perulangan()