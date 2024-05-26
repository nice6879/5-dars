

def eng_uzun_soz(filename):
    
        with open(filename, "r", encoding='utf-8') as file:
            read = file.read()
            a = read.split()
            if not a:
                return "Faylda so'zlar yo'q."
            eng_uzun = max(a, key=len)
            return eng_uzun
filename = 'main.txt'
eng_uzun_soz = eng_uzun_soz(filename)
print(f"eng uzun soz: {eng_uzun_soz}")
