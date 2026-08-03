

try:

    with open("article.txt", "r") as file:
    
        content = file.read()
        char_count = len(content)
        word_count = len(content.split())
        line_count = len(content.splitlines())
        
        print(f"Results for 'article.txt':")
        print(f"● Total Lines: {line_count}")
        print(f"● Total Words: {word_count}")
        print(f"● Total Characters: {char_count}")

except FileNotFoundError:
    print("Error: The file 'article.txt' was not found.")
    print("Please make sure the file exists in the same directory as this script.")
