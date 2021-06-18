FROM python:alpine3.6
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]