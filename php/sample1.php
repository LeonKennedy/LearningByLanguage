<?php 

/*
 * 类相关的例子
 *  虚类  继承
 */

abstract class Event
{
    const TAG = 'EVENT';
    public static $tag = 'static_event';
    function getTag(){
	return self::TAG;
    }
    function getStaticTag(){
	return self::$tag;
    }
}

class AppointCreated extends Event
{
    const TAG = 'Appoitmnt';
    public static $tag = 'static_appointment';

}


$e = new AppointCreated();
var_dump($e->getTag());  // "EVENT"   还是基类常数
var_dump($e->getStaticTag());

var_dump(AppointCreated::getStaticTag());
