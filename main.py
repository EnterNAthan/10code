from hashlib import sha256
print("""

  $$\    $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$$\ 
$$$$ |  $$$ __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|
\_$$ |  $$$$\ $$ |$$ /  \__|$$ /  $$ |$$ |  $$ |$$ |      
  $$ |  $$\$$\$$ |$$ |      $$ |  $$ |$$ |  $$ |$$$$$\    
  $$ |  $$ \$$$$ |$$ |      $$ |  $$ |$$ |  $$ |$$  __|   
  $$ |  $$ |\$$$ |$$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |      
$$$$$$\ \$$$$$$  /\$$$$$$  | $$$$$$  |$$$$$$$  |$$$$$$$$\ 
\______| \______/  \______/  \______/ \_______/ \________|
                                            
""")

print("It's straightforward to use 10 CODE, a tool that simplifies the process of decrypting messages encrypted with XOR cipher.\n")


def Info():
    mode_entre = input("L'entrée est-elle un fichier ou le terminal ? F = Fichier ; T = Terminal : ")
    if mode_entre.upper() == 'F':
        entre = input("Entrez le nom du fichier à chiffrer : ")
    else:
        entre = None  # Aucun fichier à lire

    sortie = input("Entrez le nom du fichier final (laissez vide pour sortie terminal) : ")
    key = input("Entrez la clé de chiffrement : ")
    keys = sha256(key.encode('utf-8')).digest()
    return entre, sortie, keys, mode_entre

def encode(entre, sortie, keys, mode_entre):
    donnees = b""

    if mode_entre.upper() == 'F':
        with open(entre, 'rb') as f_entre:
            donnees = f_entre.read()
    else:
        donnees = input("Entrez le texte à chiffrer : ").encode('utf-8')

    result = b""
    for i, c in enumerate(donnees): 
        j = i % len(keys)
        result += bytes([c ^ keys[j]])

    if sortie:
        with open(sortie, 'wb') as f_sortie:
            f_sortie.write(result)
    else:
        print("Résultat : ", result)

def main():
    entre, sortie, keys, mode_entre = Info()
    encode(entre, sortie, keys, mode_entre)

main()
