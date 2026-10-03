from kafka import KafkaConsumer, KafkaProducer

from src.core.config import settings

BOOTSTRAP_SERVERS = settings.kafka_bootstrap_servers.split(",")


def get_producer(**kwargs) -> KafkaProducer:
    return KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS, **kwargs)


def get_consumer(*topics: str, **kwargs) -> KafkaConsumer:
    return KafkaConsumer(*topics, bootstrap_servers=BOOTSTRAP_SERVERS, **kwargs)
