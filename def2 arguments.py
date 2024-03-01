name = input('Enter name:' )

def greet(lang):
    if lang == 'pt':
        return 'Oi'
    elif lang == 'en':
        return 'Hello'
    elif lang == 'es':
        return 'Hola'  # Corrected spelling
    else:
        return 'no lang'

while True:
    language = input('Enter lang (or "quit" to exit): ')
    if language == 'quit': #or delete this to break the loop and go next
        break  # Exit the loop if the user enters 'quit'

    text = greet(language)
    print(text, 'Sr', name)

