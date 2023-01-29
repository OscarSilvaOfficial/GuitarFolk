# Use an official Node.js image as the base image
FROM node:19-alpine

WORKDIR /usr/src/app

COPY . .

RUN yarn

CMD [ "yarn", "dev" ]
