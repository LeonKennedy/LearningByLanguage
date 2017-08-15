const Koa = require('koa');
const app = new Koa();
const router = require('koa-router')();
const bodyparser = require('koa-bodyparser');
app.use(bodyparser());

app.use(async (ctx, next) => {
    const start = Date.now();
    await next();
    const ms = Date.now() - start;
    ctx.set('X-Response-Time', `${ms}ms`);
});

app.use(async (ctx, next) => {
    const start = Date.now();
    await next();
    const ms = Date.now() - start;
    console.log(`${ctx.method} ${ctx.url} - ${ms}ms`);
});
router.get('/hello/:name', async (ctx, next) => {
    var name = ctx.params.name;
    ctx.response.body = `<h1> Hello, ${name}! </h1>`;
});

router.get('/', async (ctx, next) => {
    ctx.response.body = `<h2> Index </h1>
    <form action="/signin" method="post">
        <p>Name: <input name="name" value="olenji" /></p>
        <p>Password: <input name="password" type="password" /></p>
        <p><input type="submit" value="submit" /></p>
    </form>`;

});

router.post('/signin', async (ctx, next) => {
    var name =  ctx.request.body.name || '',
    password =  ctx.request.body.password || '';
    console.log(`signin with name: ${name}, password: ${password}`);
    if (name === 'koa' && password === '12345') {
        ctx.response.body = `<h1>Welcome, ${name}!</h1>`;
    } else {
        ctx.response.body = `<h1>Login failed!</h1>
        <p><a href="/">Try again</a></p>`;
    }
});
app.use(router.routes());

app.listen(4000);
