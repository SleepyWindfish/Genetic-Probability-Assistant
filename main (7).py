from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Genetic Probability Generator")
root.configure(bg='lemon chiffon')

def info(type):
  if(type=='Si'):
    messagebox.showinfo("Sickle Cell","Sickle Cell anemia is a disease in which the cell is contorted into a Sickle like shape. Your cells die more early and you often feel more fatigue then others.")
  if(type=='Bl'):
    messagebox.showinfo("Color Blind","Color Blindness is a condition that is often inherited. If you are Color Blind you are often unable to distinguish between different colors.(Most commonly Red and Green)")
  if(type=='Ta'):
    messagebox.showinfo("Blood-Type","Every Person has a blood type that falls into the A,B,AB,or O catagory with (+) or (-). Using this information the program can identify whether you are adopted and calcuate all your possible blood types. Additionaly the Program will tell who you can receive blood from.")
  if(type=='Tr'):
    messagebox.showinfo("Genetic Tree","Here the program will create your Genetic tree otherwise known as a Pedigree. It will show previous Generations and how you may have inherited a trait or diesease. ")

def Sickle_Probability(dad_positive,mom_positive,dad_trait_positive,mom_trait_positive):
  Punnet_Squares=["1-father","1-mother","2-father",'2-mother','3-father',"3-mother","4-father","4-mother"]
  chance=0
  spacing1=Label(root,text="",bg='lemon chiffon')
  spacing2=Label(root,text="",bg='lemon chiffon')
  Dad_Label=Label(root,text="Dad Allel 1",width=5,bg='royal blue')
  Dad_Label_2=Label(root,text="Dad Allel 2",width=5,bg='royal blue')
  Mom_Label=Label(root,text="Mom Allel 1",width=5,bg='royal blue')
  Mom_Label_2=Label(root,text="Mom Allel 2",width=5,bg='royal blue')
  
  
  if(dad_positive=="Yes"):
    Dad_Allel_1=Label(root,text='s',width=5)
    Punnet_Squares[0]='s'
    Punnet_Squares[2]='s'
    Dad_Allel_2=Label(root,text='s',width=5)
    Punnet_Squares[4]='s'
    Punnet_Squares[6]='s'
  if(mom_positive=="Yes"):
    Mom_Allel_1=Label(root,text='s',width=5)
    Punnet_Squares[1]='s'
    Punnet_Squares[5]='s'
    Mom_Allel_2=Label(root,text='s',width=5)
    Punnet_Squares[3]='s'
    Punnet_Squares[7]='s'
  if(dad_positive=="No" and dad_trait_positive=="Yes"):
    Dad_Allel_1=Label(root,text='N',width=5)
    Punnet_Squares[0]='N'
    Punnet_Squares[2]='N'
    Dad_Allel_2=Label(root,text='s',width=5)
    Punnet_Squares[4]='s'
    Punnet_Squares[6]='s'
  if(mom_positive=="No" and mom_trait_positive=="Yes"):
    Mom_Allel_1=Label(root,text='N',width=5)
    Punnet_Squares[1]='N'
    Punnet_Squares[5]='N'
    Mom_Allel_2=Label(root,text='s',width=5)
    Punnet_Squares[3]='s'
    Punnet_Squares[7]='s'
  if(dad_positive=="No" and dad_trait_positive=="No"):
    Dad_Allel_1=Label(root,text='N',width=5)
    Punnet_Squares[0]='N'
    Punnet_Squares[2]='N'
    Dad_Allel_2=Label(root,text='N',width=5)
    Punnet_Squares[4]='N'
    Punnet_Squares[6]='N'
  if(mom_positive=="No" and mom_trait_positive=="No"):
    Mom_Allel_1=Label(root,text='N',width=5)
    Punnet_Squares[1]='N'
    Punnet_Squares[5]='N'
    Mom_Allel_2=Label(root,text='N',width=5)
    Punnet_Squares[3]='N'
    Punnet_Squares[7]='N'
  if(Punnet_Squares[5]!='N' and Punnet_Squares[5]!='s'):
    messagebox.showerror("Invalid","You have made a spelling mistake or entered a impossible situation please reevaluate your responses.")
  
  Square_1=Button(root,text=Punnet_Squares[0]+Punnet_Squares[1],width=5,bg="SkyBlue2")
  Square_2=Button(root,text=Punnet_Squares[2]+Punnet_Squares[3],width=5,bg="SkyBlue2")
  Square_3=Button(root,text=Punnet_Squares[4]+Punnet_Squares[5],width=5,bg="SkyBlue2")
  Square_4=Button(root,text=Punnet_Squares[6]+Punnet_Squares[7],width=5,bg="SkyBlue2")

  for i in range(0,8,2):
    if(Punnet_Squares[i]=='s' and Punnet_Squares[i+1]=='s'):
      chance=chance+25
  chance=str(chance)    
  inherited=Label(root,text="You have a "+chance+"%"+" of inheriting Sickle cell anemia.",bg="chocolate1")  
      
  
  spacing1.grid(row=7,column=1)
  spacing2.grid(row=8,column=1)
  Dad_Label.grid(row=9,column=3,sticky='nsew')
  Dad_Allel_1.grid(row=10,column=3,sticky='nsew')
  Dad_Label_2.grid(row=9,column=4,sticky='nsew')
  Dad_Allel_2.grid(row=10,column=4,sticky='nsew')
  Mom_Label.grid(row=11,column=1,sticky='nsew')
  Mom_Allel_1.grid(row=11,column=2,sticky='nsew')
  Mom_Label_2.grid(row=12,column=1,sticky='nsew')
  Mom_Allel_2.grid(row=12,column=2,sticky='nsew')
  Square_1.grid(row=11,column=3,sticky='nsew')
  Square_2.grid(row=12,column=3,sticky='nsew')
  Square_3.grid(row=11,column=4,sticky='nsew')
  Square_4.grid(row=12,column=4,sticky='nsew')
  inherited.grid(row=13,column=1)
  

