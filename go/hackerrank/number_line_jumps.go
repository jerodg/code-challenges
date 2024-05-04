// Package main provides a solution to the problem of determining if two kangaroos on a number line can land at the same spot.
//
// This particular file provides a solution to the problem from HackerRank.
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// kangaroo determines if two kangaroos on a number line can land at the same spot.
//
// It accepts four parameters:
// - x1: an integer representing the starting position of the first kangaroo.
// - v1: an integer representing the jump distance of the first kangaroo.
// - x2: an integer representing the starting position of the second kangaroo.
// - v2: an integer representing the jump distance of the second kangaroo.
//
// The function returns a string "YES" if the two kangaroos can land at the same spot, and "NO" otherwise.
//
// The function calculates if the difference in the start positions and jump distances can result in the kangaroos landing at the same spot.
//
// Time complexity analysis:
// - Best-case: O(1), as the calculation is done in constant time.
// - Worst-case: O(1), as the calculation is done in constant time.
// - Average-case: O(1), as the calculation is done in constant time.
func kangaroo(x1 int32, v1 int32, x2 int32, v2 int32) string {
	if v1 == v2 {
		if x1 == x2 {
			return "YES"
		}
		return "NO"
	}
	if (x2-x1)%(v1-v2) == 0 && (x2-x1)/(v1-v2) > 0 {
		return "YES"
	}
	return "NO"
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	x1Temp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	x1 := int32(x1Temp)

	v1Temp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	v1 := int32(v1Temp)

	x2Temp, err := strconv.ParseInt(firstMultipleInput[2], 10, 64)
	checkError(err)
	x2 := int32(x2Temp)

	v2Temp, err := strconv.ParseInt(firstMultipleInput[3], 10, 64)
	checkError(err)
	v2 := int32(v2Temp)

	result := kangaroo(x1, v1, x2, v2)

	fmt.Fprintf(writer, "%s\n", result)

	writer.Flush()
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
