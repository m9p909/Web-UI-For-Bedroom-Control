import pika
import traceback
import unittest
from multiprocessing import Process
from typing import List
def TODO():
    raise Exception("TODO")

class _MQSubscribeThread(Process):

    def __init__(self, connection, exchange_name, callback):
        channel = connection.channel()
        exchange = channel.exchange_declare(exchange=exchange_name, exchange_type="fanout")
        self.exchange = exchange
        self.queue_name = exchange.method.queue
        channel.queue_bind(exchange=exchange_name, queue=self.queue_name)
       # def callback(ch, method, properties, body):
       #     print(" [x] %r" % body)
        channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)
        self.channel = channel

    def run(self):
        self.channel.start_consuming()



class PubSubManager():
    subscribe_threads: List[_MQSubscribeThread] = []

    exchange_name = "raspi"
    def __init__(self, connection_str: str | None):
        if connection_str:
            self.connection_str = connection_str
            self.parameters = pika.URLParameters(connection_str)

        self._connect()
        self._open_channel()
    
    def _start_io_loop_blocking(self):
        try:
            self.connection.ioloop.start()
        except KeyboardInterrupt:
            self.connection.close()
            self.connection.ioloop.start()

    def _open_channel(self):
        self._channel = self.connection.channel()
        return self._channel


    def _connect(self):
        self.connection = pika.SelectConnection()  


    def send_message(self, message, exchange):
        TODO()


    def subscribe(self, exchange, on_message_receive):
        def callback(ch, method, properties, body): # will create up to 20-30 threads, not ideal Twisted? or good enough?
            on_message_receive(body, properties)
        process = _MQSubscribeThread(self.connection, exchange, callback)
        process.start()
        self.subscribe_threads.append(process)

    def unsubscribe(self, exchange):
        for proc in self.subscribe_threads:
            if proc.exchange == exchange:
                proc.terminate()
        
        





mq_server_up = False
class PubSubManagerTest(unittest.TestCase):
    
    def test_send_message(self):
        manager = PubSubManager(None)
        manager.send_message("cool stuff", "/pizza/party")

    def test_does_not_work_with_invalid_connection_string(self):
        exceptTriggered = False
        try:
            PubSubManager("dajks")
        except Exception:
            traceback.print_exc()
            exceptTriggered = True
        self.assertTrue( exceptTriggered)

    def test_works_with_valid_connection_string_when_mq_is_up(self):
        exception_triggered = False
        try: 
            PubSubManager("amqp://guest:guest@localhost:5672/%2F")
        except Exception: 
            traceback.print_exc()
            exception_triggered = True
        assert exception_triggered == (not mq_server_up)
    
    def test_constructor_takes_none(self):
        exception_triggered = False
        try: 
            PubSubManager(None)
        except Exception: 
            traceback.print_exc()
            exception_triggered = True
        assert exception_triggered == (not mq_server_up)
 

if __name__ == "__main__":
    unittest.main()
        

