### test ci mehdi
# DoorDash Delivery Fee Service (FastAPI)

This is a simple FastAPI application that simulates DoorDash's delivery fee calculation service.
It provides three endpoints to calculate delivery fees, estimate delivery time, and check the service status.

## API Endpoints

1. **GET /** - Welcome message
2. **POST /calculate-fee/** - Calculate delivery fee based on distance and weight
3. **GET /estimate-time/{distance_km}** - Estimate delivery time based on distance
4. **GET /status/** - Check the service status

## Running the App

1. Build the Docker image:
    ```bash
    docker build -t doordash/delivery-fee-service .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8080:8080 doordash/delivery-fee-service
    ```

3. Access the application:
    - Go to `http://localhost:8080` for the welcome message.
    - Use `/calculate-fee/` to calculate fees, `/estimate-time/{distance_km}` to estimate delivery times, and `/status/` to check the status.

## Example Request

### POST /calculate-fee/
```json
{
  "distance_km": 10.5,
  "weight_kg": 2.0
}
```

### Example Response
```json
{
  "delivery_fee": 22.75
}
```
