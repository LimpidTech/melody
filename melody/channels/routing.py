from channels import routing


routes = (
    routing.route('http.request', 'melody.channels.consumers.route_request'),
    routing.route('websocket.resceive', 'melody.channels.consumers.route_message'),
)
