def main():
    quantity = int(input('Enter the quantity of grades:'))
    grades = [int(input("Enter grade(0-100):")) for _ in range(quantity)]
    A = sum(G>=90 for G in grades)
    B = sum(75<=G<90 for G in grades)
    C = sum(60<=G< 75 for G in grades)
    D = sum(50<=G<60 for G in grades)
    F = sum(G<50 for G in grades)

    total = len(grades)

    print("A:", A, "({}%)".format(round(A/total *100) if total else 0))
    print("B:", B, "({}%)".format(round(B/total *100) if total else 0))
    print("C:", C, "({}%)".format(round(C/total *100) if total else 0))
    print("D:", D, "({}%)".format(round(D/total *100) if total else 0))
    print("F:", F, "({}%)".format(round(F/total *100) if total else 0))

if __name__ == "__main__":
    main()