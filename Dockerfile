FROM python:3.6.8-jessie
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]