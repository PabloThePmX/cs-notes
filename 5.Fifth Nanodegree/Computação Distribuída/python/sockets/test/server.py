import tornado.ioloop
import tornado.web
import tornado.websocket
import json

clients = set()
document = ""

# 👇 This serves your HTML page
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("D:\\Users\\Pablo\\Desktop\\CC\\5.Fifth Nanodegree\\Computação Distribuída\\python\\sockets\\test\\test.html")  # file must exist in same folder


class MarkdownSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True  # allow connections (dev only)

    def open(self):
        print("WebSocket OPENED")
        clients.add(self)

        self.write_message(json.dumps({
            "type": "init",
            "content": document
        }))

    def on_message(self, message):
        global document
        data = json.loads(message)

        if data["type"] == "update":
            document = data["content"]

            for client in clients:
                if client != self:
                    client.write_message(json.dumps({
                        "type": "update",
                        "content": document
                    }))

    def on_close(self):
        print("WebSocket CLOSED")
        clients.remove(self)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),      # 👈 serves the page
        (r"/ws", MarkdownSocket) # 👈 websocket endpoint
    ], template_path=".")


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()