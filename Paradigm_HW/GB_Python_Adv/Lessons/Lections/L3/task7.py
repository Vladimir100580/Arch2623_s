# Классы bytes и bytearray

text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))

text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))       # так выглядит "Привет, мир" при передачи в utf-8

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')    # изменяемый набор байтов (массив байтов)
print(f'{x = }\n{y = }')