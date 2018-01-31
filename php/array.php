<?php

$a = array();
$b = array(1,2,3);
$b['a'] = 'ba';
$b['b'] = ['b1'];
$b['b'][] = 'b2';
$b['c'][] = 'c1';
$b['c']['cc1'] = 'cc1';
$b['c'][] = array('cc1'=>'cc1');


var_dump($b);

