imt = float(input())/float(input())**2
print(int(imt>25), int(imt<18.5))
print(('Оптимальная', 'Избыточная', 'Недостаточная')[(imt>25)-(imt<18.5)], 'масса')
