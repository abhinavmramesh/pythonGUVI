    
def main():
   ad = 0
   num = int(input("Enter the no: "))
   
   for i in range(1,num):
       if num%2!=0:
           ad += i
       
       
   print("The sum is " + str(ad))
   
if __name__ == '__main__':
  main()
