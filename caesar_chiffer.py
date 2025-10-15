
def caesar_chiffer(text, nyckel):
    resultat = ""
    # Se till att nyckeln är inom 0-25 så att den fungerar korrekt
    nyckel = nyckel % 26
    
    for char in text:
        if 'A' <= char <= 'Z': 
            
            # Hitta position (0-25)
            nummer = ord(char) - ord('A')
            
            # Applicera chiffret (Shift + Modulo)
            nytt_nummer = (nummer + nyckel) % 26
            
            # Konvertera tillbaka till bokstav
            ny_char = chr(nytt_nummer + ord('A'))
            resultat += ny_char
            
        elif 'a' <= char <= 'z': # Små bokstäver
            nummer = ord(char) - ord('a')
            nytt_nummer = (nummer + nyckel) % 26
            ny_char = chr(nytt_nummer + ord('a'))
            resultat += ny_char
        
        else: # Icke-bokstäver (mellanslag, siffror, etc.)
            resultat += char
            
    return resultat


def brute_force_caesar(chiffertext):
    print("\n--- Startar Brute-Force Attack ---")
    
    # testar alla möjliga krypteringsnycklar N (1 till 25)
    for N in range(1, 27):
        
        # Beräkna dekrypteringsnyckeln D
        # D = 26 - N ger oss det skift framåt som motsvarar N steg bakåt.
        D = 26 - N
        
        # Använd caesar_chiffer-funktionen för att dekryptera
        mojlig_klartext = caesar_chiffer(chiffertext, D)
        
        # Skriv ut nyckeln och den möjliga klartexten
        print(f"Nyckel {N}: {mojlig_klartext}")
        

num_for_a = ord('A')
text = "I feel stupid"

#krypterade text
test1 = caesar_chiffer(text, 8)

print(num_for_a)
print(test1)

#skickar in krypterad text och dekrypterar med brute force
brute_force_caesar(test1)