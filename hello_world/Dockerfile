FROM public.ecr.aws/lambda/python:3.9

RUN yum install -y ImageMagick

COPY requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .

COPY app.py ./
COPY buggy.mp4 ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