def Blood_Probability(dad_blood,mom_blood,child_blood):
  Possibilities=[]
  combine=0
  AB_is_present=False
  sign='none'
  spacing1=Label(root,text="",bg='lemon chiffon')
  spacing2=Label(root,text="",bg='lemon chiffon')
  Dad_Label=Label(root,text="Dad Allel 1",width=5,bg='royal blue')
  Mom_Label=Label(root,text="Mom Allel 1",width=5,bg='royal blue')
   
  if(len(dad_blood)==3):
    if(str(dad_blood[2])=="+"):
      sign="+"
    else:
      sign="-"
    Dad_Allel_1=Label(root,text=dad_blood,width=5)
    Possibilities.append(dad_blood[0]+sign)
    Possibilities.append(dad_blood[1]+sign)
    AB_is_present=True
  
  if(len(dad_blood)==2):
    if(str(dad_blood[1])=="+"):
      sign="+"
    else:
      sign="-"
    Dad_Allel_1=Label(root,text=dad_blood[0]+sign,width=5)
    Possibilities.append(dad_blood[0]+sign)
    combine=combine+1
  
  if(len(mom_blood)==3):
    if(str(mom_blood[2])=="+"):
      sign="+"
    else:
      sign="-"
    Mom_Allel_1=Label(root,text=mom_blood,width=5)
    Possibilities.append(mom_blood[0]+sign)
    Possibilities.append(mom_blood[1]+sign)
    AB_is_present=True
    
    
  if(len(mom_blood)==2):
    if(str(mom_blood[1])=="+"):
      sign="+"
    else:
      sign="-"
    Mom_Allel_1=Label(root,text=mom_blood[0]+sign,width=5)
    Possibilities.append(mom_blood[0]+sign)
    combine=combine+1
  
  if(len(dad_blood)>3 or len(mom_blood)>3 or len(child_blood)>3):
    messagebox.showerror("Invalid","You Entered a inccorect Response. Please choose (A[+/-],B[+/-],AB[+/-],O[+/-]) for a blood type")
  if(combine>1 and mom_blood[0]!=dad_blood[0]):
    if("O+" not in Possibilities):
      if("O-" not in Possibilities):
        Possibilities.append("AB+")
        Possibilities.append("AB-")
        
  if("A+" or "A-" or "B+" or "B-" in Possibilities):
    if(AB_is_present==True):
      Possibilities.append("AB+")
      Possibilities.append("AB-")
      
  if(mom_blood!="O+" and mom_blood!="O-" or dad_blood!="O+" and dad_blood!="O-"):
    if(AB_is_present==True):
      Possibilities.append("A+")
      Possibilities.append("A-")
      Possibilities.append("B+")
      Possibilities.append("B-")
  
  if('AB+' or 'AB-' or 'O+' or 'O-' not in Possibilities):
    if(AB_is_present==False):
      Possibilities.append("O+")
      Possibilities.append("O-")
  if(dad_blood=='AB+' or dad_blood=="AB-"):
    if(mom_blood=="O+" or mom_blood=="O-"):
      Possibilities=["A+","B+","A-","B-"]
  if(dad_blood=='O+' or dad_blood=="O-"):
    if(mom_blood=="AB+" or mom_blood=="AB-"):
      Possibilities=["A+","B+","A-","B-"]
    
    
  New_Possibilities=[]
  for filter in Possibilities:
    if(filter not in New_Possibilities):
      New_Possibilities.append(filter)
  
  
  Square_1=Button(root,text="Possible Blood Types: "+str(New_Possibilities),width=5,bg="SkyBlue2")
  
  if (child_blood in New_Possibilities):
      inherited=Label(root,text="You Have a Blood Type of "+child_blood+" Which Matches With the Possible Outcomes for Your Parents. You are Most likely not Adopted",bg="chocolate1")
  else:
    inherited=Label(root,text="Your Blood Type "+child_blood+" Does Not Match with Any Possible Outcomes For Your Parents. You Are Adopted",bg="chocolate1")

  
  if(child_blood=="AB+"):
    donation=Label(root,text="You can Recive Blood From Anyone!")
  elif(child_blood=="AB-"):
    donation=Label(root,text="You can Recive Blood From: AB-,A-,B-,O-")
  elif(child_blood=="B-"):
    donation=Label(root,text="You can Recive Blood From: B-,O-")
  elif(child_blood=="A-"):
    donation=Label(root,text="You can Recive Blood From: A-,O-")
  elif(child_blood=='O-'):
    donation=Label(root,text="You can Recive Blood From: O-")
  elif(child_blood=="B+"):
    donation=Label(root,text="You can Recive Blood From: B+,B-,O+,O-")
  elif(child_blood=="O+"):
    donation=Label(root,text="You can Recive Blood From: O+,O-")
  elif(child_blood=="A+"):
    donation=Label(root,text="You can Recive Blood From: A+,A-,O+,O-")


  spacing1.grid(row=7,column=1)
  spacing2.grid(row=8,column=1)
  Dad_Label.grid(row=9,column=3,sticky='nsew')
  Dad_Allel_1.grid(row=10,column=3,sticky='nsew')
  Mom_Label.grid(row=11,column=1,sticky='nsew')
  Mom_Allel_1.grid(row=11,column=2,sticky='nsew')
  Square_1.grid(row=11,column=3,sticky='nsew')
  inherited.grid(row=12,column=1)
  donation.grid(row=13,column=1)
    
  #USE A FORLOOP TO PRINT ALL OF THE ITEMS IN THE LIST
  
  
  




