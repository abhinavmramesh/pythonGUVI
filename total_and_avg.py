def main():
    arr = list()
    n = int(raw_input("How many to be subjects: "))
    
    for i in range(1,n+1):
        a = int(raw_input("Marks of sub " + str(i)))
        arr.append(a)
    avg = sum(arr)/n
    print("Avg marks is " + str(avg))

if __name__ == '__main__':
  main()
    