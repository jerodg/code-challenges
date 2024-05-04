// Package main provides a solution to the problem of counting apples and oranges falling within a certain range.
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

// countApplesAndOranges counts the number of apples and oranges that fall on Sam's house.
//
// It accepts six parameters:
// - s: an integer representing the start point of Sam's house location.
// - t: an integer representing the end point of Sam's house location.
// - a: an integer representing the location of the Apple tree.
// - b: an integer representing the location of the Orange tree.
// - apples: a slice of integers representing the distances at which each apple falls from tree a.
// - oranges: a slice of integers representing the distances at which each orange falls from tree b.
//
// The function does not return a value. It prints two integers to stdout: the first line contains the number of apples
// that fall on Sam's house, and the second line contains the number of oranges.
//
// The function iterates over the distances at which each apple and orange falls, and increments a counter if the fruit
// falls on Sam's house.
//
// Time complexity analysis:
// - Best-case: O(n + m), when all fruits fall on Sam's house.
// - Worst-case: O(n + m), when no fruits fall on Sam's house.
// - Average-case: O(n + m), as we always have to check each fruit.
func countApplesAndOranges(s int32, t int32, a int32, b int32, apples []int32, oranges []int32) {
	appleCount := 0
	orangeCount := 0

	for _, d := range apples {
		if s <= a+d && a+d <= t {
			appleCount++
		}
	}

	for _, d := range oranges {
		if s <= b+d && b+d <= t {
			orangeCount++
		}
	}

	fmt.Println(appleCount)
	fmt.Println(orangeCount)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	firstMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	sTemp, err := strconv.ParseInt(firstMultipleInput[0], 10, 64)
	checkError(err)
	s := int32(sTemp)

	tTemp, err := strconv.ParseInt(firstMultipleInput[1], 10, 64)
	checkError(err)
	t := int32(tTemp)

	secondMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	aTemp, err := strconv.ParseInt(secondMultipleInput[0], 10, 64)
	checkError(err)
	a := int32(aTemp)

	bTemp, err := strconv.ParseInt(secondMultipleInput[1], 10, 64)
	checkError(err)
	b := int32(bTemp)

	thirdMultipleInput := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	mTemp, err := strconv.ParseInt(thirdMultipleInput[0], 10, 64)
	checkError(err)
	m := int32(mTemp)

	nTemp, err := strconv.ParseInt(thirdMultipleInput[1], 10, 64)
	checkError(err)
	n := int32(nTemp)

	applesTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var apples []int32

	for i := 0; i < int(m); i++ {
		applesItemTemp, err := strconv.ParseInt(applesTemp[i], 10, 64)
		checkError(err)
		applesItem := int32(applesItemTemp)
		apples = append(apples, applesItem)
	}

	orangesTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var oranges []int32

	for i := 0; i < int(n); i++ {
		orangesItemTemp, err := strconv.ParseInt(orangesTemp[i], 10, 64)
		checkError(err)
		orangesItem := int32(orangesItemTemp)
		oranges = append(oranges, orangesItem)
	}

	countApplesAndOranges(s, t, a, b, apples, oranges)
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
