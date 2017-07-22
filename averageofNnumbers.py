def main():
    arr = list()
    n = int(raw_input("How many to be added: "))
    
    for i in range(n):
        a = int(raw_input("Enter the numbers:"))
        arr.append(a)
    avg = sum(arr)/n
    print("Avg is " + str(avg))

if __name__ == '__main__':
  main()