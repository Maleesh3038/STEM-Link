test_score = int(input("Enter the test score(1-100): "))

if 90 <= test_score <= 100:
    print("Test Score is A")

elif 80 <= test_score <= 89:
    print("Test Score is B")

elif 70 <= test_score <= 79:
    print("Test Score is C")

elif 60 <= test_score <= 69:
    print("Test Score is D")

else:
    print("Test Score is F")
    