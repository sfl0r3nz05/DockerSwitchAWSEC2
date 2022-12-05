# Docker API to manage on/off AWS EC2 instances

- Creation of API based on Docker to manage AWS EC2 instances on/off.

## Demonstration

- Check this [youtube link for a video demonstration](https://youtu.be/DKFEdS1wlJU).

## Prerequisites

1. [Install docker on ubunu](https://docs.docker.com/engine/install/ubuntu/).
2. [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).
3. [Install docker compose on ubunu](https://docs.docker.com/compose/install/linux/).

## How to use

1. Rename `.env.example` as `.env`.
2. Set the enviromental variables:

    ```console
    AWS_ACCESS_KEY_ID=XXX
    AWS_SECRET_ACCESS_KEY=XXX
    AWS_SESSION_TOKEN=XXX
    REGION_NAME=XXX
    ```

3. Deploy the containers

    ```console
    docker compose up -d
    ```

4. Stop the containers

    ```console
    docker comopose down
    ```

## How to develop

1. Modify `docker-compose.yml` file:

    - From this line:

    ```console
    image: sflorenz05/api-aws-mngmt:v0.1
    ```

    - To this line:

    ```console
    build: api-ec2/
    ```

2. Repository structure

   - API-EC2

    ```console
    /api-ec2
        |_ /api
            |_ main.py
                |_ status_ec2.py
                |_ start_ec2.py
                |_ stop_ec2.py
    ```

   - Swagger
     - Modify `*.json` file to e.g., introduce new endpoints:

    ```console
    /swagger
        |_ swagger.json
    ```

3. Introduce new endpoints or improve improve existing ones
   1. Crete/modify the endpoint in `main.py` file.
   2. Crete/modify the fuctionality through files such as `start_ec2.py`.
