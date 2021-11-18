# Fraud Detector

## Project Setup
Project directory looks like this:
```
.
├── docker-compose.yml
├── detector
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
└── generator
  ├── Dockerfile
  ├── app.py
  └── requirements.txt
```
### Kafka Network
To allow the Kafka zookeeper and broker services to interact (as they are spun up in separate `docker-compose` files), I use an external docker network by running `docker network create kafka-network` on the command line. This way, the Kafka cluster runs as an isolated system separate from the Docker applications.

The new network must be specified by name in the `docker-compose.yml` and the `docker-compose.kafka.yml` files. 

<img width="219" alt="Network specification in docker-compose file" src="https://user-images.githubusercontent.com/65197541/142467252-5f615c18-6d90-4bbd-9b03-ccb887c4488a.png">

## Generator
The `generator` directory contains files for the transaction generator which creates an infinite stream of faux-transactions for us to play with. The generator application is a Kafka producer that publishes plain byte messages to the Kafka cluster to be stored on-disk as a broker topic. We can build producers using the `kafka-python` library.

After building the producer, it must be included in the `docker-compose.yml` config.

<img width="376" alt="Add generator app to docker-compose config" src="https://user-images.githubusercontent.com/65197541/142468194-88eca51d-1b65-45bc-ba67-ad81ba78e3cb.png">

### Test
1. Start network: ``
2. Spin up local Kafka cluster: ``
3. Start generator's producer: `docker-compose up`

## Detector 
The `detector` directory contains files for the fraud detector.
