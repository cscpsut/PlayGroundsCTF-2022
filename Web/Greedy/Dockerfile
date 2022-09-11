FROM golang:alpine

MAINTAINER Maintainer

ENV GIN_MODE=release
ENV PORT=3004


WORKDIR /go/src/go-docker-dev.to

COPY src /go/src/go-docker-dev.to/src
COPY templates /go/src/go-docker-dev.to/templates


RUN go mod init
RUN go get -u github.com/gin-gonic/gin
RUN apk update && apk add --no-cache git
RUN go get ./...

#COPY dependencies /go/src


RUN go build go-docker-dev.to/src/app

EXPOSE $PORT

ENTRYPOINT ["./app"]
