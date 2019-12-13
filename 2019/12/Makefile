.PHONEY: build run clean

build: main.go
	go build main.go

run: build
	cat input | ./main

clean:
	-rm ./main
