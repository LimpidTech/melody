def route_request(a):
    print(a)

def route_message(message):
    message.reply_channel.send({
        'text': message.content['text'],
    })
