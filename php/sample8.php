<?php
class Strings
{
    static function fix_string($a)
    {
        echo
            xdebug_call_class(1).
            "::".
            xdebug_call_function(1).
            " is called at ".
            xdebug_call_file(1).
            ":".
            xdebug_call_line(1).
            "\n";
    }
}

$ret = Strings::fix_string( 'Derick' );
?>