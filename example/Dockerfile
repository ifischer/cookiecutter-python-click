FROM python:3.7
RUN pip install --upgrade setuptools pip

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/code

WORKDIR /code
COPY requirements.txt .
COPY requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . /code

RUN mkdir -p $(python -m site --user-site)
RUN cd $(python -m site --user-site) && python /code/setup.py develop

# Configure IPython
COPY config/ipython/ipython_config.py /root/.ipython/profile_default/
COPY config/ipython/startup.py /root/.ipython/profile_default/startup/

