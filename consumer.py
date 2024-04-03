from kafka import KafkaConsumer

def consume_messages(topic):
    consumer=KafkaConsumer(topic,bootstrap_servers='localhost:9092', group_id='my-group')

    try:
        for msg in consumer:
            print(f'Received message: {msg.value.decode("utf-8")}')
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__=='__main__':
    topic_name='quickstart-event'
    consume_messages(topic_name)

