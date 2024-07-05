import MathematicQuizGenerator

if __name__=="__main__":
    level = input("input level: ")
    print()

    match level:
        case "1":
            MathematicQuizGenerator.level01()
        case "2":
            MathematicQuizGenerator.level02()
        case "3":
            MathematicQuizGenerator.level03()
        case _:
            print("The level you entered was not found.")
