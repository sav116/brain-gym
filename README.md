# Brain Gym Bot 🧠

**Brain Gym Bot** is a Telegram bot that provides math problems to help you warm up your brain. Whether you're looking to sharpen your mental math skills or just want a quick challenge, this bot has got you covered.

## Features

- 📊 Provides random arithmetic problems for brain exercises.
- 💡 Ideal for quick mental warm-ups.
- ⚙️ Easy deployment and setup on your server.

## Quick Start

### 1. Clone the Repository

Start by cloning the repository to your local machine or server:
```bash
git clone git@github.com:sav116/brain-gym.git
cd brain-gym
```

### 2. Configure Environment Variables
The bot uses a .env file to manage configuration. Rename the .env.dist file to .env and edit it with your specific values:
```bash
mv .env.dist .env
```

### 3. Deploy the Bot
Deploy the bot using the following command:
```bash
chmod +x deploy.sh
./deploy.sh
```

This will build the Docker image, start the container, and your bot will be up and running!
