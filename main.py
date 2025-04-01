ukoly = {}

def options():
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

def add_task():
    print("\nPřidání nového úkolu")
    name = str(input("Zadejte název úkolu: "))
    description = str(input("Zadejte popis úkolu: "))
    ukoly[name] = description
    print("\nÚkol " + name + " úspěšně přidán")
    return

def show_tasks():
    print("\nSeznam úkolů: ")

    if not ukoly:
        print("\nŽádné úkoly nejsou k dispozici.")
        return

    i = int(1)
    for x,y in ukoly.items():
        print(str(i) + ". " + x + " - " + y)
        i += i
    return

def delete_task():
    
    i = int(1)

    if not ukoly:
        print("\nŽádné úkoly nejsou k dispozici.")
        return

    print("\nVýpis úkolů:")
    for x,y in ukoly.items():
        print(str(i) + ". " + x + " - " + y)
        i += 1

    num = int(input("\nZadejte číslo úkolu, který chcete vymazat: "))
    keys = list(ukoly.keys())

    if 1 <= num <= len(keys):
        key_to_delete = keys[num - 1]
        del ukoly[key_to_delete]
        print("Úkol " + key_to_delete + " byl smazán.")
    else:
        print("Neplatná volba.")
    
    return 

def hlavni_menu():
    while True:
        options()

        try:
            num = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            print("Zadejte platné číslo")
            continue    

        if(num == 4):
            print("\nKonec programu")
            break
        elif(num == 1):
            add_task()
            continue
        elif(num == 2):
            show_tasks()
            continue
        elif(num == 3):
            delete_task()
            continue
        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    hlavni_menu()