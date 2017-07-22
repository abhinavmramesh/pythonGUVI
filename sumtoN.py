def main():
   sum = 0
   num = int(raw_input("Enter the no: "))
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is " + str(sum))

if __name__ == '__main__':
  main()