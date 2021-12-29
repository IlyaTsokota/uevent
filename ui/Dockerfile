FROM node:17-alpine

# set workin-directory
WORKDIR /app/ui

ENV PATH /app/ui/node_modules/.bin:$PATH

#add app
COPY ./package.json ./
COPY ./package-lock.json ./

RUN npm install
RUN npm install @craco/craco -g

COPY ./ ./

EXPOSE 3001