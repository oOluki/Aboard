import socket
import threading
import key_input
import os

def serve_html(filename):
    # Read the HTML file content
    with open(filename, 'r') as file:
        html_content = file.read()

    # Prepare the HTTP response
    http_response = f"""HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html_content)}

{html_content}
"""
    return http_response.encode('utf-8')

def init_server(address):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(address)
    server.listen(1)

    print("Server stablished on " + address[0] + ":" + str(address[1]))
    return server


# Server setup
server = init_server(('<enter your server address here>'))
running_server: bool = True
update_server: bool = True

def run_server():
    global server, update_server
    while running_server:    
        print("Waiting for connection")
        client_socket, client_address = server.accept()
        print(f"Connection from {client_address}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"client: {data}")

        if 'POST /button_id' in data:
            
            request_body = data.split('\r\n\r\n')[1]
            button_id = request_body.strip() 
            
            # Process the received button ID
            print(f"Button ID received: {button_id}")
            if button_id != '':
                key_input.press_key(button_id)

        elif 'POST /text_input' in data:
            request_body = data.split('\r\n\r\n')[1]
            key_input.pyautogui.typewrite(request_body)

        
        response = serve_html('page.html')
        client_socket.sendall(response)
        
        # Close the connection
        client_socket.close()


server_process = threading.Thread(target=run_server)
server_process.start()


while running_server:
    if(input("admin (enter close and refresh any client to exit): ") == "close"):
        running_server = False
        break


server.close()
server_process.join()

#