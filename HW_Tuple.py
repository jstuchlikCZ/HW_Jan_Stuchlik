"""
Task 3
Create an app Company. Store the following information about a person:
 full name, phone number, corporate email, job title, room number, skype.
 Provide the possibility to add, delete, search, and replace data.
 Use a dictionary to store information.
"""
company = {}

# přidání zaměstnance
def add_person():
    full_name = input("Zadejte jméno a příjmení: ")
    phone = input("Zadejte telefoní číslo: ")
    email = input("Zadejte služební email: ")
    job_title = input("Zadejte pracovní pozici: ")
    room_number = input("Zadejte číslo pokoje: ")
    company[full_name] = {
        "Phone": phone,
        "Email": email,
        "Job Title": job_title,
        "Room Number": room_number,

    }
    print(f"{full_name} added successfully!")

# smazání
def delete_person():
    full_name = input("Zadejte jméno a příjmení pro smazání záznamu: ")
    if full_name in company:
        del company[full_name]
        print(f"{full_name} úspěšně vymazán!")
    else:
        print("Zaměstnanec neexistuje.")

# vyhledání v seznamu
def search_person():
    full_name = input("Zadejte jméno a příjmení pro vyhledání zaměstnance: ")
    if full_name in company:
        print("Záznam zaměstnance:")
        for key, value in company[full_name].items():
            print(f"{key}: {value}")
    else:
        print("Zaměstnanec neexistuje.")

# Editovat zaměstannce
def replace_person():
    full_name = input("Zadejte jméno a příjmení pro editaci: ")
    if full_name in company:
        print("Co chcete upravit?")
        print("Options: Telefone, Email, Pracovní pozice, Číslo pokoje")
        field = input("Enter the field to update: ").title()
        if field in company[full_name]:
            new_value = input(f"Zadejte novou hodnotu {field}: ")
            company[full_name][field] = new_value
            print(f"{field} úspěšně upraveno!")
        else:
            print("Neexistující pole.")
    else:
        print("Zaměstnanec neexistuje.")

# Smyčka while pro ukončení aplikace uživatelem a volbu uživatele
while True:
    print("\nAplikace pro správu zaměstnanců")
    print("1. Přidat zaměstance")
    print("2. Odstranit zaměstance")
    print("3. Vyhledat zaměstnance")
    print("4. Upravit údaje zaměstnance")
    print("5. Zavřít aplikaci")
    choice = input("Zadejte Volbu: ")

    if choice == "1":
        add_person()
    elif choice == "2":1
        delete_person()
    elif choice == "3":
        search_person()
    elif choice == "4":
        replace_person()
    elif choice == "5":
        print("Aplikace bude ukončena.")
        break
    else:
        print("Volba není na seznamu.")