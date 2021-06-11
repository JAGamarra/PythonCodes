def greet(username):
    message = f'¡Hola, {username}!'

    def show_message():
        print(message)

    
    return show_message

username = 'Julian'

answer = greet(username)

answer()