def Sickle_Form():
  prompt=Label(root,text="For each of the following Respond with a Yes or No. Capitilization Matters!",bg="slate gray")
  dad=Label(root,text="Does your Dad have sickle cell anemia?",bg="PaleGreen2")
  dad_response=Entry(bg="OliveDrab2")
  dad_trait=Label(root,text="Does your dad carry a allel of sickle cell anemia?",bg="sea green")
  dad_trait_response=Entry(bg="OliveDrab2")
  mom=Label(root,text="Does your Mom have sickle cell anemia?",bg="PaleGreen2")
  mom_response=Entry(bg="OliveDrab2")
  mom_trait=Label(root,text="Does your Mom carry a allel of sickle cell anemia?",bg="sea green")
  mom_trait_response=Entry(bg="OliveDrab2")
  start=Button(root,text="Ready",bg="orange red",activebackground="indian red",command=lambda: Sickle_Probability(str(dad_response.get()),str(mom_response.get()),str(dad_trait_response.get()),str(mom_trait_response.get())))
  
  prompt.grid(row=1,column=3)
  dad.grid(row=2,column=1)
  dad_response.grid(row=2,column=2)
  dad_trait.grid(row=3,column=1)
  dad_trait_response.grid(row=3,column=2)
  mom.grid(row=4,column=1)
  mom_response.grid(row=4,column=2)
  mom_trait.grid(row=5,column=1)
  mom_trait_response.grid(row=5,column=2)
  start.grid(row=6,column=1)
  
  
  
