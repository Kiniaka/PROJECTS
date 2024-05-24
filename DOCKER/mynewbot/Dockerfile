FROM python:3.11
ENV MY-BOT /app
WORKDIR $MY-BOT
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "mynewbot.py"]