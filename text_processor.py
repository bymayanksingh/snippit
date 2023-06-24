import re
import sys

def generate_blobs(large_text, word_limit=2500):
    """Generates text blobs from a large text string, 
    doesn't consider punctuations."""
    
    words = re.findall(r'\b\w+\b', large_text)
    num_blobs = len(words) // word_limit
    blobs = []
    for i in range(num_blobs):
        start = i * word_limit
        end = (i+1) * word_limit
        blob = " ".join(words[start:end])
        blobs.append(blob)
    remaining_words = words[num_blobs * word_limit:]
    if remaining_words:
        blobs.append(" ".join(remaining_words))
    return blobs


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the path to the input file!")
    else:
        input_file = sys.argv[1]
        with open(input_file, 'r') as file:
            text = file.read()
            blobs = generate_blobs(text)
            for i, blob in enumerate(blobs):
                print(f"Blob{i+1}: {blob}\n")