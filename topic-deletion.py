from kafka.admin import KafkaAdminClient

def delete_topic(bootstrap_servers, topic_name):
    admin_client = KafkaAdminClient (bootstrap_servers=bootstrap_servers)
    admin_client.delete_topics([topic_name])

if __name__=='__main__':
    bootstrap_servers ="localhost: 9092"
    topic_name = "test"
    delete_topic(bootstrap_servers, topic_name)
    print(f'{topic_name} deleted successfully !!')