def func(i, n):
    # Base Condition
    if i < 1:
        return

    print(i)

    # Recursive call with i decremented
    func(i - 1, n)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    func(n, n)