FROM ubuntu:16.04

# Install needed things
RUN apt update -y && apt install python3-pip git -y

RUN mkdir /thunderwagon
WORKDIR /thunderwagon

# Copy app
COPY webapp .

# Install required things
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 5000

# Start application
CMD ["/usr/bin/python3","run.py"]