from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of jokes (you can replace this with your own jokes)
jokes = [
    "Why was the math book sad? Because it had too many problems!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "How does a penguin build its house? Igloos it together!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "I used to play piano by ear, but now I use my hands.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "How do you organize a space party? You planet!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "I'm on a seafood diet. I see food, and I eat it.",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Did you hear about the cheese factory that exploded? There was nothing left but de-brie.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't oysters donate to charity? Because they are shellfish!",
    "How do you make a tissue dance? You put a little boogie in it!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don't scientists trust stairs? Because they're always up to something!",
    "I'm writing a book on reverse psychology. Please don't read it!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "I'm friends with all electricians. We have such good current connections.",
    "Why was the math book sad? Because it had too many problems!",
    "How does a penguin build its house? Igloos it together!",
    "I'm reading a book about anti-gravity. It's really uplifting!",
    "What do you call a factory that makes okay products? A satisfactory.",
    "I used to play piano by ear, but now I use my hands.",
    "I'd tell you a chemistry joke, but all the good ones are Argon.",
    "I'm friends with all electricians. We have such good current connections.",
    "Why don't skeletons fight each other? They don't have the guts!",
]

@app.route('/random_joke', methods=['GET'])
def get_random_joke():
    random_joke = random.choice(jokes)
    return jsonify({'joke': random_joke})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3010)
