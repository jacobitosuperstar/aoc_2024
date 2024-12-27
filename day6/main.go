package main

import (
	"bufio"
	"fmt"
	"os"
	// "strconv"
	// "strings"
	// "math"
	// "slices"
)


func FileReader(filepath string) *bufio.Scanner {
  file, err := os.Open(filepath)
  if err != nil {
      panic(err)
  }
  return bufio.NewScanner(file)
}

// checks if a [2]int vector is contained within a [][2]int slice
func vectorInSlice(a [2]int, b [][2]int) bool {
    for _, v := range b {
        if a == v {
            return true
        }
    }
    return false
}

// checks if we are at the edge of the map
func mapEdge(guardMap [][]rune, pos [2]int, dir string) bool {
    if pos[0] <= 0 && dir == "UP" {
        return true
    }
    if pos[0] >= len(guardMap)-1 && dir == "DOWN" {
        return true
    }
    if pos[1] <= 0 && dir == "LEFT" {
        return true
    }
    if pos[1] >= len(guardMap[0])-1 && dir == "RIGHT" {
        return true
    }
    return false
}

func Processor(filebuffer *bufio.Scanner) int {
    var charMatrix [][]rune
    for filebuffer.Scan() {
        line := filebuffer.Text()
        var rowChar []rune
        for _, r := range line {
            rowChar = append(rowChar, r)
        }
        charMatrix = append(charMatrix, rowChar)
    }
    // finding the guard
    initialDirection := "UP"
    // when does the guard stops??
    guardState := "WALKING"
    var guardPos [2]int
    var obstacles [][2]int
    // row
    for i := range charMatrix {
        // column
        for j := range charMatrix[i] {
            if charMatrix[i][j] == '#' {
                obstaclePos := [2]int{i, j}
                obstacles = append(obstacles, obstaclePos)
            }
            if charMatrix[i][j] == '^' {
                guardPos[0] = i
                guardPos[1] = j
            }
        }
    }
    // Unique positons counter
    var uniquePos [][2]int

    for guardState == "WALKING" {
        for guardPos[0] >= 0 && initialDirection == "UP" {
            // uniquePos = append(uniquePos, guardPos)
            if !vectorInSlice(guardPos, uniquePos) {
                uniquePos = append(uniquePos, guardPos)
            }
            n_guardPos := [2]int{guardPos[0]-1, guardPos[1]}
            if vectorInSlice(n_guardPos, obstacles) {
                initialDirection = "RIGHT"
                break
            }
            guardPos[0] -= 1
        }
        for guardPos[1] < len(charMatrix[0]) && initialDirection == "RIGHT" {
            // uniquePos = append(uniquePos, guardPos)
            if !vectorInSlice(guardPos, uniquePos) {
                uniquePos = append(uniquePos, guardPos)
            }
            n_guardPos := [2]int{guardPos[0], guardPos[1]+1}
            if vectorInSlice(n_guardPos, obstacles) {
                initialDirection = "DOWN"
                break
            }
            guardPos[1] += 1
        }
        for guardPos[0] < len(charMatrix) && initialDirection == "DOWN" {
            // uniquePos = append(uniquePos, guardPos)
            if !vectorInSlice(guardPos, uniquePos) {
                uniquePos = append(uniquePos, guardPos)
            }
            n_guardPos := [2]int{guardPos[0]+1, guardPos[1]}
            if vectorInSlice(n_guardPos, obstacles) {
                initialDirection = "LEFT"
                break
            }
            guardPos[0] += 1
        }
        for guardPos[1] >= 0 && initialDirection == "LEFT" {
            // uniquePos = append(uniquePos, guardPos)
            if !vectorInSlice(guardPos, uniquePos) {
                uniquePos = append(uniquePos, guardPos)
            }
            n_guardPos := [2]int{guardPos[0], guardPos[1]-1}
            if vectorInSlice(n_guardPos, obstacles) {
                initialDirection = "UP"
                break
            }
            guardPos[1] -= 1
        }
        if mapEdge(charMatrix, guardPos, initialDirection) {
            guardState = "STOP"
            break
        }
    }
    fmt.Println(obstacles)
    fmt.Println("rows: ", len(charMatrix))
    fmt.Println("cols: ", len(charMatrix[0]))
    return len(uniquePos)
}


func main() {
  filepath := os.Args[1]
  file := FileReader(filepath)
  state := Processor(file)
  fmt.Println("UniquePos: ", state)
}
