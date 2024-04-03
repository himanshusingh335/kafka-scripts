from kafka import KafkaProducer
import time
import random
def consume_messages(topic):
    producer=KafkaProducer(bootstrap_servers='localhost:9092')
   
    try:
        while True:
            myrand=random.uniform(20,100)
            producer.send(topic,f'{myrand}'.encode('utf-8'))
            print(f'Sent message: {myrand}')
            time.sleep(5)
    except KeyboardInterrupt:
        producer.close()

if __name__=='__main__':
    topic_name='quickstart-event'
    consume_messages(topic_name)