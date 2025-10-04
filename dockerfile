# Dockerfile
FROM node:18-alpine

WORKDIR /app
COPY frontend/ ./

# Устанавливаем serve для статического хостинга
RUN npm install -g serve

EXPOSE 3000

CMD ["serve", "-s", ".", "-l", "3000"]