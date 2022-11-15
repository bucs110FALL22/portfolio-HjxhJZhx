class StringUtility:
    strcount=[]
    vowels=0
    def __init__(self,mystring):
        self.mystring = str(mystring)

    def __str__(self):
        return self.mystring


    def locindex(self,n):

        self.n=self.mystring[n]
        return self.n
    def lenstr(self):
        
        return len(self.mystring)

    def strconcat(self):
  
        
        return " ".join([self.mystring]) 



   
    def vowels(self):


        for i in self.mystring:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                StringUtility.vowels += 1
                return print('this string has', StringUtility.vowels,' vowels')
            elif StringUtility > 5:
                return print('many')

            

    def bothEnds(self):
     

        if len(self.mystring)>2:
            return self.mystring[0:1]+self.mystring[-2:-1]
        elif len(self.mystring)<=2:
            return ""
            
            
            
        
    def fixStart(self):


        if not self.mystring: 
            return self.mystring
        else:
            return self.mystring[0] + self.mystring[1:].replace(s[0], '*')

    
    def asciiSum(self):
 
        return print(sum([ord(ele) - 96 for ele in self.mystring]))

       
    def cipher(self):

        cipher=""
        for i in self.mystring:
            if i.isalpha():
                alphabet = ord(i) + len(self.string)
                if alphabet > ord('z'):
                    alphabet-= 26
            letter = chr(alphabet)
            cipher += letter
        return cipher
    


                
                 
        
        
        

    
    

    
            
    