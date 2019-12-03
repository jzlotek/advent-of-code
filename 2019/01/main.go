// Advent of Code 2019
// Day 1

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func fuel(mass float64) float64 {
	fuel := math.Floor(mass/3) - 2

	extra := fuel
	for {
		extra = math.Floor(extra/3) - 2
		if extra <= 0 {
			break
		}
		fuel += extra
	}

	return fuel
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	sum := float64(0)

	for input.Scan() {
		num, err := strconv.Atoi(input.Text())

		if err == nil {
			sum += fuel(float64(num))
		}
	}

	fmt.Println(int(sum))
}
