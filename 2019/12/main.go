// Advent of Code 2020
// Day 12

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Triple struct {
	X int
	Y int
	Z int
}

type Moon struct {
	pos Triple
	vel Triple
}

func convToInt(l string) int {
	i, err := strconv.Atoi(strings.Split(l, "=")[1])
	if err != nil {
		return -1
	}
	return i
}

func Gcd(m int, n int) int {
	if n == 0 {
		return m
	}
	return Gcd(n, m%n)
}

func Lcm(m int, n int) int {
	return m * n / Gcd(m, n)
}

func GetDiff(m int, n int) int {
	if m > n {
		return -1
	} else if m < n {
		return 1
	} else {
		return 0
	}
}
func (t *Triple) GetMag() int {
	return int(math.Abs(float64(t.X)) + math.Abs(float64(t.Y)) + math.Abs(float64(t.Z)))
}

func (m *Moon) ApplyGravity(n Moon) {
	m.vel.X += GetDiff(m.pos.X, n.pos.X)
	m.vel.Y += GetDiff(m.pos.Y, n.pos.Y)
	m.vel.Z += GetDiff(m.pos.Z, n.pos.Z)
}

func (m *Moon) AddVel() {
	m.pos.X += m.vel.X
	m.pos.Y += m.vel.Y
	m.pos.Z += m.vel.Z
}
func (m *Moon) GetEnergy() int {
	return m.pos.GetMag() * m.vel.GetMag()
}

func IterateMoons(moons *[]Moon) {
	for i := 0; i < len(*moons); i++ {
		for j := 0; j < len(*moons); j++ {
			if i != j {
				(*moons)[i].ApplyGravity((*moons)[j])
			}
		}
	}
	for i := 0; i < len(*moons); i++ {
		(*moons)[i].AddVel()
	}
}

func GetCoord(v Triple, i int) int {
	switch i {
	case 0:
		return v.X
	case 1:
		return v.Y
	case 2:
		return v.Z
	default:
		panic("Invalid Index")
	}
}

func main() {
	var moons []Moon
	var part2 []Moon
	var originalMoons []Moon
	input := bufio.NewScanner(os.Stdin)
	zero := Triple{0, 0, 0}

	for input.Scan() {

		line := strings.ReplaceAll(strings.ReplaceAll(input.Text(), ">", ""), "<", "")
		splitLine := strings.Split(line, ", ")

		pos := Triple{convToInt(splitLine[0]), convToInt(splitLine[1]), convToInt(splitLine[2])}
		moons = append(moons, Moon{pos, zero})
		part2 = append(part2, Moon{pos, zero})
		originalMoons = append(originalMoons, Moon{pos, zero})
	}

	for i := 0; i < 1000; i++ {
		IterateMoons(&moons)
	}
	sum := 0
	for i := 0; i < len(moons); i++ {
		sum += moons[i].GetEnergy()
	}
	fmt.Println(sum)

	// Part2
	var lcms map[int]int
	lcms = make(map[int]int)

	moons = part2
	count := 1
	for {
		count++
		IterateMoons(&moons)

		for i := 0; i < 3; i++ {
			_, inLcms := lcms[i]

			if GetCoord(moons[0].pos, i) == GetCoord(originalMoons[0].pos, i) && GetCoord(moons[1].pos, i) == GetCoord(originalMoons[1].pos, i) && GetCoord(moons[2].pos, i) == GetCoord(originalMoons[2].pos, i) && GetCoord(moons[3].pos, i) == GetCoord(originalMoons[3].pos, i) && !inLcms {
				lcms[i] = count
			}
		}
		if len(lcms) == 3 {
			break
		}
	}
	fmt.Println(Lcm(lcms[0], Lcm(lcms[1], lcms[2])))
}
