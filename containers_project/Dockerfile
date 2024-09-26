# Use the Node.js image from DockerHub
FROM node:18

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Copy the wait-for-it script
COPY wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

# Expose the application port
EXPOSE 5000

# Start the Node.js application
CMD ["npm", "start"]

