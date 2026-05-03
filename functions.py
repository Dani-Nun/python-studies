def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = 70
height = 1.75

bmi = calculate_bmi(weight, height)
classification = classify_bmi(bmi)

print(f"Weight: {weight}kg")
print(f"Height: {height}m")
print(f"BMI: {bmi:.1f}")
print(f"Classification: {classification}")