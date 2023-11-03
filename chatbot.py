import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT-3.5.")
    parser.add_argument("--personality", type=str, help="A brief summary of the chatbot personality",
                        default="happy and helpful")
    args = parser.parse_args()

    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}"
    messages = [{"role":"system", "content":initial_prompt}]

    while True:
        try:
            user_input = input(f"{bcolors.BOLD}{bcolors.BLUE}YOU:{bcolors.END}{bcolors.END} ")
            messages.append({"role":"user", "content":user_input})
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            messages.append(res["choices"][0]["message"].to_dict())
            print(f'{bcolors.BOLD}{bcolors.RED}ASSISTANT:{bcolors.END}{bcolors.END} {res["choices"][0]["message"]["content"]}')

        except KeyboardInterrupt:
            print(f"{bcolors.BOLD}{bcolors.GREEN}Exiting...{bcolors.END}{bcolors.END}")
            break

if __name__=="__main__":
    main()

