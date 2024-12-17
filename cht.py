from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window

Config.set('graphics', 'resizable', False)
Window.size = (400, 600)

class ChatUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create widgets
        self.chat_label = Label(text='Chat')
        self.chat_history = Label(text='', halign='left', valign='top', text_size=(350, None))
        self.message_input = TextInput(multiline=False)
        self.send_button = Button(text='Send')
        
        # Add widgets to layout
        self.add_widget(self.chat_label)
        self.add_widget(self.chat_history)
        self.add_widget(self.message_input)
        self.add_widget(self.send_button)
        
        # Bind button press to function
        self.send_button.bind(on_press=self.send_message)
    
    def send_message(self, instance):
        message = self.message_input.text
        
        if message:
            # Add message to chat history
            self.chat_history.text += 'You: {}\n'.format(message)
            
            # Clear message input
            self.message_input.text = ''
            
            # TODO: Send message to other person in chat (implement your own logic here)
    
class ChatApp(App):
    def build(self):
        return ChatUI()
    
if __name__ == '__main__':
    ChatApp().run()