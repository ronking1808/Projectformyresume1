from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a Flask web application
app = Flask(__name__)

# Create and train the chatbot
chatbot = ChatBot('corona bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations")

# Define a route for receiving user input and getting bot responses
@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_message = request.json['user_message']  # Get the user's message from the POST request
    bot_response = str(chatbot.get_response(user_message))  # Get the bot's response
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
