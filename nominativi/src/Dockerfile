FROM python:3.12
WORKDIR /src
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY app1.py /src/app1.py
COPY templates /src/templates
CMD python app1.py
