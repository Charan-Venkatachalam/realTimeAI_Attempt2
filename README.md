Explanation of Integration:

1. The submit_query() function is triggered when the user clicks the submit button in the UI.
2. It fetches the user input from the UI entry field (user_input), calls handle_user_query() 
from the backend, processes the input, and retrieves an AI response.
3. Finally, it updates the ai_response label in the UI with the obtained AI response.
4. This code links the UI elements (entry field, submit button) with the backend logic (handle_user_query()),
allowing the UI to interact with the backend to process user queries and display AI responses.

Please note that this example is a basic demonstration. For a complete application, you'd need 
to implement more sophisticated AI logic inside process_input() and handle various user 
interactions and scenarios in the UI.
