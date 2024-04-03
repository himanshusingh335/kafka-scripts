from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

def create_topic(bootstrap_servers, topic_name, partitions=1, replication_factor=1):
    admin_client = KafkaAdminClient (bootstrap_servers=bootstrap_servers)
    topic = NewTopic(name=topic_name, num_partitions=partitions, replication_factor=replication_factor) 
    try:
        admin_client.create_topics(new_topics=[topic])
        print (f"Topic '{topic_name}' created successfully.")
    except TopicAlreadyExistsError:
        print (f"Topic {topic_name}' already exists.")
    finally:
        admin_client.close()
if __name__=='__main__':
    bootstrap_servers ="localhost: 9092"
    topic_name = "test"
    create_topic (bootstrap_servers, topic_name)