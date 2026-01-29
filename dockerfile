FROM python:3.13.5
# Set the working directory to /app
WORKDIR /app
# Copy local contents into the container
ADD . /app
# install all required dependencies
RUN pip install -r requirements.txt
CMD ["python", "main.py"]