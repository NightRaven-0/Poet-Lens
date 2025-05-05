from transformers import pipeline, set_seed

# Load the text generation pipeline
text_generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_poem(caption):
    prompt = f"Write a short poetic description of this scene: {caption}\nPoem:"
    
    generated = text_generator(prompt, max_length=80, num_return_sequences=1, do_sample=True)
    poem = generated[0]['generated_text'].replace(prompt, '').strip()
    
    return poem