def Blood_Form():
  prompt=Label(root,text="For each of the following Respond with the letters (A[+/-],B[+/-],AB[+/-],O[+/-]). Choose One Sign For Each Option!",bg="slate gray")
  dad=Label(root,text="Enter the Blood type of your Dad:",bg="PaleGreen2")
  dad_response=Entry(bg="OliveDrab2")
  mom=Label(root,text="Enter the Blood type of your Mom:",bg="PaleGreen2")
  mom_response=Entry(bg="OliveDrab2")
  child=Label(root,text="Enter the Blood type you have:",bg="PaleGreen2")
  child_response=Entry(bg="OliveDrab2")
  start=Button(root,text="Ready",bg="orange red",activebackground="indian red",command=lambda: Blood_Probability(str(dad_response.get()),str(mom_response.get()),str(child_response.get())))  

  prompt.grid(row=1,column=3)
  dad.grid(row=2,column=1)
  dad_response.grid(row=2,column=2)
  mom.grid(row=3,column=1)
  mom_response.grid(row=3,column=2)
  child.grid(row=4,column=1)
  child_response.grid(row=4,column=2)
  start.grid(row=5,column=1)
  



    

def clear(gateway):
  Menu.destroy()
  Sickle.destroy()
  Sickle_info.destroy()
  Blind.destroy()
  Blind_info.destroy()
  Taste.destroy()
  Taste_info.destroy()
  Tree.destroy()
  Tree_info.destroy()
  if(gateway=='Si'):
    Sickle_Form()
  elif(gateway=='Bl'):
    messagebox.showinfo("Unavalible","This mode is currently unavalible")
  elif(gateway=='Ta'):
    Blood_Form()
  elif(gateway=='Tr'):
    messagebox.showinfo("Unavalible","This mode is currently unavalible")
    

Menu=Label(root,text="Medical Patient Menu ",bg='snow')

Sickle=Button(root,text="Check for Sickle Cell Anemia",bg='SlateBlue2',activebackground='LightBlue3',height=2,width=20,command=lambda: clear('Si'))

Sickle_info=Button(root,text="Info",bg='khaki2',command=lambda: info('Si'))

Blind=Button(root,text="Check for Color Blindness",bg='SlateBlue2',activebackground='LightBlue3',height=2,width=20,command=lambda: clear('Bl'))

Blind_info=Button(root,text="Info",bg='khaki2',command=lambda: info('Bl'))

Taste=Button(root,text="Check If I Am Secretly Adopted",bg='SlateBlue2',activebackground='LightBlue3',height=2,width=23,command=lambda: clear('Ta'))

Taste_info=Button(root,text="Info",bg='khaki2',command=lambda: info('Ta'))

Tree=Button(root,text="My Genetic Tree",bg='SlateBlue2',activebackground='LightBlue3',height=2,width=20,command=lambda: clear('Tr'))

Tree_info=Button(root,text="Info",bg='khaki2',command=lambda: info('Tr'))




Menu.grid(row=1,column=3)
Sickle.grid(row=2,column=1)
Sickle_info.grid(row=2,column=2)
Blind.grid(row=3,column=1)
Blind_info.grid(row=3,column=2)
Taste.grid(row=4,column=1)
Taste_info.grid(row=4,column=2)
Tree.grid(row=5,column=1)
Tree_info.grid(row=5,column=2)


root.mainloop()
#User input Dog name
#Dog species 

#Mabye human inherited dieseas medical analysis cheacker using the a pedigree drawing and mabye graph?

#First asks user for thier basic medical history and phenotypes(phisical features)
#next thier is a User_menue in which the user can choose what to do. one option could be called family tree showin a pedigree. Sickle cell amenia and color blindness,able to tasete PTS testing

#Add a DNA background
