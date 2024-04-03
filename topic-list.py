from kafka.admin import KafkaAdminClient

def get_topics_list(bootstrap_servers):
    admin_client = KafkaAdminClient (bootstrap_servers=bootstrap_servers)
    topics = admin_client.list_topics()
    return topics
if __name__=='__main__':
    bootstrap_servers ="localhost: 9092"
    topics=get_topics_list(bootstrap_servers)
    print("Topics list: ")
    for topic in topics:
        print(topic)