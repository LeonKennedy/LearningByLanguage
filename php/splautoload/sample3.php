<?php 

/*
 * $this 的例子
 *  伪变量
 */

spl_autoload_register(function ($class_name){
    require_once $class_name. '.php';
});

$obj = new Test();

