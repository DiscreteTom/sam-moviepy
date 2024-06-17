FROM public.ecr.aws/lambda/python:3.12

# for python <= 3.11, use yum
# RUN yum install -y ImageMagick
# for python >= 3.12, use dnf
RUN dnf install -y ImageMagick

COPY requirements.txt ./
RUN python3.12 -m pip install -r requirements.txt -t .

COPY app.py ./
COPY buggy.mp4 ./

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
