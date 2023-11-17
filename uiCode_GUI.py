import tkinter as tk

# Function to handle UI button click
def submit_query():
    user_query = user_input.get()  # Get user input
    response = handle_user_query(user_query)  # Process user query using the backend
    ai_response.config(text=response)  # Update the UI with the AI response

root = tk.Tk()
root.title("AI Assistant")

user_input = tk.Entry(root, width=50)
user_input.pack()

submit_button = tk.Button(root, text="Submit", command=submit_query)
submit_button.pack()

ai_response = tk.Label(root, text="")
ai_response.pack()

root.mainloop()
