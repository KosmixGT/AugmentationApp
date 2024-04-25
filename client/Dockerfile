# Dockerfile for frontend service

# Use the official Node.js image from Docker Hub
FROM node:16

# Set the working directory in the container
WORKDIR /app

RUN npm install @vue/cli@5.0.8 -g

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application's code to the working directory
COPY . .

# Command to run the application
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

