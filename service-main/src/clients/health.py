from uuid import uuid4

from src.clients import hdfs, kafka, mongo, postgres


def check_postgres() -> dict:
    try:
        conn = postgres.get_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT 1")
            return {"service": "postgres", "ok": True, "output": cur.fetchone()[0]}
        finally:
            conn.close()
    except Exception as e:
        return {"service": "postgres", "ok": False, "error": str(e)}


def check_mongo() -> dict:
    try:
        client = mongo.get_client()
        try:
            return {"service": "mongo", "ok": True, "output": client.admin.command("ping")}
        finally:
            client.close()
    except Exception as e:
        return {"service": "mongo", "ok": False, "error": str(e)}


def check_kafka() -> dict:
    try:
        message = f"health-check-{uuid4()}".encode()

        producer = kafka.get_producer()
        producer.send("health-check", message)
        producer.flush()
        producer.close()

        consumer = kafka.get_consumer(
            "health-check", auto_offset_reset="earliest", consumer_timeout_ms=3000
        )
        received = [m.value for m in consumer]
        consumer.close()

        return {"service": "kafka", "ok": message in received, "output": received}
    except Exception as e:
        return {"service": "kafka", "ok": False, "error": str(e)}


def check_hdfs() -> dict:
    try:
        client = hdfs.get_client()
        return {"service": "hdfs", "ok": True, "output": client.list("/")}
    except Exception as e:
        return {"service": "hdfs", "ok": False, "error": str(e)}


def check_all() -> dict:
    results = [check_postgres(), check_mongo(), check_kafka(), check_hdfs()]
    return {"ok": all(r["ok"] for r in results), "services": results}
