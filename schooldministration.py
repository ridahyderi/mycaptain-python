#basic school administation
import csv

def write_into_csv(info_list):
    with open ('student_info.csv','a', newline=' ') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.row(["Name","Age","Contact Number","E-mail ID"])
        writer.writerow(info_list)
if __name__=='__main__':
    condition=True
    student_num=1
    while(condition):
        student_info=input("Enter Student Information for student #{} in the following format (Name, Age, Contact Number, Email ID):".format(student_num))

        student_info_list=student_info.split(',')
        
        
        print("\nThe entered information is:\nName: {}\nAge: {}\nCOntact Number: {}\n E-mail ID: {}"
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        write_into_csv(student_info_list)
    
        choice=input("Is the entered information correct? (yes/no):")   
        
        if choice=="yes":
            write_into_csv(student_info_list)
            
            condition_check=input("Enter (yes/no) if you want to enter information for another student:")
            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            elif condition_check=="no":
                condition=False
    
        elif choice=="no":
            print("Please re-enter the values")
        