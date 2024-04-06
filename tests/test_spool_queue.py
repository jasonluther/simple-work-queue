from time import sleep
from simple_work_queue.queue_consumer import QueueConsumerSpoolDir
from simple_work_queue.queue_producer import QueuePublisherSpoolDir
import json
import os
import tempfile
import unittest


class TestSpoolQueue(unittest.TestCase):
    def test_queue_consumer_spool_dir(self):
        test_message_data = {
            "data": "Test message",
            "attributes": {"key": "value"},
        }
        test_message_json = json.dumps(test_message_data)

        with tempfile.TemporaryDirectory() as temp_dir:
            print(temp_dir)
            spool_dir = temp_dir
            file_extension = ".json"

            producer = QueuePublisherSpoolDir(spool_dir, file_extension)

            def process_request_func(message):
                print("process_request_func")
                self.assertDictEqual(json.loads(message), test_message_data)
                return True

            producer.publish(test_message_json)

            consumer = QueueConsumerSpoolDir(spool_dir, file_extension)

            consumer.consume_forever(process_request_func, max_iterations=1)

            print(os.listdir(spool_dir))
            sleep(1)
            self.assertEqual(len(os.listdir(spool_dir)), 0)


if __name__ == "__main__":
    unittest.main()
