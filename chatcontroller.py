from chatterbot import ChatBot



chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',

    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        }
    ]
)
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

def chat_with_bot(message):
    # Get a response to an input statement
    return chatbot.get_response(message).text