# 🧠 Cybersecurity Threat Detection ELK Project

A comprehensive hands-on project demonstrating cybersecurity threat detection, analysis, and visualization using the ELK stack (Elasticsearch, Logstash, Kibana).

## 📊 Project Overview

This project ingests cybersecurity threat detection logs from Kaggle, processes them through a Logstash pipeline, stores them in Elasticsearch, and visualizes attack patterns through interactive Kibana dashboards.

**Dataset**: [Kaggle Cybersecurity Threat Detection Logs](https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs)  
**Stack**: Elasticsearch 8.11.0, Logstash 8.11.0, Kibana 8.11.0  
**Deployment**: Docker Compose

---

## ✨ Features

- ✅ **Automated Data Pipeline**: Logstash CSV ingestion with field parsing
- ✅ **Optimized Index Mapping**: Custom Elasticsearch mappings for IP addresses, timestamps, and categorical data
- ✅ **Interactive Dashboards**: Multiple Kibana visualizations showing attack patterns, trends, and distributions
- ✅ **Scalable Architecture**: Docker-based deployment with configurable resources
- ✅ **Sample Dataset**: Stratified sampling script for faster development/testing

---

## 📁 Project Structure

```
cyber-threat-elk/
├── docker-compose.yml                    # ELK stack services configuration
├── elasticsearch_mapping.json            # Custom index mappings
├── logstash/
│   └── pipeline/
│       └── cybersecurity.conf           # Logstash pipeline configuration
├── data/
│   ├── small_sample.csv                 # Reduced dataset (1% sample)
│   └── sample_cybersecurity.csv         # Medium dataset (10% sample)
├── create_index.py                      # Elasticsearch index creation script
├── create_small_sample.py               # Dataset sampling utility
├── setup_kibana_dataview.py             # Automated Kibana data view setup
├── explore_dataset.py                   # Dataset analysis script
├── KIBANA_SETUP_GUIDE.md               # Step-by-step visualization guide
├── ADD_MORE_VISUALIZATIONS_GUIDE.md    # Advanced visualization tutorials
├── QUICK_VIZ_CHEATSHEET.md             # Quick reference for visualizations
├── ADVANCED_FEATURES.md                # Next steps and advanced features
└── README.md                            # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Docker & Docker Compose** installed
- **Python 3.8+** with pip
- **4GB+ RAM** available for ELK stack
- **Internet connection** for dataset download

### 1. Clone & Setup

```bash
cd cyber-threat-elk
```

### 2. Download Dataset

Option A: Download from [Kaggle](https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs) and place in `data/` folder

Option B: Use the sampling script to create a smaller test dataset:

```bash
python create_small_sample.py
```

### 3. Start ELK Stack

```bash
docker-compose up -d
```

Wait 1-2 minutes for services to initialize.

### 4. Create Elasticsearch Index

```bash
python create_index.py
```

### 5. Verify Ingestion

Check document count:

```powershell
Invoke-RestMethod -Uri "http://localhost:9200/cybersecurity-threats/_count"
```

Expected result: ~6,000 documents (small sample) or ~60,000 documents (10% sample)

### 6. Setup Kibana

```bash
python setup_kibana_dataview.py
```

Then open: **http://localhost:5601**

---

## 📊 Dataset Information

**Source**: Kaggle - Cybersecurity Threat Detection Logs  
**Original Size**: 833 MB (~5.8M records)  
**Sample Sizes**:

- Small: 0.83 MB (~6K records, 1% sample)
- Medium: 83 MB (~580K records, 10% sample)

**Fields**:

- `timestamp` - Event timestamp
- `source_ip` - Attack source IP address
- `dest_ip` - Target IP address
- `protocol` - Network protocol (TCP, HTTP, HTTPS, UDP, ICMP, SSH, FTP)
- `action` - Firewall action (allowed, blocked)
- `threat_label` - Threat classification (benign, suspicious, malicious)
- `log_type` - Log source (firewall, ids, application)
- `bytes_transferred` - Data volume
- `user_agent` - Client software/tool
- `request_path` - Target URL path

---

## 🎨 Visualizations

### Built-in Dashboards

1. **Threat Timeline** - Attacks over time (Line chart)
2. **Threat Distribution** - Pie chart of benign/suspicious/malicious
3. **Top Threat Types** - Bar chart of attack categories
4. **Protocol Distribution** - Donut chart of network protocols
5. **Top Attack Sources** - Table of most active IPs
6. **Attack Tools** - Tag cloud of user agents (Nmap, SQLMap, etc.)
7. **Log Source Distribution** - Firewall vs IDS vs Application logs
8. **Block Rate Metrics** - Success rate of security controls

See `KIBANA_SETUP_GUIDE.md` for step-by-step creation instructions.

---

## 🔧 Configuration

### Elasticsearch Mapping

Custom field mappings for optimal queries:

- `source_ip` & `dest_ip`: `ip` type (supports CIDR queries)
- `timestamp`: `date` type (time-series analysis)
- `protocol`, `action`, `threat_label`: `keyword` type (exact matching, aggregations)
- `bytes_transferred`: `long` type (numeric operations)

See `elasticsearch_mapping.json` for full schema.

### Logstash Pipeline

Pipeline features:

- CSV parsing with header skip
- Date parsing to `@timestamp`
- Type conversions (bytes to integer)
- Field cleanup (remove unnecessary metadata)

See `logstash/pipeline/cybersecurity.conf` for configuration.

### Docker Resources

Default allocations (adjust in `docker-compose.yml`):

- Elasticsearch: 512MB heap
- Logstash: 256MB heap
- Kibana: Default

---

## 🛠️ Advanced Features

### Data Sampling

Create custom sample sizes:

```python
# Edit create_small_sample.py
sample_fraction = 0.05  # 5% of data
```

### Query Examples

Search Elasticsearch directly:

```bash
# Find all malicious attacks
curl "http://localhost:9200/cybersecurity-threats/_search?q=threat_label:malicious"

