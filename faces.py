def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    a = input()
    b = convert(a)
    print(b)

if __name__ == "__main__":
    main()
