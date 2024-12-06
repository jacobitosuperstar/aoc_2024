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
  // defer file.Close()
  return bufio.NewScanner(file)
}


func Processor(filebuffer *bufio.Scanner) int {
    var charMatrix [][]rune
    for filebuffer.Scan() {
        line := filebuffer.Text()
        var rowChar []rune
        for _, r := range line {
            // char := strconv.QuoteRune(r)
            rowChar = append(rowChar, r)
        }
        charMatrix = append(charMatrix, rowChar)
    }
    // fmt.Println(charMatrix)

    // We will check how the chars are distributed within the Matrix.
    // rows
    r := len(charMatrix)
    // columns
    c := len(charMatrix[0])
    // XMAS counter
    // fmt.Println(r, c)
    counter := 0
    for i := range r {
        // fmt.Println("row: ", i)
        for j := range c {
            // in line left to rigth
            if j + 3 < c && charMatrix[i][j] == 'X' && charMatrix[i][j+1] == 'M' && charMatrix[i][j+2] == 'A' && charMatrix[i][j+3] == 'S' {
                counter += 1
            }
            // in line right to left
            if j - 3 >= 0 && charMatrix[i][j] == 'X' && charMatrix[i][j-1] == 'M' && charMatrix[i][j-2] == 'A' && charMatrix[i][j-3] == 'S' {
                counter += 1
            }
            // up to down
            if i + 3 < r && charMatrix[i][j] == 'X' && charMatrix[i+1][j] == 'M' && charMatrix[i+2][j] == 'A' && charMatrix[i+3][j] == 'S' {
                counter += 1
            }
            // down to up
            if i - 3 >= 0 && charMatrix[i][j] == 'X' && charMatrix[i-1][j] == 'M' && charMatrix[i-2][j] == 'A' && charMatrix[i-3][j] == 'S' {
                counter += 1
            }
            // diagonal left to right
            if i + 3 < r && j + 3 < c && charMatrix[i][j] == 'X' && charMatrix[i+1][j+1] == 'M' && charMatrix[i+2][j+2] == 'A' && charMatrix[i+3][j+3] == 'S' {
                counter += 1
            }
            // diagonal left to right
            if i - 3 >= 0 && j - 3 >= 0 && charMatrix[i][j] == 'X' && charMatrix[i-1][j-1] == 'M' && charMatrix[i-2][j-2] == 'A' && charMatrix[i-3][j-3] == 'S' {
                counter += 1
            }
            // diagonal left to right
            if i + 3 < r && j - 3 >= 0 && charMatrix[i][j] == 'X' && charMatrix[i+1][j-1] == 'M' && charMatrix[i+2][j-2] == 'A' && charMatrix[i+3][j-3] == 'S' {
                counter += 1
            }
            // diagonal left to right
            if i - 3 >= 0 && j + 3 < c && charMatrix[i][j] == 'X' && charMatrix[i-1][j+1] == 'M' && charMatrix[i-2][j+2] == 'A' && charMatrix[i-3][j+3] == 'S' {
                counter += 1
            }
        }
    }
    return counter
}


func ProcessorPt2(filebuffer *bufio.Scanner) int {
    var charMatrix [][]rune
    for filebuffer.Scan() {
        line := filebuffer.Text()
        var rowChar []rune
        for _, r := range line {
            // char := strconv.QuoteRune(r)
            rowChar = append(rowChar, r)
        }
        charMatrix = append(charMatrix, rowChar)
    }
    // fmt.Println(charMatrix)

    // We will check how the chars are distributed within the Matrix.
    // rows
    r := len(charMatrix)
    // columns
    c := len(charMatrix[0])
    // XMAS counter
    fmt.Println(r, c)
    counter := 0
    for i := range r {
        // fmt.Println("row: ", i)
        for j := range c {
            // MMASS
            if i + 1 < r && j + 1 < c && i - 1 >=0 && j - 1 >= 0 && charMatrix[i-1][j-1] == 'M' && charMatrix[i-1][j+1] == 'M' && charMatrix[i][j] == 'A' && charMatrix[i+1][j-1] == 'S' && charMatrix[i+1][j+1] == 'S' {
                counter += 1
            }
            // SSAMM
            if i + 1 < r && j + 1 < c && i - 1 >=0 && j - 1 >= 0 && charMatrix[i-1][j-1] == 'S' && charMatrix[i-1][j+1] == 'S' && charMatrix[i][j] == 'A' && charMatrix[i+1][j-1] == 'M' && charMatrix[i+1][j+1] == 'M' {
                counter += 1
            }
            // SMASM
            if i + 1 < r && j + 1 < c && i - 1 >=0 && j - 1 >= 0 && charMatrix[i-1][j-1] == 'S' && charMatrix[i-1][j+1] == 'M' && charMatrix[i][j] == 'A' && charMatrix[i+1][j-1] == 'S' && charMatrix[i+1][j+1] == 'M' {
                counter += 1
            }
            // MSAMS
            if i + 1 < r && j + 1 < c && i - 1 >=0 && j - 1 >= 0 && charMatrix[i-1][j-1] == 'M' && charMatrix[i-1][j+1] == 'S' && charMatrix[i][j] == 'A' && charMatrix[i+1][j-1] == 'M' && charMatrix[i+1][j+1] == 'S' {
                counter += 1
            }
        }
    }
    return counter
}


func main() {
  filepath := os.Args[1]
  file := FileReader(filepath)
  // state := Processor(file)
  // fmt.Println("Count PT1: ", state)
  state := ProcessorPt2(file)
  fmt.Println("Count PT2: ", state)
}
