# INSTALL NODE IMAGE
FROM node:14.17.3-alpine

WORKDIR /app

COPY package.json ./

RUN npm install 

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]