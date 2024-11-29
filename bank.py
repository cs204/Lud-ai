def main():
    greeting = input("Приветствие: ")
    value(greeting)

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("здравcтвуйте"):
       print("$0")
    elif greeting.startswith("з"):
       print("$20")
    else:
       print("100")

if __name__== "__main__":
    main()

