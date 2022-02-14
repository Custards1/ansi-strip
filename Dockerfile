FROM python:3.9

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./src ./src
COPY ./frontend ./frontend
ENV HUFIT_DB_CONNECTION=$HUFIT_DB_CONNECTION
CMD ["python","-m","uvicorn","src.main:app","--host","0.0.0.0","--port","8000"]
EXPOSE 8000