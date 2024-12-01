import wikipedia


def main():
    """ prompts the user for a search phrase, then prints some details of that page"""
    search_phrase = input("Enter a search phrase: ")
    while search_phrase:
        try:
            wikipedia.page(search_phrase, auto_suggest=False)
            print (f"{wikipedia.summary.(search_phrase)}")
        except wikipedia.exceptions.PageError:
            print (f"Error: Page for {search_phrase} does not exist")
        except wikipedia.exceptions.DisambiguationError:
            print (f"Error: Disambiguation for {search_phrase}")
        search_phrase = input("Enter a search phrase: ")
    print("Farewell")

main()