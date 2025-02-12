FROM public.ecr.aws/lambda/python:3.13

RUN apt-get -y update \
    && apt-get -y --no-install-recommends install \
        git \
    && pip install --upgrade pip \
    && pip install --no-cache-dir \
        git+https://github.com/achillesrasquinha/upyog.git@upyog#egg=upyog \
    && apt-get remove --purge -y \
        git \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./handler.py ${LAMBDA_TASK_ROOT}

CMD [ "handler.handle" ]