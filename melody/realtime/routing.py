from channels import routing

routes = [
    routing.route(
        'websocket.resceive', 'melody.realtime.consumers.route_message'
    ),
]
