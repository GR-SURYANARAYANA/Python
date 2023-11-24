import random
from PythonProject import Form
from PythonProject.Text import Style

style = Style()


class Owner:
    survey_list = {}
    people = []

    # def __init__(self):
        # print("*" * 50)
        # print("|" + "Welcome Owner Create Your Account".center(48) + "|")
        # print("*" * 50)
        # name = input("What's your name ? ".ljust(20) + ":")
        # code = input("Enter security code ? ".ljust(20))
        # self.name = name
        # self.code = code
        # self.password = self.__password_manager()
        # print("Account created Successfully...!")

    def __password_manager(self, msg=""):
        password = input(f"Enter your {msg} password ?".ljust(20) + ":")
        while True:
            confirm_password = input("Confirm your password?".ljust(20) + ":")
            security_code = input("Confirm Your Security Code ".ljust(20) + ":")
            if password == confirm_password and security_code == self.code:
                break
            else:
                print("Invalid password or Security code Please Try Again...!")
        return password

    def forget_password(self):
        print("*" * 50)
        print("|" + f"Recover {self.name} Account's Password ".center(48) + "|")
        print("*" * 50)
        code = input("Enter the Security Pin to Recover Your Password : ".ljust(20) + ":")
        while code != self.code:
            print("Invalid Code..! ")
            code = input("Enter the Security Pin to Recover Your Password : ".ljust(20) + ":")

        else:
            self.__password_manager()
        print("Password Recovered Successfully...!")

    def change_password(self):
        print("*" * 50)
        print("|" + f"Change {self.name} Account's Password ".center(48) + "|")
        print("*" * 50)
        self.__password_manager("new")
        print("Password changed Successfully...!")

    def __survey_mode(self, ls):
        print("*" * 50)
        print("|" + "Welcome to User Survey Mode : ".center(48) + "|")
        print("*" * 50)
        count = 0
        for i in self.survey_list.keys():
            ls += [self.survey_list[i]]
            count += 1
            print(f"{count}. {self.survey_list[i].title}")
        ch = input("Enter the choice to survey :  ")
        if ch.upper() == "EXIT":
            return "Exit"
        else:
            try:
                ch = int(ch)
            except Exception:
                print("Invalid Choice...!")
        while len(self.survey_list) <= ch < 0:
            print("Invalid Choice...! Please Try Valid one Again...! ")
            ch = int(input("Enter the choice to survey :  "))
        ls[ch - 1].get_feedback()
        return "Not Exit"

    def owner_play(self):
        while True:
            ls = []
            print("*"*50)
            print("*"*50)
            print("1.Create Feedback Form", "2.Update Survey Question", "3.Survey Mode", "4.Get Responses",
                  "5.Analyse Feedback Form", "6.Get Feedback ID's ", "7.Exit", sep='\n')
            print("*"*50)
            choice = int(input("Enter the choice : "))
            print("*"*50)
            match choice:
                case 1:
                    while True:
                        generate_id = random.randint(1000, 9999)
                        if generate_id not in self.survey_list:
                            break
                    template = Form()
                    template.create_form(generate_id)
                    self.survey_list[generate_id] = template
                case 2:
                    feedback_id = int(input("Enter the Feedback id to perform "))
                    if feedback_id in self.survey_list:
                        # template = survey_list[feedback_id]
                        # print(template.get_question)
                        # template.update_question()
                        while True:
                            print("-" * 50)
                            print("|"+f"{style.bold_start()}Welcome To Form Update Mode{style.bold_end()}".center(48)+"|")
                            print("|"+f"{style.italic_start()}Feedback ID : {feedback_id}{style.italic_end()}".center(48)+"|")
                            print("-" * 50)
                            ch = input("1. To Add question to Form\n2.To remove question from Form\n3.To Update The Form\n4.Exit Update\nEnter the choice : ")
                            match ch:
                                case "1":
                                    self.survey_list[feedback_id].add_question()
                                case "2":
                                    self.survey_list[feedback_id].remove_question()
                                case "3":
                                    self.survey_list[feedback_id].update_question()
                                case "4":
                                    break
                                case _:
                                    print("Invalid choice ")
                    else:
                        print("Invalid Survey ID ")
                case 3:
                    while True:
                        ch = self.__survey_mode(ls)
                        if ch.upper() == "EXIT":
                            break
                case 4:
                    feedback_id = int(input("Enter the Feedback id to perform "))
                    if feedback_id in self.survey_list:
                        self.survey_list[feedback_id].get_responses()
                    else:
                        print("Invalid Survey ID ")
                case 6:
                    print("*" * 50)
                    print("|"+"Get feedback Id's".center(48)+"|")
                    print("*" * 50)
                    print()
                    for i in self.survey_list.keys():
                        print(f"{self.survey_list[i].title} ----> {i}")
                case 5:
                    feedback_id = int(input("Enter the Feedback id to perform "))
                    if feedback_id in self.survey_list:
                        print("*" * 50)
                        print("|" + "Welcome To Analysis Mode ".center(48) + "|")
                        print("*" * 50)
                        self.survey_list[feedback_id].form_analysis()
                    else:
                        print("Invalid Survey ID ")

                case 7:
                    return None

