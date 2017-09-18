<?php
interface Visit
{
    public function go();
}

class Leg implements Visit
{
    public function go()
    {
        echo "Walk!!\n";
    }
}

class Car implements Visit
{
    public function go()
    {
        echo "Drive car to go!!\n";
    }
}

class Train implements Visit
{
    public function go()
    {
        echo "To go by Train!!\n";
    }
}

class Traveller
{
    protected $trafficTool;
    public function __construct(Visit $trafficTool)
    {
        $this->trafficTool = $trafficTool;
    }

    public function visitTibei(){
        $this->trafficTool->go();
    }
}

function getDependencies($parameters)
{
    $dependencies = [];
    foreach ($parameters as $parameter){
        $dependency = $parameter->getClass();
        if ( is_null($dependency)){
            $dependencies[] = NUll;
        }else{
            $dependencies[] = $this->resolveClass($parameter);
        }
    }
    return (array)$dependencies;
}

$reflector = new ReflectionClass('Traveller');

if ( ! $reflector->isInstantiable()){
    echo $message = "Target [$concrete] is not instantiable.";
}

$constructor = $reflector->getConstructor();
$dependencies = $constructor->getParameters();
foreach($dependencies as $dependency){
    var_dump($dependency->getClass());
}
$instances[] = new Train();
$a =  $reflector->newInstanceArgs($instances);
$a->visitTibei();