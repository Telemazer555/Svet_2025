def multiply():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'  {i * j:2}', end=" ")
        print()
if __name__ == '__main__':
    multiply()
