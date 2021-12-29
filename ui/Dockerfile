FROM node:17-alpine

# set workin-directory
WORKDIR /app/ui

ENV PATH /app/node_modules/.bin:$PATH

#add app
COPY ./ ./

RUN npm install
RUN npm install react-scripts -g
