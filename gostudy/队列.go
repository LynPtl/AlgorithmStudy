package main

import (
	"container/list"
	"fmt"
)

func main() {
	// 初始化一个空的整型队列 q
	q := list.New()

	// 在队尾添加元素
	q.PushBack(10)
	q.PushBack(20)
	q.PushBack(30)

	// 检查队列是否为空，输出：false
	fmt.Println(q.Len() == 0)

	// 获取队列的大小，输出：3
	fmt.Println(q.Len())

	// 获取队列的队头元素
	// 输出：10
	front := q.Front().Value.(int)
	fmt.Println(front)

	// 删除队头元素
	q.Remove(q.Front())

	// 输出新的队头元素：20
	newFront := q.Front().Value.(int)
	fmt.Println(newFront)
}
