// Package main provides a solution to the problem of creating a dynamic array.
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

// dynamicArray creates a dynamic array and performs queries on it.
//
// It accepts two parameters:
// - n: an integer representing the number of empty sequences to initialize.
// - queries: a 2D array of integers representing the queries to perform.
//
// The function returns a slice of integers representing the results of each type 2 query.
//
// The function initializes n empty sequences and performs each query in order. If the query is of type 1,
// it appends a value to a sequence. If the query is of type 2, it appends the result of the query to the result slice.
//
// Time complexity analysis:
// - Best-case: O(q), when all queries are of type 1.
// - Worst-case: O(q), when all queries are of type 2.
// - Average-case: O(q), as we always have to perform each query.
func dynamicArray(n int32, queries [][]int32) []int32 {

	var seqList [][]int32
	var lastAnswer int32
	var result []int32

	for i := 0; i < int(n); i++ {
		seqList = append(seqList, []int32{})
	}

	for _, query := range queries {
		queryType := query[0]
		x := query[1]
		y := query[2]

		seqIndex := (x ^ lastAnswer) % n

		if queryType == 1 {
			seqList[seqIndex] = append(seqList[seqIndex], y)
		} else if queryType == 2 {
			seq := seqList[seqIndex]
			lastAnswer = seq[y%int32(len(seq))]
			result = append(result, lastAnswer)
		}
	}

	return result
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	nTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	n := int32(nTemp)

	qTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	q := int32(qTemp)

	var queries [][]int32
	for i := 0; i < int(q); i++ {
		queriesRowTemp := strings.Split(strings.TrimRight(readLine(reader), " \t\r\n"), " ")

		var queriesRow []int32
		for _, queriesRowItem := range queriesRowTemp {
			queriesItemTemp, err := strconv.ParseInt(queriesRowItem, 10, 64)
			checkError(err)
			queriesItem := int32(queriesItemTemp)
			queriesRow = append(queriesRow, queriesItem)
		}

		if len(queriesRow) != 3 {
			panic("Bad input")
		}

		queries = append(queries, queriesRow)
	}

	result := dynamicArray(n, queries)

	for i, resultItem := range result {
		fmt.Fprintf(writer, "%d", resultItem)

		if i != len(result)-1 {
			fmt.Fprintf(writer, "\n")
		}
	}

	fmt.Fprintf(writer, "\n")

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
