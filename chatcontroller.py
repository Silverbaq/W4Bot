from chatterbot import ChatBot



chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

def chat_with_bot(message):
    # Get a response to an input statement
    return chatbot.get_response(message).text