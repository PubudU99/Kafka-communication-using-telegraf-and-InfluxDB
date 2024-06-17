# Local Deployment Setup
## Steps

### Step 01 - Downloading Kafka
* Install Kafka windows in your computer.
* Select your preffered OS and download
  - [Kafka Download](https://kafka.apache.org/downloads)
---
### Step 02 - Setting up Kafka Directory
* Extract the zip file to C: directory and rename it as Kafka ( This is for clarity - not nessasary)
---
### Step 03 - CMD 
* Go to the relevent folder for your OS in Kafka Folder
 - For windows you should be in,
 ```bash
C:\kafka\bin\windows
```
 - Next open two command prompts in that directory - Type cmd in the address bar
---
### Step 04 - Initializing broker server and Zookeeper
* Enter the codes given -> [Initializing Codes](.main/Local%20Deployment/Server%20initializing%20codes.txt/)
* Open seperate 2 Prompts for Kafka, Zookeeper in that same directory
> Starting Zookeeper
```bash
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```
> Starting Kafka server
```bash
.\bin\windows\kafka-server-start.bat .\config\server.properties
```
---
### Step 05 - Creating topics for producing and consuming data by the kafka
* Enter the codes below to create topics for data communication
> Creating topic
```bash
.\bin\windows\kafka-topics.bat --create --topic your-topic-name --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
---
### Step 07 - Checking the Producer and consumer are working via CMD
> Producing messages
```bash
.\bin\windows\kafka-console-producer.bat --topic your-topic-name --bootstrap-server localhost:9092
```
> Consuming data to the topic
```bash
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic your-topic-name --from-beginning
```
---
### Step 06 - Running the python files to inspect communication
* You can find the Kafka Producer -> [Producer](./Local%20Deployment/kafka_producer.py)
* You can find the Kafka consumer -> [Consumer](./Local%20Deployment/kafka_consumer.py)
---
### Step 07 - Done
---

