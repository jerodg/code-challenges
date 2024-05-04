// Package main provides a solution to the problem of calculating the maximum sum of hourglass in a 2D array.
//
// This particular file provides a solution to the problem from HackerRank.
package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
	"strings"
)

// hourglassSum calculates the maximum sum of hourglass in a 2D array.
//
// It accepts one parameter:
// - arr: a 2D array of integers.
//
// The function returns an integer representing the maximum sum of hourglass in the array.
//
// The function iterates over the array, calculating the sum of hourglass for each element and keeping track
// of the maximum sum found.
//
// Time complexity analysis:
// - Best-case: O(n^2), when the array has only one element.
// - Worst-case: O(n^2), when the array is full.
// - Average-case: O(n^2), as we always have to iterate over each element of the array.
func hourglassSum(arr [][]int32) int32 {
	maxSum := int32(math.MinInt32)
	for i := 1; i < 5; i++ {
		for j := 1; j < 5; j++ {
			top := arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
			mid := arr[i][j]
			bottom := arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
			hourglassSum := top + mid + bottom
			if hourglassSum > maxSum {
				maxSum = hourglassSum
			}
		}
	}
	return maxSum
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer func(stdout *os.File) {
		err := stdout.Close()
		if err != nil {
			panic(err)
		}
	}(stdout)

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	var arr [][]int32
	for i := 0; i < 6; i++ {
		arrRowTemp := strings.Split(strings.TrimRight(readLine(reader), " \t\r\n"), " ")

		var arrRow []int32
		for _, arrRowItem := range arrRowTemp {
			arrItemTemp, err := strconv.ParseInt(arrRowItem, 10, 64)
			checkError(err)
			arrItem := int32(arrItemTemp)
			arrRow = append(arrRow, arrItem)
		}

		if len(arrRow) != 6 {
			panic("Bad input")
		}

		arr = append(arr, arrRow)
	}

	result := hourglassSum(arr)

	fmt.Fprintf(writer, "%d\n", result)

	err = writer.Flush()
	if err != nil {
		return
	}
}

// readLine reads a line from the provided reader and returns it as a string.
func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

// checkError checks if the provided error is nil. If it's not, it panics with the error.
func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
