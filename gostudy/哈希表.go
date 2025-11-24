package main

import (
	"fmt"
)

func main() {
	// 初始化一个空的哈希表 hashmap
	var hashmap map[int]string
	hashmap = make(map[int]string)

	// 初始化一个包含一些键值对的哈希表 hashmap
	hashmap = map[int]string{
		1: "one",
		2: "two",
		3: "three",
	}

	fmt.Println(hashmap)
}
