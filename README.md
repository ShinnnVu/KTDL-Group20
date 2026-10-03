# KTDL-Group20

## base configs

| Container | Host port(s) | Internal port(s) |
|---|---|---|
| `db` (postgres) | - | 5432 |
| `adminer` | 8082 | 8080 |
| `mongo` | - | 27017 |
| `mongo-express` | 8081 | 8081 |
| `kafka-0` / `kafka-1` / `kafka-2` | random | 9092 (client), 9093 (controller) |
| `spark` | 8080, 7077 | 8080, 7077 |
| `spark-worker` | - | 8081 |
| `namenode` | 9870, 9000 | 9870, 9000 |
| `datanode` | - | 9864, 9866 |
| `resourcemanager` | 8088 | 8088 |
| `nodemanager` | - | 8042 |

- `db` — Postgres database, stores relational data.
- `adminer` — web UI for browsing/querying `db`.
- `mongo` — MongoDB database, stores document data.
- `mongo-express` — web UI for browsing/querying `mongo`.
- `kafka-0`, `kafka-1`, `kafka-2` — 3-broker Kafka cluster (KRaft mode, no Zookeeper) for streaming data between services.
- `spark` — Spark master; schedules and tracks jobs, serves the cluster UI.
- `spark-worker` — Spark worker; executes the jobs the master assigns.
- `namenode` — HDFS namenode; tracks file metadata and block locations.
- `datanode` — HDFS datanode; stores the actual file blocks.
- `resourcemanager` — YARN resource manager; schedules cluster resources for jobs.
- `nodemanager` — YARN node manager; runs containers/tasks on behalf of the resource manager.

All containers share one external Docker network, `ktdl-network`, so every container can reach every other by its service name. Start everything with:

```bash
./start-all.sh
```
