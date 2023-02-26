def move_it(fr, to):
    print(f"Move from {fr} to {to}")
    

def do_hannoi(n: int, to: int, fr: int, temp: int):
    if n == 0: return []
    do_hannoi(n-1, temp, fr, to)
    move_it(fr, to)
    do_hannoi(n-1, to, temp, fr)
    

def main():
    try:
        n = int(input("Enter the number of discs: "))
        do_hannoi(n, to=3, fr=1, temp=2)
    except ValueError:
        main()
    except RecursionError:
        main()


if __name__ == "__main__":
    main()
