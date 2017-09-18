<?php

class Container
{
    protected $bindings = [];

    public function bind($abstract, $concrete = null, $shared = false)
    {
        if (!$concrete instanceof Closure){
            $concrete =  $this->getClouse($abstract, $concrete);
        }
        $this->bindings[$abstract] = compact('concrete', 'shared');
        // var_dump($this->bindings);
    }

    protected function getClouse($abstract, $concrete)
    {
        return function($c) use($abstract, $concrete){
            $method = ($abstract == $concrete) ? 'build' : 'make';
            return $c->$method($concrete);
        };
    }

    public function make($abstract)
    {
        $concrete = $this->getConcrete($abstract);
        //TODO
        if ($this->isBuildable($concrete, $abstract)){
            $object = $this->build($concrete);
        }else{
            $object = $this->make($concrete);
        }
      
        return $object;
    }

    protected function isBuildable($concrete, $abstract)
    {
        return $concrete === $abstract || $concrete instanceof Closure;
    }

    protected function getConcrete($abstract)
    {
        if ( ! isset($this->bindings[$abstract])){
            return $abstract;
        }
        return $this->bindings[$abstract]['concrete'];
    }

    public function build($concrete)
    {
        if ($concrete instanceof Closure){
            return $concrete($this);
        }

        //TODO
        $reflector = new ReflectionClass($concrete);
        if ( ! $reflector->isInstantiable()){
            echo $message = "Target [$concrete] is not instantiable.";
        }

        $constructor = $reflector->getConstructor();
        if (is_null($constructor)) {
            return new $concrete;
        }

        $dependencies = $constructor->getParameters();
        $instances = $this->getDependencies($dependencies);
        return $reflector->newInstanceArgs($instances);


    }

    protected function getDependencies($parameters)
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

    protected function resolveClass(ReflectionParameter $parameter)
    {
        return $this->make($parameter->getClass()->name);
    }
}

interface Visit
{
    public function go();
}

class Leg implements Visit
{
    public function go()
    {
        echo "Walk!!";
    }
}

class Car implements Visit
{
    public function go()
    {
        echo "Drive car to go!!";
    }
}

class Train implements Visit
{
    public function go()
    {
        echo "To go by Train!!";
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


$app = new Container();
$app->bind('Visit', 'Train');
$app->bind('traveller', 'Traveller');

$tra = $app->make("traveller");
$tra->visitTibei();