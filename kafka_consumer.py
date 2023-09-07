from confluent_kafka import Consumer
import os
################
c=Consumer({'bootstrap.servers':os.environ.get('KAFKA_BOOTSTRAP'),'group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe([os.environ.get('KAFKA_TOPIC')])
################
def main():
    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print(data)
    c.close()
        
if __name__ == '__main__':
    main()
