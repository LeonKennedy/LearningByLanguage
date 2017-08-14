const Koa = require('koa');
const app = new Koa();
const router = require('koa-router')();

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
    ctx.response.body = `<h2> Index </h1>`;

});
app.use(router.routes());

app.listen(3000);
