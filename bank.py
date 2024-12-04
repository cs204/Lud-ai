def main():
    greeting = input("Приветствие: ")
    value(greeting)

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("здравствуйте"):
       return 0
    elif greeting.startswith("з"):
       return 20
    else:
       return 100

if __name__== "__main__":
    main()

