package main

import (
	"fmt"
)

func main() {
	a := 10

	if a > 5 {
		fmt.Println("a > 5")
	} else if a == 5 {
		fmt.Println("a == 5")
	} else {
		fmt.Println("a < 5")
	}
	// 输出：a > 5
}
