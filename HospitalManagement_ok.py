class hospital:
    name=""
    age=""
    phno=""
    add=""
    bloodgrp=""
    weight=""
    height=""
    adhar=""
    fever=""
    id="RR"
    pswd="1234"
    id1=""
    pswd1=""
    hemo=""
    CTscan=""
    Xray=""
    Sonography=""
    MRI=""
    
    def reg(self):
        print("*********Registration***********")
        
        self.name=input("Enter Patients Name: ")
        self.age=input("Enter Patients Age: ")
        self.phno=input("Enter Patients Phone Number: ")
        self.add=input("Enter Patients Address: ")
        self.bloodgrp=input("Enter Patients Blood Group: ")
        self.weight=input("Enter Patients Weight: ")
        self.height=input("Enter Patients Height: ")
        self.adhar=input("Enter Patients Adhar Card Number: ")
        self.fever = input("Enter disease:")

        
        print("====================Patients Details====================")
        print("+++++++++++++++Hospital Name: Noble Hospital++++++++++++++++++")
        print("Patients Name: ",self.name)
        print("Patients Age: ",self.age)
        print("Patients Phone Number: ",self.phno)
        print("Patients Address: ",self.add)
        print("Patients Blood Group: ",self.bloodgrp)
        print("Patients Weight: ",self.weight)
        print("Patients Height: ",self.height)
        print("Patients Adhar card number: ",self.adhar)
        
    def appo(self):
        print("""==============Appointment fixed=============== 
              date: 19 Dec 2023
              time: 12: 00
              doctor name: Vaibhav
              Appointment confirmed"""
              )
          
    def rec(self):
        print("==============Medical Record===============")
        
        self.hemo=input("Hemoglobin Report: ")
        self.CTscan=input("CT Scan Report: ")
        self.Xray=input("Xray Report: ")
        self.Sonography=input("Sonography Report: ")
        self.MRI=input("MRI Report: ")
        
        print("++++++Medical Reports given by Patient+++++++")
        print("Hospital Name: Noble Hospital")
        print("Doctor Assigned: Vaibhav")
        print("Patients Name: ", self.name)
        print("Patients Phone Number: ", self.phno)
        print("Patients Address: ", self.add)
        print("Patient Disease: ",self.fever)
        print("Patients Hemoglobin Report: ",self.hemo)
        print("Patients CT Scan Report: ",self.CTscan)
        print("Patient Xray Report: ",self.Xray)
        print("Patient Sonography Report: ",self.Sonography)
        print("Patient MRI Report: ",self.MRI)
        
              
    def con(self):
        print("==========Concultancy===========")
        print("Hospital Name: Noble Hospital")
        print("Doctor Assigned: Vaibhav")
        print("Patients Name: ",self.name)
        print("Medicine to be taken: Crocin, Azee 500")
        print("Fees = 500")
        
    def login(self):

        self.id1=input("Enter Your ID: ")
        self.pswd1=input("Enter Your Password: ")
        self.main()

    def main(self):
        if self.id==self.id1 and self.pswd==self.pswd1:
            print("""
                  1. Registration
                  2. Appointment
                  3. Medical Record
                  4. Concultancy
                  5. Exit""")
            a=int(input("Enter Your Choice: "))
        else:
            print("Invalid User")
            
        if a==1:
            self.reg()
            self.main()
        elif a==2:
            self.appo()
            self.main()
        elif a==3:
            self.rec()
            self.main()
        elif a==4:
            self.con()
            self.main()
        elif a==5:
            print("Exit")
        else:
            print("""
                  Invalid Choice...........Select Again""")
            self.main()      
            
            
obj=hospital()
obj.login()            
            