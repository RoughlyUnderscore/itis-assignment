# syntax=docker/dockerfile:1

FROM python:3.11-slim

# Установим рабочую директорию
WORKDIR /app

# Копируем только файлы зависимостей
COPY pyproject.toml requirements.txt ./

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install -e .[dev]

# Копируем весь проект
COPY src/ src/
COPY scripts/ scripts/
COPY data/ data/

# Точка входа
ENTRYPOINT ["python", "scripts/generate_report.py"]

# Пример запуска по умолчанию
CMD ["--input", "data/sample_students.csv", "--output", "report.html"]