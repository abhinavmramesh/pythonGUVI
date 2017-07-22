def main():
   
   n = int(input("Enter the days: "))
   a = n/365
   b = n%365
   c = b/30
   d = n-(c*30)-(a*365)
   
   print("Years:" + str(a))
   print("Months:" + str(c))
   print("Days:" + str(d))
   
if __name__ == '__main__':
  main()
