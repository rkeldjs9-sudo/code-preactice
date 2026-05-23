height = float(input("키(cm): "))
weight = float(input("몸무게(kg): "))

bmi = weight / ((height / 100) ** 2)

print("BMI:", round(bmi, 2))

if bmi >= 25:
    print("비만")
elif bmi >= 23:
    print("과체중")
elif bmi >= 18.5:
    print("정상")
else:
    print("저체중")
