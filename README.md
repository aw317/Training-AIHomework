Repository contains ping and receiver REST APi

### api/ping

contains logic to ping given url.

To see documentation visit
```localhost:8080/api/v1```

### api/receiver

test service for ping

### Run

To run project:
```
sudo docker-compose up
```

### Tests

Create virtualenv and activate it

```
pip install -r requirements
cd api &&  python -m pytest
```

