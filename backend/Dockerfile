FROM python:3
WORKDIR /Users/thangle/Documents/test/backend
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x ./start.sh
EXPOSE 8000
CMD ["./start.sh"]
