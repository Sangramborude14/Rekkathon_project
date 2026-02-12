🧬 GenomeGuard — AI-Powered Genetic Disease Predictor (Enterprise Edition)

GenomeGuard is an AI-based system that analyzes human genomic data (VCF files) to predict the risk of genetic diseases such as cancer, Alzheimer's, and inherited disorders.
Featuring a secure backend with user authentication, MongoDB database, and RESTful API architecture for scalable deployment.

## 🚀 Quick Start

```bash
# Clone and start with Docker (Recommended)
git clone https://github.com/username/GenomeGuard.git
cd GenomeGuard
docker-compose up -d

# Access the application
# Dashboard: http://localhost:8501
# API: http://localhost:8000/docs
```

🚀 Key Features

✅ **Secure Backend Architecture**
- FastAPI REST API with JWT authentication
- MongoDB database for scalable data storage
- User management and access control
- Background task processing

✅ **Genomic Analysis Pipeline**
- VCF file processing and variant extraction
- Disease-specific variant annotation
- Machine learning risk prediction (XGBoost)
- Comprehensive reporting and visualization

✅ **Enterprise Features**
- Multi-user support with personal dashboards
- Analysis history and result management
- Secure file upload and storage
- RESTful API for integration
- Docker containerization support




## ⚙️ Installation & Setup

### Option 1: Docker Deployment (Recommended)

```bash
# Clone repository
git clone https://github.com/username/GenomeGuard.git
cd GenomeGuard

# Start services with Docker
docker-compose up -d

# Access the application
# Frontend: http://localhost:8501
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## ▶️ Using GenomeGuard

### 1. Access the Application
- **Frontend Dashboard**: http://localhost:8501
- **API Documentation**: http://localhost:8000/docs
- **Backend API**: http://localhost:8000

### 2. User Workflow
1. **Register/Login**: Create account or login to existing account
2. **Upload VCF**: Upload your genomic data file (.vcf format)
3. **Analysis**: System automatically processes and analyzes variants
4. **Results**: View risk predictions and detailed reports
5. **History**: Access previous analyses and results

### 3. API Usage
```python
import requests

# Login
response = requests.post("http://localhost:8000/auth/token", 
                        data={"username": "user", "password": "pass"})
token = response.json()["access_token"]

# Upload VCF
headers = {"Authorization": f"Bearer {token}"}
files = {"file": open("sample.vcf", "rb")}
response = requests.post("http://localhost:8000/analysis/upload", 
                        headers=headers, files=files)
```



### Prerequisites
```bash
# Install development dependencies
pip install -r requirements.txt
python scripts/train.py  # Train ML model
```

### Running Tests
```bash
pytest tests/ -v
```

### Code Formatting
```bash
black backend/ app/ tests/
flake8 backend/ app/ tests/
```

### Database Management
```bash
# Access MongoDB shell
docker exec -it genomeguard-mongo mongosh

# Backup database
mongodump --host localhost:27017 --db genomeguard --out backup/

# Restore database
mongorestore --host localhost:27017 --db genomeguard backup/genomeguard/
```

## 📝 API Documentation

Once the backend is running, visit http://localhost:8000/docs for interactive API documentation.

### Key Endpoints:
- `POST /auth/register` - User registration
- `POST /auth/token` - User login
- `GET /auth/me` - Get current user
- `POST /analysis/upload` - Upload VCF file
- `GET /analysis/results/{id}` - Get analysis results
- `GET /analysis/history` - Get user's analysis history
- `DELETE /analysis/results/{id}` - Delete analysis

### Response Examples:
```json
// Analysis Result
{
  "id": "analysis_id",
  "status": "completed",
  "risk_probability": 0.75,
  "risk_classification": "high",
  "total_variants": 1250,
  "high_risk_variants": 15
}
```


This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Issues**: Report bugs via GitHub Issues
- **Documentation**: Full API docs at `/docs` endpoint
- **Community**: Join our discussions for help and updates
