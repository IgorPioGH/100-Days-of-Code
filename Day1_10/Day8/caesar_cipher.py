alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):

    new_word = ""
    for letter in original_text:
        if letter in alphabet: # If is a letter of the alphabet
            index = alphabet.index(letter) # search the index
            shifted_index_encoding = index + shift_amount # new index for encoding
            shifted_index_decoding = index - shift_amount # new index for decoding

            if direction == 'encode':
                new_word += alphabet[shifted_index_encoding % len(alphabet)] # circular list the new index

            elif direction == 'decode':
                new_word += alphabet[shifted_index_decoding % len(alphabet)]
        else: # If was not a letter of the alphabet
            new_word += letter

    print(f'Here is the encoded result: {new_word}') # Final result

# Cycle to go again
again = "yes"
while again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(original_text=text, shift_amount=shift)
    again = input("Do you want to go again? 'yes' or 'no'\n")
