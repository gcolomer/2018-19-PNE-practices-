import http.server
import socketserver
import termcolor
from Seq import Seq

# Define the Server's port
PORT = 8008


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def validSequence(self, s):
        valid = 'ACTG'
        for letter in s:
            if letter not in valid:
                return False
        return True

    def tratar(self, s1, comando):
        print("Haciendo comando", comando)
        if (comando == "len"):
            return s1.len()
        elif (comando == "complement"):
            return s1.complement().get_strbase()
        elif (comando == "reverse"):
            return s1.reverse().get_strbase()
        elif (comando == "countA"):
            return s1.count('A')
        elif (comando == "countT"):
            return s1.count('T')
        elif (comando == "countG"):
            return s1.count("G")
        elif (comando == "countC"):
            return s1.count("C")
        elif (comando == "percA"):
            return s1.perc("A")
        elif (comando == "percT"):
            return s1.perc("T")
        elif (comando == "percG"):
            return s1.perc("G")
        elif (comando == "percC"):
            return s1.perc("C")
        else:
            return "ERROR"



    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        if self.path == "/":
            f = open("form.html", 'r')
            contents = f.read()
        elif '/seq' in self.path:
           contents = """<!DOCTYPE html>
           <html lang="en">
           <head>
                <meta charset= "UTF-8">
                <title>SERVER RESPONSE</title>
                </head>
                <body style"background-color: white">"""


           cadena = self.path.split('=')[1]
           trozos = cadena.split('&')
           parte = trozos[0]
           contents = contents + "<p>Cadena: "+parte+"</p"
           contents = contents + """<br> <a href="/"> [Main page] </a>
                      </body></html>"""
           contents = contents + "<p>Cadena: " + parte + "</p>"

           if self.validSequence(parte):
               s1 = Seq(parte)
               if 'len=on' in self.path:
                   longitud = s1.len()
                   contents = contents + "<p>Longitud: " + str(longitud) + "</p>"
               operation = self.path.split('operation=')[1].split("&")[0]
               contents = contents + "<p>Operation: " + operation + "</p>"
               base = self.path.split('base=')[1].split("&")[0]
               contents = contents + "<p>Base: " + base + "</p>"
               comando = operation + base
               respuesta = self.tratar(s1, comando)
               contents = contents + "<p>Respuesta: " + str(respuesta) + "</p>"
           else:
               contents = contents + "<p>No Valida</p>"

           contents = contents + """<br> <a href="/"> [Main page] </a>
            </body></html>"""


        else:
            f = open("Error.html", 'r')
            contents = f.read()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")