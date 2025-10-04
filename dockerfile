FROM node:18-alpine

WORKDIR /frontend/html

# Копируем зависимости для кэширования
COPY frontend/package.json ./
RUN npm install

# Копируем все файлы фронтенда
COPY frontend/ ./

EXPOSE 3000

CMD ["node", "server.js"]