package main

import (
	"fmt"
)

func main() {
	// 初始化一个空的整型栈 s
	var s []int

	// 向栈顶（切片末尾）添加元素
	s = append(s, 10)
	s = append(s, 20)
	s = append(s, 30)

	// 检查栈是否为空，输出：false
	fmt.Println(len(s) == 0)

	// 获取栈的大小，输出：3
	fmt.Println(len(s))

	// 获取栈顶元素，输出：30
	fmt.Println(s[len(s)-1])

	// 删除栈顶元素
	s = s[:len(s)-1]

	// 输出新的栈顶元素：20
	fmt.Println(s[len(s)-1])
}
