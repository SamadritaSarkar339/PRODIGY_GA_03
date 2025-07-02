import random
from collections import defaultdict

# Function to build the Markov Chain model
def build_markov_chain(text, n=2):
    model = defaultdict(list)
    words = text.split()

    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        model[key].append(next_word)

    return model

# Function to generate new text
def generate_text(model, length=50, seed=None):
    if not seed:
        seed = random.choice(list(model.keys()))
    output = list(seed)

    for _ in range(length):
        key = tuple(output[-len(seed):])
        if key in model:
            next_word = random.choice(model[key])
            output.append(next_word)
        else:
            break

    return ' '.join(output)

# Sample text to train the model
sample_text = """
Artificial Intelligence is transforming the world. Machine learning enables computers to learn from data.
Markov chains are useful for generating random but plausible text based on probabilities of word sequences.
"""

# Build model and generate text
model = build_markov_chain(sample_text, n=2)
generated = generate_text(model, length=30)

print("Generated Text:\n", generated)
