FROM python:3.5.3-jessie
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]