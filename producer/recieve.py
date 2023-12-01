import json
import time
import argparse

from kafka import KafkaConsumer

# ターミナル出力用
def topic_to_tm(consumer):
    print('ターミナル 出力')

    # Read data from kafka
    try :
        for message in consumer:
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value))
    except KeyboardInterrupt :
        print('\r\n Output to Terminal - interrupted!')
        return

# Kafka Topic からのデータ受取
def get_kafka_topic():
    # Initialize consumer variable and set property for JSON decode
    consumer = KafkaConsumer (
        'topic-01',
        bootstrap_servers = ['broker:29092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset="earliest"
    )

    print(consumer)
    return consumer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='KafkaからのIoT機器のなんちゃってStreamデータの取得')
    parser.add_argument('--mode', type=str, default='tm', help='tm（ターミナル出力）')
    args = parser.parse_args()

    start = time.time()

    consumer = get_kafka_topic()
    topic_to_tm(consumer)

    making_time = time.time() - start

    print("")
    print("Streamデータ取得待機時間:{0}".format(making_time) + " [sec]")
    print("")