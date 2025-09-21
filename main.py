def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # BMI hisoblash
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Past vazn"
    elif 18.5 <= bmi <= 24.9:
        return "Normal vazn"
    elif 25 <= bmi <= 29.9:
        return "Ortiqcha vazn"
    else:
        return "Semizlik"

def main():
    # Foydalanuvchidan ma'lumotlarni olish
    weight = float(input("Og'irlikni kiriting (kg): "))
    height = float(input("Boyni kiriting (metr): "))
    
    # BMI hisoblash
    bmi = calculate_bmi(weight, height)
    
    # Natijani chop etish
    print(f"Sizning BMI: {bmi:.2f}")
    print(f"Vazn turingiz: {categorize_bmi(bmi)}")

# Dastur ishga tushishi
if __name__ == "__main__":
    main()
