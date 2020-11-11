FROM python:alpine
COPY . /app
#COPY internetten bir dosya cekemez,bunun icin ADD kullaniriz
WORKDIR /app
RUN pip install -y reqirements.txt
EXPOSE 80
CMD ["python", "bookstore-api.py"]