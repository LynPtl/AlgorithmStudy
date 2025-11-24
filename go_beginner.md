# Go 语言入门：LeetCode 常用数据结构

> 本文档旨在帮助新手快速掌握 Go 语言中常用的基础语法和数据结构。
>
> Happy Coding!

## 基础语法

官方入门[Go语言之旅](https://tour.go-zh.org)。

在深入数据结构之前，我们先快速了解一下 Go 的一些基础语法。

### 标准输出

Go 的 `fmt` 包提供了丰富的函数用于格式化和输出数据。`fmt.Println` 和 `fmt.Printf` 是最常用的两个。

```go
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
```

### 条件判断

Go 的 `if-else` 结构与其它语言类似，但条件不需要用括号括起来。

```go
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
```

### 循环

Go 只有一个循环关键字 `for`，但它能实现多种循环方式。

```go
package main

import (
	"fmt"
)

func main() {
	// 输出：0 1 2 3 4
	for i := 0; i < 5; i++ {
		fmt.Print(i, " ")
	}
	fmt.Println()

	num := 100
	// 输出：100 50 25 12 6 3 1
	for num > 0 {
		fmt.Print(num, " ")
		num /= 2
	}
	fmt.Println()
}
```
## 核心数据结构

掌握以下数据结构是刷 LeetCode 的基础。

### 动态数组（切片）

Go 的切片（Slice）是对底层数组的封装，提供了更强大、灵活的动态数组功能。

#### 初始化

```go
package main

import (
	"fmt"
)

func main() {
	// 初始化一个空的切片 nums
	var nums []int

	// 初始化一个大小为 7 的切片 nums，元素值默认都为 0
	nums = make([]int, 7)

	// 初始化一个包含元素 1, 3, 5 的切片 nums
	nums = []int{1, 3, 5}

	// 初始化一个大小为 7 的切片 nums，其值全都为 2
	nums = make([]int, 7)
	for i := range nums {
		nums[i] = 2
	}

	fmt.Println(nums)

	// 初始化一个大小为 3 * 3 的布尔切片 dp，其中的值都初始化为 true
	var dp [][]bool
	dp = make([][]bool, 3)
	for i := 0; i < len(dp); i++ {
		row := make([]bool, 3)
		for j := range row {
			row[j] = true
		}
		dp[i] = row
	}

	fmt.Println(dp)
}
```

#### 常用操作

```go
package main

import (
	"fmt"
)

func main() {
	n := 10
	// 初始化切片，大小为 10，元素值都为 0
	nums := make([]int, n)

	// 输出：false
	fmt.Println(len(nums) == 0)

	// 输出：10
	fmt.Println(len(nums))

	// 在切片尾部插入一个元素 20
	// append 函数会返回一个新的切片，所以需要将返回值重新赋值给 nums
	nums = append(nums, 20)
	// 输出：11
	fmt.Println(len(nums))

	// 得到切片最后一个元素
	// 输出：20
	fmt.Println(nums[len(nums)-1])

	// 删除切片的最后一个元素
	nums = nums[:len(nums)-1]
	// 输出：10
	fmt.Println(len(nums))

	// 可以通过索引直接取值或修改
	nums[0] = 11
	// 输出：11
	fmt.Println(nums[0])

	// 在索引 3 处插入一个元素 99
	// ... 是展开操作符，表示将切片中的元素展开
	nums = append(nums[:3], append([]int{99}, nums[3:]...)...)

	// 删除索引 2 处的元素
	nums = append(nums[:2], nums[3:]...)

	// 交换 nums[0] 和 nums[1]
	nums[0], nums[1] = nums[1], nums[0]

	// 遍历切片
	// 输出：0 11 99 0 0 0 0 0 0 0
	for _, num := range nums {
		fmt.Print(num, " ")
	}
	fmt.Println()
}
```

### 栈

Go 没有内置的栈结构，但可以用切片（Slice）轻松实现。栈遵循“后进先出”（LIFO）的原则。

```go
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
```

### 队列

队列遵循“先进先出”（FIFO）的原则。Go 的标准库 `container/list` 提供了一个双向链表，可以高效地实现队列。

```go
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
```

### 哈希表（Map）

Go 内置了 `map` 类型来实现哈希表，用于存储键值对。

#### 初始化

```go
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
```

#### 常用操作

```go
package main

import (
	"fmt"
)

func main() {
	// 初始化哈希表
	hashmap := make(map[int]string)
	hashmap[1] = "one"
	hashmap[2] = "two"
	hashmap[3] = "three"

	// 检查哈希表是否为空，输出：false
	fmt.Println(len(hashmap) == 0)

	// 获取哈希表的大小，输出：3
	fmt.Println(len(hashmap))

	// 查找指定键值是否存在
	// 输出：Key 2 -> two
	if val, exists := hashmap[2]; exists {
		fmt.Println("Key 2 ->", val)
	} else {
		fmt.Println("Key 2 not found.")
	}

	// 获取指定键对应的值，若不存在会返回空字符串
	// 输出：
	fmt.Println(hashmap[4])

	// 插入一个新的键值对
	hashmap[4] = "four"

	// 获取新插入的值，输出：four
	fmt.Println(hashmap[4])

	// 删除键值对
	delete(hashmap, 3)

	// 检查删除后键 3 是否存在
	// 输出：Key 3 not found.
	if val, exists := hashmap[3]; exists {
		fmt.Println("Key 3 ->", val)
	} else {
		fmt.Println("Key 3 not found.")
	}

	// 遍历哈希表
	// 输出（顺序可能不同）：
	// 1 -> one
	// 2 -> two
	// 4 -> four
	for key, value := range hashmap {
		fmt.Printf("%d -> %s\n", key, value)
	}
}
```

### 哈希集合 (Set)

Go 没有内置的集合类型，但可以用 `map[T]struct{}` 巧妙地实现。`struct{}` 是一个空结构体，不占用任何内存空间，非常适合用作集合的值。

```go
package main

import (
	"fmt"
)

func main() {
	// 初始化一个包含一些元素的哈希集合 hashset
	hashset := map[int]struct{}{
		1: {},
		2: {},
		3: {},
		4: {},
	}

	// 检查哈希集合是否为空，输出：false
	fmt.Println(len(hashset) == 0)

	// 获取哈希集合的大小，输出：4
	fmt.Println(len(hashset))

	// 查找指定元素是否存在
	// 输出：Element 3 found.
	if _, exists := hashset[3]; exists {
		fmt.Println("Element 3 found.")
	} else {
		fmt.Println("Element 3 not found.")
	}

	// 插入一个新的元素
	hashset[5] = struct{}{}

	// 删除一个元素
	delete(hashset, 2)
	// 输出：Element 2 not found.
	if _, exists := hashset[2]; exists {
		fmt.Println("Element 2 found.")
	} else {
		fmt.Println("Element 2 not found.")
	}

	// 遍历哈希集合
	// 输出（顺序可能不同）：
	// 1
	// 3
	// 4
	// 5
	for element := range hashset {
		fmt.Println(element)
	}
}
```

### 双向链表

Go 的 `container/list` 包提供了一个功能完备的双向链表实现。

```go
package main

import (
	"container/list"
	"fmt"
)

func main() {
	// 初始化链表
	lst := list.New()
	lst.PushBack(1)
	lst.PushBack(2)
	lst.PushBack(3)
	lst.PushBack(4)
	lst.PushBack(5)

	// 检查链表是否为空，输出：false
	fmt.Println(lst.Len() == 0)

	// 获取链表的大小，输出：5
	fmt.Println(lst.Len())

	// 在链表头部插入元素 0
	lst.PushFront(0)
	// 在链表尾部插入元素 6
	lst.PushBack(6)

	// 获取链表头部和尾部元素，输出：0 6
	front := lst.Front().Value.(int)
	back := lst.Back().Value.(int)
	fmt.Println(front, back)

	// 删除链表头部元素
	lst.Remove(lst.Front())
	// 删除链表尾部元素
	lst.Remove(lst.Back())

	// 在链表中插入元素
	// 移动到第三个位置
	third := lst.Front().Next().Next()
	lst.InsertBefore(99, third)

	// 删除链表中某个元素
	second := lst.Front().Next()
	lst.Remove(second)

	// 遍历链表
	// 输出：1 99 3 4 5
	for e := lst.Front(); e != nil; e = e.Next() {
		fmt.Print(e.Value.(int), " ")
	}
	fmt.Println()
}
```
