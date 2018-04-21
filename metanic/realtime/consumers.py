def route_message(message):
    message.reply_channel.send({
        'error': 'Could not handle socket request',
    })
