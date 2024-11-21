import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    print("Do you have a school certificate? (No - 0, Yes - 1)")
    choose_certificate = input("Choose 0 or 1: ")
    certificate = choose_certificate == '1'

    ort_score = int(input("Enter your ORT score: "))

    print("1 - Beginner, 2 - Elementary, 3 - Pre-Intermediate, 4 - Intermediate, 5 - Upper-Intermediate, 6 - Advanced")
    choose_level = int(input("Choose level (1-6): "))
    english_levels = ["Beginner", "Elementary", "Pre-Intermediate", "Intermediate", "Upper-Intermediate", "Advanced"]
    english_level = english_levels[choose_level - 1]

    clear_screen()

    if not certificate:
        print("You cannot enroll in Ala-Too University.")
        return
    if ort_score < 110:
        print("You cannot enroll in Ala-Too University.")
        return
    if english_level not in ["Intermediate", "Upper-Intermediate", "Advanced"]:
        print("You are invited to a preparatory English course.")
        return

    print(f"Dear {first_name} {last_name}, congratulations! You are recommended for admission to Ala-Too University.")

    specialties = { 
        "Computer Engineering": 2500,
        "Artificial Intelligence": 2200,
        "Psychology": 1900,
        "Journalism": 1700,
        "International Relations": 2200,
        "Law": 1800,
        "Management": 2200,
        "Medicine": 3300
    }

    print("Choose your specialty:")
    for index, specialty in enumerate(specialties.keys()):
        print(f"{index + 1} - {specialty}: ${specialties[specialty]}")

    choose_specialty = int(input("Choose specialty (1-8): "))
    selected_specialty = list(specialties.keys())[choose_specialty - 1]
    tuition_fee = specialties[selected_specialty]

    discount = 0
    if 140 <= ort_score <= 155:
        discount = 0.05
    elif 156 <= ort_score <= 174:
        discount = 0.10
    elif 175 <= ort_score <= 199:
        discount = 0.25
    elif 200 <= ort_score <= 209:
        discount = 0.50
    elif 210 <= ort_score <= 218:
        discount = 0.75
    elif 219 <= ort_score <= 240:
        discount = 1.00

    final_tuition_fee = tuition_fee * (1 - discount)

    clear_screen()

    if discount > 0:
        print(f"Dear {first_name} {last_name}, we congratulate you! You have been admitted to the {selected_specialty} program at Ala-Too International University. The cost of your tuition with a {int(discount * 100)}% discount will be ${final_tuition_fee:.2f} per year.")
    else:
        print(f"Dear {first_name} {last_name}, we congratulate you! You have been admitted to the {selected_specialty} program at Ala-Too International University. The cost of your tuition will be ${tuition_fee} per year.")

if __name__ == "__main__":
    main()
