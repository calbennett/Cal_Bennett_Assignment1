#echo.py
def echo(text: str, repititions : int = 3):
    while repititions >= 1:
        print(text[repititions * -1:])
        repititions -= 1
    return(".")
    
if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

    