FROM python:3.10
COPY . /LocalGPT/.
WORKDIR /LocalGPT/
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "src/main.py"]
