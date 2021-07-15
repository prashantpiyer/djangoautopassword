from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def about(request):
    return render(request,'generator/about.html')

def home(request):
    return render(request,'generator/home.html')

def password(request):
    length=int(request.GET.get('length',12))
    def charactersGeneration(length):
          jj=[]
          listofsmallCharacters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
          listofbigCharacters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
          MixofUpperCase=listofsmallCharacters[0:length] + listofbigCharacters[0:length]
          random.shuffle(MixofUpperCase)
          result1 = MixofUpperCase[:len(listofsmallCharacters)]
          for value in range(1,length+1):
              jj.append(random.choice(result1))

          return jj
    def specialCharacters(length):
         new = []
         listOfSpecialCharacters=["@","_","!","#","$","%","^","&","*","()","<>","?","/","}","{","~",":"]
         for value in range(1,length+1):
             new.append(random.choice(listOfSpecialCharacters[0:length]))
         return new;

    def numbers(length):
           listOfNumbers=[];
           pp=[];
           juggledNumberPassword=[];
           for value in  (range(1,length+1)):
               listOfNumbers.append(value);
           for value in  (range(1,length+1)):
               pp.append(random.choice(listOfNumbers))
           return pp
    if request.GET.get('uppercase'):
        print("h1")
        if (request.GET.get('numbers')==None):
            parent_3=[]
        else:
         parent_3=numbers(length)    
        if (request.GET.get('special')==None):
            parent_1=[]
        else:
            parent_1=specialCharacters(length)
        parent_2=charactersGeneration(length)
        print(parent_3)
        print(parent_1)
        c =  parent_2 + parent_3 +parent_1
        random.shuffle(c)
        result = c[:len(parent_2)]
        listToStr = ''.join(map(str,result))
        thepassword=listToStr
 
  
     
    
    if request.GET.get('numbers'):
        print("h2")
        if (request.GET.get('uppercase')==None):
            parent_2=[]
        else:
            parent_2=charactersGeneration(length)
        if (request.GET.get('special')==None):
            parent_1=[]
        else:
            parent_1=specialCharacters(length)
        parent_3=numbers(length)
        
        

        c =  parent_2 + parent_3 +parent_1
        random.shuffle(c)
        result = c[:len(parent_3)]
        listToStr = ''.join(map(str,result))
        thepassword=listToStr
   
    

    if request.GET.get('special'):
        print(request.GET.get('special'))
        if (request.GET.get('uppercase')==None):
           parent_2=[]
        else:
          parent_2=charactersGeneration(length)
        if (request.GET.get('numbers')==None):
            parent_3=[]
        else:
            parent_3=numbers(length) 
  
        parent_1=specialCharacters(length)
         
        c =  parent_2 + parent_3 +parent_1
        random.shuffle(c)
        result = c[:len(parent_1)]
        listToStr = ''.join(map(str,result))
        thepassword=listToStr
   
    if request.GET.get('length'):
        if (request.GET.get('uppercase')==None)& (request.GET.get('numbers')==None)& (request.GET.get('special')==None):
            parent_2=charactersGeneration(length)
            parent_3=numbers(length) 
            parent_1=specialCharacters(length)
            c =  parent_2 + parent_3 +parent_1
            random.shuffle(c)
            result = c[:len(parent_1)]
            listToStr = ''.join(map(str,result))
            thepassword=listToStr
        # else:
        #   parent_2=charactersGeneration(length)
        # if (request.GET.get('numbers')==None):
        #     parent_3=[]
        # else:
        #     parent_3=numbers(length) 
        
        # if (request.GET.get('special')==None):
        #      parent_1=[]
        # else:
        #     parent_1=specialCharacters(length)
  




    
    return render(request,'generator/password.html',{'password':thepassword})