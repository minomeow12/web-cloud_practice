FROM python:3.11-slim

#create working directory
WORKDIR /app



#copy app files
COPY . .

#install packages
RUN pip3 install -r requirements.txt

#expose to port 8080
EXPOSE 8080

#start flask
CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT:-8080} app:app"]