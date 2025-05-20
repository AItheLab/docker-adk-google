# Google Agent Development Kit - Dockerized Application

This project demonstrates a Dockerized application using the Google Agent Development Kit with two simple agents: `EchoAgent` and `ReverseAgent`.

## Prerequisites

- Docker installed and running on your system.
- Docker Compose (usually included with Docker Desktop).

## Project Structure

- `app/`: Contains the main application code.
  - `agents/`: Houses the agent implementations.
    - `echo_agent.py`: Implements an agent that echoes back input.
    - `reverse_agent.py`: Implements an agent that reverses input strings.
    - `__init__.py`: Makes agents importable.
  - `main.py`: The main application script that initializes and runs the agents using the Google Agent Development Kit.
- `Dockerfile`: Defines the Docker image for the application, including Python, the Google Agent Development Kit, and dependencies.
- `docker-compose.yml`: Configures the Docker Compose setup for easy building and running of the application.
- `requirements.txt`: Python package dependencies (currently empty as ADK is installed directly in Dockerfile).

## Building and Running the Application

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Build and run the application using Docker Compose:**
    Open a terminal in the project's root directory and run:
    ```bash
    docker-compose up --build
    ```
    This command will:
    - Build the Docker image based on the `Dockerfile`.
    - Start a container based on that image.
    - Forward port 8080 from the container to port 8080 on your host machine.
    - Mount the local `./app` directory into the container for live code reloading.

3.  **Accessing the Agents:**
    Once the application is running, the `main.py` script will attempt to start a server (e.g., a web server) using the Google Agent Development Kit, exposing the agents on port 8080.

    The exact method for interacting with the agents (e.g., API endpoints, specific client libraries) depends on the features provided by the Google Agent Development Kit's `run_app` function.

    If `run_app` starts a web server, you would typically interact with agents via HTTP requests. For example:
    - `EchoAgent` might be available at an endpoint like `http://localhost:8080/echo`
    - `ReverseAgent` might be available at an endpoint like `http://localhost:8080/reverse`

    Check the console output when `docker-compose up` is run. The `main.py` script or the Agent Development Kit might print messages indicating how to access the agents or the URLs they are served on.

    If the `run_app` command in `main.py` fails or if the Agent Development Kit does not automatically start a server, the `main.py` script will fall back to a simple test execution in the console, printing the output of `EchoAgent` and `ReverseAgent` with a sample string. In this case, there won't be a running server.

## Development

- The volume mount in `docker-compose.yml` allows you to modify the code in the `app/` directory on your host machine, and the changes should be reflected in the running container (often requiring a restart of the Python process if the framework doesn't support hot-reloading).
- You can install additional Python dependencies by adding them to `requirements.txt` and rebuilding the Docker image (`docker-compose up --build`).

## Agents

-   **EchoAgent**: Responds with the exact message it receives.
-   **ReverseAgent**: Responds with the reversed version of the message it receives.

The application is configured to use `gemini-2.0-flash` as specified in the `main.py` for the `run_app` function, though the current agents do not utilize an LLM.
