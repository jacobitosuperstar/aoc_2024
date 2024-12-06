package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
    "math"
    "strconv"
    "slices"
)


func FileReader(filepath string) *bufio.Scanner {
  file, err := os.Open(filepath)
  if err != nil {
      panic(err)
  }
  // defer file.Close()
  return bufio.NewScanner(file)
}

func ReportProcessor(filebuffer *bufio.Scanner) int {
    safe_counter := 0
    for filebuffer.Scan() {
        line := filebuffer.Text()
        // if LineProcessor(line) == "Safe" {
        //safe_counter += 1
        // }
        if LineProcessorPt2(line) == "Safe" {
            safe_counter += 1
        }
  }
  return safe_counter
}

// absolute distance
func AbsDistance(a, b int) float64 {
    return math.Abs(float64(a - b))
}

func LineProcessor(line string) string {
    var report_list  []string = strings.Split(line, " ")
    report_ints := make([]int, len(report_list))
    for i, s := range report_list {
        report_ints[i], _ = strconv.Atoi(s)
    }

    report_state := "Safe"
    // Check that the slice is sorted
    // sorted and inv sorted
    inv_report_ints := make([]int, len(report_ints))
    copy(inv_report_ints, report_ints)
    slices.Reverse(inv_report_ints)
    if (slices.IsSorted(inv_report_ints) || slices.IsSorted(report_ints)) {
        // check that the steps are not that big
        for i := 0; i < (len(report_ints) - 1); i++ {
            increment := AbsDistance(report_ints[i],report_ints[i+1])
            if (increment > 3 || increment == 0 ) {
                report_state = "Unsafe"
                break
            }
        }
    } else {
        report_state = "Unsafe"
    }
    return report_state
}

// ElementRemover
// deletes en element from an slice
func ElementDeleter(slice []int, index int) []int {
    var new_slice []int
    new_slice = append(new_slice, slice[:index]...)
    new_slice = append(new_slice, slice[index + 1:]...)
    return new_slice
}

// Adding the dampener
func LineProcessorPt2(line string) string {
    var report_list  []string = strings.Split(line, " ")
    report_ints := make([]int, len(report_list))
    for i, s := range report_list {
        report_ints[i], _ = strconv.Atoi(s)
    }

    // PT1 of the solution, this doesn't need to change a thing.
    // All of this validation is the same
    overall_state := "Safe"
    for j := range report_ints {
        // Check that the slice is sorted
        // sorted and inv sorted
        filtered_report := ElementDeleter(report_ints, j)
        inv_report_ints := make([]int, len(filtered_report))
        copy(inv_report_ints, filtered_report)
        slices.Reverse(inv_report_ints)
        report_state := "Safe"
        if (slices.IsSorted(inv_report_ints) || slices.IsSorted(filtered_report)) {
            // check that the steps are not that big
            for i := 0; i < (len(filtered_report) - 1); i++ {
                increment := AbsDistance(filtered_report[i], filtered_report[i+1])
                if (increment > 3 || increment == 0 ) {
                    report_state = "Unsafe"
                    overall_state = "Unsafe"
                    break
                }
            }
        } else {
            report_state = "Unsafe"
            overall_state = "Unsafe"
        }
        if report_state == "Safe" {
            overall_state = "Safe"
            break
        }
    }
    return overall_state
}

func main() {
  filepath := os.Args[1]
  file := FileReader(filepath)
  state := ReportProcessor(file)
  fmt.Println(state)
}
