def generator(atas=1, bawah=51):
    for i in range(bawah):
        if i%2 != 0:
            yield i

gen = generator()
print(type(gen))
for i in gen:
    print(i, end=',')
        