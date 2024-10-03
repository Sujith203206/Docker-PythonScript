# Use Ubuntu as the base image
FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && apt-get install -y fortune cowsay && apt-get clean

# Copy the wisecow.sh script into the container
COPY wisecow.sh /usr/local/bin/wisecow.sh

# Make the script executable
RUN chmod +x /usr/local/bin/wisecow.sh

# Set the command to run the script
CMD ["/usr/local/bin/wisecow.sh"]
