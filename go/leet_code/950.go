package leet_code

import "sort"

func deckRevealedIncreasing(deck []int) []int {
	var q []int
	for i:=0;i<len(deck);i++{
		q=append(q,i)
	}
	sort.Ints(deck)
	ans:=make([]int,len(deck))
	for _,card:=range deck{
		ans[q[0]]=card
		q=q[1:]
		if len(q)>0{
			q=append(q,q[0])
			q=q[1:]
		}
	}
	return ans
}
