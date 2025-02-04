p = 'Kalkulator IMT'.center(30, '-')
print(p)

beratBadan = float(input('masukkan berat badan (kg) : '))
tinggiBadan = float(input('masukkan tinggi badan (cm) : '))
hasil = beratBadan / (tinggiBadan * tinggiBadan)
print(hasil)

if hasil <= 17.0:
    print('Kategori : Kurus ringan')
    
elif hasil <= 18.4:
    print('Kategori : Kurus berat')
    
elif hasil  <= 25.0:
    print('Kategori : Normal')
    
elif hasil <= 27.0:
    print('Kategori : Gemuk ringan')
    
elif hasil >= 27:
    print('Kategori : Gemuk berat')