# Get attack count by protocol
curl "http://localhost:9200/cybersecurity-threats/_search" -H 'Content-Type: application/json' -d'
{
  "size": 0,
  "aggs": {
    "protocols": {
      "terms": { "field": "protocol.keyword" }
    }
  }
}'
```

### Add GeoIP Enrichment

See `ADVANCED_FEATURES.md` for instructions on:

- Geographic attack visualization
- IP geolocation mapping
- Country-level aggregations

### Set Up Alerts

Configure Kibana alerts for:

- Malicious traffic spikes
- Unusual protocol usage
- High-volume data transfers

---

## 📚 Documentation

- **`KIBANA_SETUP_GUIDE.md`** - Complete Kibana visualization tutorial
- **`ADD_MORE_VISUALIZATIONS_GUIDE.md`** - 10 additional visualization ideas
- **`QUICK_VIZ_CHEATSHEET.md`** - Quick reference for common charts
- **`ADVANCED_FEATURES.md`** - Next-level features (alerts, GeoIP, etc.)

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

✅ **ELK Stack Architecture** - Understanding Elasticsearch, Logstash, Kibana components  
✅ **Data Pipeline Design** - CSV ingestion, parsing, transformation  
✅ **Index Optimization** - Field mappings, data types, query performance  
✅ **Data Visualization** - Creating meaningful charts and dashboards  
✅ **Security Analytics** - Identifying attack patterns and trends  
✅ **Docker Deployment** - Container orchestration with Docker Compose

---

## 🐛 Troubleshooting

### Elasticsearch not responding

```bash
docker-compose restart elasticsearch
# Wait 30-60 seconds, then check: curl http://localhost:9200
```

### Logstash not ingesting data

```bash
# Check Logstash logs
docker logs logstash

# Verify pipeline configuration
docker exec logstash cat /usr/share/logstash/pipeline/cybersecurity.conf
```

### Kibana can't connect

```bash
# Restart Kibana
docker-compose restart kibana
# Wait 1-2 minutes, then access: http://localhost:5601
```

### Out of memory errors

Increase Docker memory allocation or reduce dataset size using sampling script.

---

## 📊 Project Statistics

- **Lines of Code**: ~500
- **Configuration Files**: 3 (docker-compose, pipeline, mapping)
- **Python Scripts**: 5 (indexing, sampling, exploration)
- **Documentation**: 1,500+ lines across 5 guides
- **Visualizations**: 8+ dashboards
- **Data Volume**: 6K-6M records (configurable)

---

## 🤝 Contributing

This is a learning project. Feel free to:

- Add more visualizations
- Enhance the Logstash pipeline
- Create additional sampling strategies
- Improve documentation

---

## 📝 License

Educational project - use freely for learning purposes.

---

## 🔗 Resources

- [Elastic Documentation](https://www.elastic.co/guide/)
- [Kibana Lens Guide](https://www.elastic.co/guide/en/kibana/current/lens.html)
- [Logstash Configuration](https://www.elastic.co/guide/en/logstash/current/configuration.html)
- [Kaggle Dataset](https://www.kaggle.com/datasets/aryan208/cybersecurity-threat-detection-logs)

---

## 📧 Support

For questions or issues:

1. Check the troubleshooting section above
2. Review documentation files in the project
3. Consult Elastic Stack official documentation

---

**Built with ❤️ for cybersecurity education and ELK stack learning**
