## Introduction

A dynamic sticker price calculator for both **fixed** and **custom quantities**.

The calculator updates prices dynamically based on the selected sticker dimensions or quantity, allowing users to either choose from predefined quantities or enter a custom amount.

## Approach

The main challenge of this project was translating an **empirically defined pricing strategy into a mathematical model**. The client did not use an explicit formula to determine prices, so I first gathered a small set of representative pricing examples by asking for quotes across different sticker dimensions and quantities. From this limited data, I derived a pricing function that reproduced the desired pricing behavior and used it as the basis of the calculator.

The actual pricing algorithm has intentionally been excluded from the repository, as it was developed for real-world commercial use. The version published here uses a dummy pricing function while preserving the rest of the application's functionality.

## Demo

A demonstration of the calculator using the **actual pricing function** is available on YouTube:

[![Sticker Price Calculator Demo](https://img.youtube.com/vi/Yugdgtk8U_U/maxresdefault.jpg)](https://www.youtube.com/watch?v=Yugdgtk8U_U)

## Technologies

- **Python** — pricing logic and backend
- **Flask** — API
- **Docker** — containerization
- **Tailwind CSS** — frontend styling

The frontend was intentionally kept minimal and was generated with LLM assistance. The focus of this project was the **mathematical modeling and backend implementation**, rather than frontend development.

## Running the Project

[Docker](https://www.docker.com/) with Docker Compose is required.

Clone the repository (or download it) and navigate to the project directory:

```bash
cd /path/to/project
```

Build and start the application:

```bash
docker compose up --build
```

> On Linux, you may need to prefix this command with `sudo`, depending on your Docker configuration.

Then open the following address in your browser:

[http://localhost:8080/](http://localhost:8080/)
