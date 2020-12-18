package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func part1(mask string, val uint64) uint64 {
	for i, c := range mask {
		if c == '0' {
			val &= ^(1 << (len(mask) - i - 1))
		} else if c == '1' {
			val |= (1 << (len(mask) - i - 1))
		}
	}

	return val
}

func part2_bit(mask string, val uint64, xidxs map[int]bool) uint64 {
	for i, c := range mask {
		if _, ok := xidxs[i]; ok {
			if c == '0' {
				val &= ^(1 << (len(mask) - i - 1))
			} else if c == '1' {
				val |= (1 << (len(mask) - i - 1))
			}
		} else if c == '1' {
			val |= (1 << (len(mask) - i - 1))
		}
	}

	return val
}

func generate_numbers(idx uint64, mask string, xidxs map[int]bool) []uint64 {
	slices := []uint64{}

	if !strings.ContainsAny(mask, "X") {
		slices = append(slices, part2_bit(mask, idx, xidxs))
		return slices
	}

	xIdx := strings.Index(mask, "X")
	xidxs[xIdx] = true
	mask = mask[:xIdx] + "0" + mask[xIdx+1:]
	slices = append(slices, generate_numbers(idx, mask, xidxs)...)
	mask = mask[:xIdx] + "1" + mask[xIdx+1:]
	slices = append(slices, generate_numbers(idx, mask, xidxs)...)

	return slices
}

func part2(mask string, idx uint64, val uint64, memory map[uint64]uint64) {
	xidxs := make(map[int]bool)
	for _, addr := range generate_numbers(idx, mask, xidxs) {
		memory[addr] = val
	}
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	var mask string = ""
	var idx uint64
	var val uint64

	memory1 := make(map[uint64]uint64)
	memory2 := make(map[uint64]uint64)

	maskline, _ := regexp.Compile("^mask = [01X]{36}$")
	mem, _ := regexp.Compile("^mem\\[[1-9][0-9]+\\]")
	v, _ := regexp.Compile("[1-9][0-9]*$")

	var line string

	for scanner.Scan() {
		line = scanner.Text()

		if maskline.MatchString(line) {
			mask = strings.Split(line, " ")[2]
		} else {
			idx, _ = strconv.ParseUint(strings.TrimRight(strings.TrimLeft(mem.FindString(line), "mem["), "]"), 10, 64)
			val, _ = strconv.ParseUint(v.FindString(line), 10, 64)

			memory1[idx] = part1(mask, val)
			part2(mask, idx, val, memory2)
		}
	}

	var sum uint64 = 0
	for _, v := range memory1 {
		sum += v
	}
	fmt.Println(sum)
	sum = 0
	for _, v := range memory2 {
		sum += v
	}
	fmt.Println(sum)
}
