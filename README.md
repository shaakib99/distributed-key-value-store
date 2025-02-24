# Distributed Key-Value Store

A **FastAPI-based distributed key-value store** that provides a scalable and fault-tolerant solution for managing key-value pairs across multiple MySQL databases.

## Features

- **Distributed Storage**: Spreads data across multiple MySQL databases.
- **FastAPI-based API**: Provides a RESTful API for easy interaction.
- **Automatic Sharding**: Assigns keys dynamically across available databases following key range partitioning.
- **Docker Support**: Easily deployable using Docker and Docker Compose.
- **Database Metadata Management**: Manages database connections and key distribution.

## Architecture

The system consists of the following components:

1. **FastAPI Application**: Manages API requests and data operations.
2. **Database Service**: Handles interactions with MySQL databases.
3. **Database Metadata Manager**: Keeps track of available databases and key distribution.
4. **MySQL Databases**: Store the key-value pairs.

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.8+

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/shaakib99/distributed-key-value-store.git
   cd distributed-key-value-store
   ```

2. Start the services using Docker Compose:
   ```sh
   docker-compose up --build
   ```

3. The FastAPI application will be running at `http://localhost:8000`

## API Endpoints

### Key-Value Operations

| Method | Endpoint         | Description                 |
|--------|-----------------|-----------------------------|
| GET    | `/app/{id}`      | Retrieve a key-value pair   |
| GET    | `/app/`          | Retrieve all key-value pairs |
| POST   | `/app`          | Create a new key-value pair |
| PUT    | `/app/{id}`      | Update an existing entry   |
| DELETE | `/app/{id}`      | Delete a key-value pair    |

### Example Request

#### Create a Key-Value Pair
```sh
curl -X POST "http://localhost:8000/app" \
     -H "Content-Type: application/json" \
     -d '{"name": "example", "description": "An example entry"}'
```

#### Retrieve a Key-Value Pair
```sh
curl -X GET "http://localhost:8000/app/1"
```

## Database Sharding Strategy

- The **DatabaseMetadataManager** assigns key-value pairs to different MySQL instances from a **static key pool**.
- Each database is responsible for a range of key IDs.
- The system supports dynamic scaling by adding new database instances.

## Issues

- Does not support multi partition join.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

