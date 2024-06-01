from wonderwords import RandomSentence
from colorama import init, Fore, Style
import time

init()

def typing_speed():
    def convert_to_colored(generated, user):
        colored_text = ''
        for gen_char, user_char in zip(generated, user):
            if gen_char == user_char:
                colored_text += Fore.GREEN + user_char + Style.RESET_ALL
            else:
                colored_text += Fore.RED + user_char + Style.RESET_ALL
        # Add remaining characters (if any) from the longer string without coloring
        if len(generated) > len(user):
            colored_text += generated[len(user):]
        elif len(user) > len(generated):
            colored_text += Fore.RED + user[len(generated):] + Style.RESET_ALL
        return colored_text

    sen1 = RandomSentence()
    generated_sentence = sen1.sentence()
    print("Generated Sentence:", generated_sentence)
    print("Type To Start:")

    start_time = time.time()
    user_input = input()
    stop_time = time.time()

    colored_output = convert_to_colored(generated_sentence, user_input)
    print(colored_output)

    time_for_typing = stop_time - start_time
    minutes = time_for_typing / 60
    length_of_sentence = len(user_input)
    speed = int(length_of_sentence / minutes)

    if user_input == generated_sentence:
        print(f"\nSpeed of typing: {speed} characters per minute")
    else:
        print("\nRETRY!!!\n")
        typing_speed()

typing_speed()
