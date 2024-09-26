alphabet = 'abcdefghijklmnopqrstuvwxyz'
direction=input("Encode or decode\n").lower()
text=input("Enter the text:\n").lower()
shift=int(input("Enter the amount to shift:\n"))

def caesercipher(encodeordecode,input,shift):
       cipher=""
       if encodeordecode=="decode":
           shift=shift*-1
    
       for a in input:
           i=alphabet.index(a)+shift
           cipher+=alphabet[i]
       print(cipher)
       
      
caesercipher(direction,text,shift)
cont = input("Do you want to continue (true or false)? ").lower()

# Continue as long as the user enters 'true'
while cont == 'true':
    direction = input("Encode or decode\n").lower()
    text = input("Enter the text:\n").lower()
    shift = int(input("Enter the amount to shift:\n"))
    
    # Call the Caesar cipher function again
    caesercipher(direction, text, shift)
    
    # Ask if they want to continue again
    cont = input("Do you want to continue (true or false)? ").lower()

     
     
