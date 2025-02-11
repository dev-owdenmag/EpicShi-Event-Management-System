# Use official Node.js image
FROM node:18

# Set working directory inside container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy frontend files
COPY . .

# Build the React app
RUN npm run build

# Expose frontend port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
