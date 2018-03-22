from channels import routing

routes = [
    routing.route(
        'websocket.resceive', 'metanic.realtime.consumers.route_message'
    ),
]
