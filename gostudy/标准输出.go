package main

import (
	"fmt"
)

func main() {
	a := 10

	// 输出：10
	fmt.Println(a)

	// 可以串联输出
	// 输出：Hello, World!
	fmt.Println("Hello" + ", " + "World!")

	s := "abc"
	// 输出：abc 10
	fmt.Println(s, a)

	// 格式化输出
	// 输出：abc 10
	fmt.Printf("%s %d\n", s, a)
}
