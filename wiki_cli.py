import wikipediaapi
import pyfiglet
import os
from pathlib import Path
import random
from datetime import datetime

user_email = os.getenv("WIKI_USER_EMAIL")
if not user_email:
    user_email = input("Please enter your contact email for the Wikipedia API.")
folder_path = Path("wiki_downloads")
isExist = os.path.exists("wiki_downloads")
wiki_wiki = wikipediaapi.Wikipedia(user_agent= f'Wiki_Client_Project ({user_email})', language='en')
l_banner = pyfiglet.figlet_format("WIKI_cli", font="larry3d")
i_banner = pyfiglet.figlet_format("THANK_YOU", font="larry3d")
folder_path.mkdir(parents=True, exist_ok=True)
print(l_banner)

while True:
    
    print("\n--------------------------------------------------------------------------")
    request = input("Hey, what do you wanna learn about today? (Type exit to leave)")
    if request == "exit":
        print(i_banner)
        break
    if not request:
        print("Hey, search query cant be empty!")
        continue

    rand_prefix = random.randint(1000, 9999)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{rand_prefix}_{timestamp}.txt"
    
    results = wiki_wiki.search(request, limit=5)
    my_list = list(results.pages.keys())
    if not my_list:
        print("Sorry, we couldn't find that!")
        continue
    print("Here are the results I found!", my_list)
    choice = input(("Please type the EXACT name of the item you want to see!(Type back to go back!)"))
    if choice == "back":
        continue
    if choice in my_list:
        page = wiki_wiki.page(choice)
        summary = page.summary
        words = summary.split()
        count = len(words)
        print("Heya! Heres a summary of the topic you chose!: ", summary)
        
        print("I've already saved that ", count, ' word summary to your computer. Have fun!')
        print(i_banner)
   
        final_destination = folder_path / filename
        with open(final_destination, "w", encoding="utf-8") as file:
            file.write(summary)
    else:
        print("Sorry, didn't catch that! Please try again")
    continue