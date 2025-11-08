# 🧠 Cybersecurity Threat Detection ELK Project

A hands-on learning project to detect and visualize cybersecurity threats using the ELK stack (Elasticsearch, Logstash, Kibana).

## 📁 Project Structure

```
cyber-threat-elk/
├── docker-compose.yml       # ELK stack services configuration
├── logstash/
│   └── pipeline/           # Logstash pipeline configurations (to be created)
├── data/                   # CSV dataset location
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- At least 4GB RAM available
- Kaggle Cybersecurity Threat Detection dataset

### Start the ELK Stack

```bash
docker-compose up -d
```

### Verify Services

- Elasticsearch: http://localhost:9200
- Kibana: http://localhost:5601

### Stop Services

```bash
docker-compose down
```
