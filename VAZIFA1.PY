
def sanash():
    with open("main.txt", "r", encoding='utf-8') as file:
        read = file.read()
        a = read.split()
        x = 0
        for i in a:
            x += 1
    return x

print(sanash())
    
