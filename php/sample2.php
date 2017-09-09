<?php 

/*
 * $this 的例子
 *  伪变量
 */


class Test
{
    static public function getNews()
    {
	return new static;
    }
}

class Child extends Test
{}

$obj1 = new Test();
$obj2 = new $obj1;
var_dump($obj1 !== $obj2);

$obj3 = Test::getNews();
var_dump($obj3 instanceof Test);

$obj4 = Child::getNews();
var_dump($obj4 instanceof Child);
