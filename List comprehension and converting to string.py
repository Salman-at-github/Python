brand = ['nokia', 'samsung', 'moto', 'oppo', 'vivo']
storage = ['32GB', '64GB', '128GB', '256GB', '512GB']
randomaccess = ['1GB', '2GB', '4GB', '6GB', '8GB']
variant = [[name, ram, rom]
           for name in brand for ram in randomaccess for rom in storage]
print(variant)
print(len(variant))

strings = '' #to convert the list into string
for i in variant:
    for j in i:
        strings += j+' '
print(strings)
