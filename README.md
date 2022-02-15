## Sample python Flask "ping" and "pong" services
### Steps
1. Build docker image for "ping" service
`docker build -t ping-service .`
2. Build docker image for "pong" service
`docker build -t pong-service .`
3. Run the "ping" service in a dedicated Docker container
`docker run --name ping-service-container -p 5000:5000 ping-service`
4. Run the "pong" service in a dedicated Docker container
`docker run --name pong-service-container -p 5001:5001 pong-service`
5. Verify that "ping" and "pong" services are reachable from host
`curl http://localhost:5000` `curl http://localhost:5001`
6. Verify that "ping" service cannot reach "pong" service
`curl http://localhost:5000/ping`
7. Create docker network
`docker network create network ping-pong-netowrk`
`docker network ls`
`docker network inspect ping-pong-network`
8. Add the "ping" and "pong" service containers to the network
`docker netowrk connect ping-pong-network ping-service-container`
`docker netowrk connect ping-pong-network pong-service-container`
9. Verify that containers are in the network
`docker network inspect ping-pong-network`
10. Verify that "ping" service service can now query "pong" service
`curl http://localhost:5000/ping`
11. Stop the "pong" service and verify that it's removed from Docker network
12. Run the "pong" service again and it back to the network
