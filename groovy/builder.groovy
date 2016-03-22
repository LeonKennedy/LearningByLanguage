import groovy.xml.*
def page = new MarkBuilder()
page.html{
    head {title 'Hello'}
    body{
        ul{
            for(count in 1..10){
                li "world $count"
            }
        }
    }
}
