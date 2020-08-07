import datetime

print('Toto je program pro vypocet doby stahovani')
print('Chces pokracovat dale??(y/n)')
canContinue = input()

if canContinue == 'y':
    print('Ok, zadej rychlost internetu v Mb/s')
    inetSpeed = input()

    print('Super, ted zadej velikost dat k prenosu MB')
    fileSize = input()
    time = int(fileSize) / (int(inetSpeed) / 8)
    sec = time
    conversion =  datetime.timedelta(seconds =sec)

    print('ok takze rychlost je ' + str(inetSpeed) + 'Mb/s a velikost dat k prenosu je ' + str(fileSize) + 'MB')

    print('Soubor budes stahovat ' + str(conversion) + 's')
