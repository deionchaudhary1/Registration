#Program Desc - takes in user input and stores it into a demo.txt file
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class RegistrationApp(App):
    def build(self):
        #WINDOW NAME
        self.title = "Resitration Form"

        #LAYOUT
        layout = BoxLayout(orientation ='vertical', padding = 30, spacing = 10)
            #the space between different elements

        #HEADING
        head_label = Label(text="Python User Registration App", font_size = 40, bold=True, height=40)

        #TEXT BOX LABELS
        name_label = Label(text="Name:", font_size = 30)
        email_label = Label(text="Email:", font_size = 30)
        password_label = Label(text="Password:", font_size = 30)
        confirm_label = Label(text="Confirm Password:", font_size = 30)

        #INPUT SECTIONS
        self.name_input = TextInput(multiline = False, font_size = 25)
        self.email_input = TextInput(multiline = False, font_size = 25)
        self.password_input = TextInput(multiline = False, font_size = 25, password = True)#holding highly sensitve info
        self.confirm_input = TextInput(multiline = False, font_size = 25, password = True)

        #REGISTER BUTTON
        submit_button = Button(text = "Register", font_size = 18, on_press = self.register)

        #Adding to Layout (order matters)
        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(submit_button)
        return layout
    
    def register(self, instance):
        #if click, take all data that user inputed and store values in some variables
        name = self.name_input.text #name = input
        email = self.email_input.text
        password = self.password_input.text
        confirm = self.confirm_input.text

        #ACCOUNTING FOR ERRORS
        #if user forgot to enter on box --> send error message
        if name.strip() == '' or email.strip() == '' or password.strip() =='' or confirm.strip() == '':
            message = "Please fill in all fields"

        #PASSWORD MATCHING
        elif password != confirm:
            message = "Passwords do not match"

        #STORE INFO
        else: #no error
            filename = name + '.txt' #generate a file with user's name
            with open(filename, 'w') as file:
                #write info to file
                file.write('Name: {}\n'.format(name))
                file.write('Email: {}\n'.format(email))
                file.write('Password: {}\n'.format(password))
            message = "Registration Successful\nName: {}\nEmail: {}".format(name, email)


        #DISPLAY POP-UP
        popup = Popup(title = "Registration Status", content = Label(text=message), size_hint = (None, None), size = (800, 400))
        popup.open()

        #IF NO MESSGAGE (NO ERROR), POPUP DOESN'T DISPLAY


            


if __name__=='__main__':
    RegistrationApp().run()
