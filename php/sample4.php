<?php
class A {
    public static function foo() {
        static::who();
    }

    public static function who() {
        echo __CLASS__."\n";
    }
}

class B extends A {
    public static function test() {
        A::foo();
        parent::foo();
        self::foo();
    }

    public static function test_b() {
        A::who();
        parent::who();
        self::who();
        static::who();
    }

    public static function who() {
        echo __CLASS__."\n";
    }
}

class C extends B {
    public static function who() {
        echo __CLASS__."\n";
    }

    public static function foo() {
        static::who();
    }

    public static function test_c() {
        A::who();
        parent::who();
        self::who();
        static::who();
    }
}



C::test_c();
?>
