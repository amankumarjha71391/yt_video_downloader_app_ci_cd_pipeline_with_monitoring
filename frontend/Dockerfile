# Use an official Node.js image as the base image
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json
COPY frontend/package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the frontend project into the container
COPY frontend/ .

# Expose port for the frontend application (React typically uses 3000)
EXPOSE 3000

# Command to start the React development server
CMD ["npm", "start"]
