.PHONEY: build run clean

build: 01.go
	go build 01.go

run: build
	cat input | ./01

clean:
	-rm ./01