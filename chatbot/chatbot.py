import tkinter as tk
import speech_recognition as sr

# Simple rule-based chatbot logic
def get_response(user_input):
    responses = {
        "hello": "Hello! How can I assist you?",
        "how are you": "I'm just a chatbot. But I'm here to help!",
        "bye": "Goodbye! Have a great day!",
        "Hi": "Hy there"
        # Add more responses as needed
    }

    user_input = user_input.lower()
    response = responses.get(user_input, "I'm sorry, I don't understand that.")
    return response

def send_message(event=None):
    user_input = input_entry.get()
    response = get_response(user_input)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_log.insert(tk.END, "ChatBot: " + response + "\n", "bot")
    chat_log.config(state=tk.DISABLED)
    input_entry.delete(0, tk.END)

def listen_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        input_entry.delete(0, tk.END)
        input_entry.insert(tk.END, user_input)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

root = tk.Tk()
root.title("Basic ChatBot GUI")

chat_log = tk.Text(root, wrap=tk.WORD, width=40, height=10)
chat_log.tag_configure("user", foreground="blue")
chat_log.tag_configure("bot", foreground="red")
chat_log.config(state=tk.DISABLED)

input_entry = tk.Entry(root, width=30)
send_button = tk.Button(root, text="Send", command=send_message)
listen_button = tk.Button(root, text="Listen", command=listen_microphone)

chat_log.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
input_entry.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
send_button.grid(row=1, column=2, pady=5)
listen_button.grid(row=1, column=1, columnspan=5, pady=5)

# Bind the "Enter" key to the send_message() function
root.bind("<Return>", send_message)

root.mainloop()
