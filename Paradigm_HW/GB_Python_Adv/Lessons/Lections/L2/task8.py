# задача

st = input("Введите текст: ")
if st.isdecimal():
    st = int(st)
    print(int(st), oct(st), bin(st), hex(st))
else:
    print('Текст должен быть числом')