from transformers import pipeline, set_seed

# Load the text generation pipeline once
text_generator = pipeline("text-generation", model="gpt2-medium")
set_seed(42)  # Optional: for reproducibility

def generate_poem(caption):
    prompt = (
        f"Write a short, vivid and emotional poem inspired by the scene: \"{caption}\".\n\n"
        "Poem:\n"
    )

    response = text_generator(
        prompt,
        max_length=120,
        temperature=0.9,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,
        do_sample=True,
        num_return_sequences=1
    )

    # Clean output: remove the prompt from result
    poem = response[0]['generated_text'].replace(prompt, '').strip()
    return poem
